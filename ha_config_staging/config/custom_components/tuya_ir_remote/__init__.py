from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
import hashlib
import hmac
import json
import logging
import time
from typing import Any

import aiohttp
import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_NAME
from homeassistant.core import HomeAssistant, ServiceCall
import homeassistant.helpers.config_validation as cv

from .const import (
    CONF_ACCESS_ID,
    CONF_ACCESS_SECRET,
    CONF_CATEGORY_ID,
    CONF_DEVICES,
    CONF_ENDPOINT,
    CONF_INFRARED_ID,
    CONF_REMOTE_ID,
    CONF_REMOTE_INDEX,
    DEFAULT_ENDPOINT,
    DEVICE_PROJECTOR,
    DEVICE_SOUNDBAR,
    DOMAIN,
    PROJECTOR_BUTTON_TO_KEY,
    SERVICE_SEND_BUTTON,
    SERVICE_SEND_KEY,
    SOUNDBAR_BUTTON_TO_KEY,
    TOKEN_REFRESH_MARGIN_SECONDS,
)

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_ACCESS_ID): cv.string,
                vol.Required(CONF_ACCESS_SECRET): cv.string,
                vol.Optional(CONF_ENDPOINT, default=DEFAULT_ENDPOINT): cv.string,
                vol.Required(CONF_INFRARED_ID): cv.string,
                vol.Required(CONF_DEVICES): {
                    vol.Required(DEVICE_SOUNDBAR): {
                        vol.Required(CONF_REMOTE_ID): cv.string,
                        vol.Required(CONF_REMOTE_INDEX): vol.Coerce(int),
                        vol.Required(CONF_CATEGORY_ID): vol.Coerce(int),
                    },
                    vol.Required(DEVICE_PROJECTOR): {
                        vol.Required(CONF_REMOTE_ID): cv.string,
                        vol.Required(CONF_REMOTE_INDEX): vol.Coerce(int),
                        vol.Required(CONF_CATEGORY_ID): vol.Coerce(int),
                    },
                },
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)

SEND_BUTTON_SCHEMA = vol.Schema(
    {
        vol.Required("device"): vol.In([DEVICE_SOUNDBAR, DEVICE_PROJECTOR]),
        vol.Required("button"): cv.string,
    }
)

SEND_KEY_SCHEMA = vol.Schema(
    {
        vol.Required("device"): vol.In([DEVICE_SOUNDBAR, DEVICE_PROJECTOR]),
        vol.Required("key"): cv.string,
    }
)


@dataclass
class DeviceConfig:
    remote_id: str
    remote_index: int
    category_id: int


class TuyaIRClient:
    def __init__(
        self,
        *,
        session: aiohttp.ClientSession,
        endpoint: str,
        access_id: str,
        access_secret: str,
        infrared_id: str,
        devices: dict[str, DeviceConfig],
    ) -> None:
        self._session = session
        self._endpoint = endpoint
        self._access_id = access_id
        self._access_secret = access_secret
        self._infrared_id = infrared_id
        self._devices = devices

        self._access_token: str | None = None
        self._token_expiry: datetime | None = None

    @property
    def base_url(self) -> str:
        return f"https://{self._endpoint}"

    def _content_sha256(self, body: str) -> str:
        return hashlib.sha256(body.encode("utf-8")).hexdigest()

    def _sign(self, payload: str) -> str:
        return hmac.new(
            self._access_secret.encode("utf-8"),
            payload.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest().upper()

    def _build_string_to_sign(self, method: str, body: str, path_with_query: str) -> str:
        content_hash = self._content_sha256(body)
        return "\n".join([method.upper(), content_hash, "", path_with_query])

    async def _request(
        self,
        *,
        method: str,
        path_with_query: str,
        body: dict[str, Any] | None = None,
        use_token: bool = True,
    ) -> dict[str, Any]:
        body_text = json.dumps(body or {}, separators=(",", ":"), ensure_ascii=False)
        string_to_sign = self._build_string_to_sign(method, body_text, path_with_query)

        t = str(int(time.time() * 1000))
        nonce = "kira-ha-tuya-ir"

        access_token = self._access_token if use_token else ""
        sign_payload = f"{self._access_id}{access_token}{t}{nonce}{string_to_sign}"
        sign = self._sign(sign_payload)

        headers = {
            "client_id": self._access_id,
            "sign": sign,
            "t": t,
            "sign_method": "HMAC-SHA256",
            "nonce": nonce,
            "Content-Type": "application/json",
        }
        if use_token and self._access_token:
            headers["access_token"] = self._access_token

        url = f"{self.base_url}{path_with_query}"
        _LOGGER.debug("Tuya IR request %s %s", method, path_with_query)

        async with self._session.request(method, url, headers=headers, data=body_text) as resp:
            txt = await resp.text()
            try:
                data = json.loads(txt)
            except json.JSONDecodeError:
                raise RuntimeError(f"Tuya IR invalid JSON response: HTTP {resp.status} {txt}")

        if resp.status >= 400:
            raise RuntimeError(f"Tuya IR HTTP error {resp.status}: {data}")

        return data

    async def ensure_token(self, force_refresh: bool = False) -> None:
        now = datetime.now(UTC)
        if (
            not force_refresh
            and self._access_token
            and self._token_expiry
            and now < (self._token_expiry - timedelta(seconds=TOKEN_REFRESH_MARGIN_SECONDS))
        ):
            return

        _LOGGER.info("Refreshing Tuya IR token")
        path = "/v1.0/token?grant_type=1"
        data = await self._request(method="GET", path_with_query=path, body={}, use_token=False)
        if not data.get("success"):
            raise RuntimeError(f"Tuya token refresh failed: {data}")

        result = data.get("result", {})
        token = result.get("access_token")
        expire_time = int(result.get("expire_time", 0))
        if not token or not expire_time:
            raise RuntimeError(f"Tuya token payload incomplete: {data}")

        self._access_token = token
        self._token_expiry = now + timedelta(seconds=expire_time)

    async def send_key(self, *, device: str, key: str) -> dict[str, Any]:
        await self.ensure_token()

        dev = self._devices[device]
        path = f"/v2.0/infrareds/{self._infrared_id}/remotes/{dev.remote_id}/command"
        payload = {
            "remote_index": dev.remote_index,
            "category_id": dev.category_id,
            "key": key,
        }

        data = await self._request(method="POST", path_with_query=path, body=payload, use_token=True)

        if not data.get("success"):
            code = str(data.get("code", ""))
            if code in {"1010", "1106", "1011"}:
                _LOGGER.warning("Tuya command failed due to token/auth (%s). Retrying after refresh.", code)
                await self.ensure_token(force_refresh=True)
                data = await self._request(method="POST", path_with_query=path, body=payload, use_token=True)

        return data


async def async_setup(hass: HomeAssistant, config: dict[str, Any]) -> bool:
    conf = config.get(DOMAIN)
    if not conf:
        return True

    devices = {
        name: DeviceConfig(
            remote_id=cfg[CONF_REMOTE_ID],
            remote_index=cfg[CONF_REMOTE_INDEX],
            category_id=cfg[CONF_CATEGORY_ID],
        )
        for name, cfg in conf[CONF_DEVICES].items()
    }

    client = TuyaIRClient(
        session=aiohttp.ClientSession(),
        endpoint=conf[CONF_ENDPOINT],
        access_id=conf[CONF_ACCESS_ID],
        access_secret=conf[CONF_ACCESS_SECRET],
        infrared_id=conf[CONF_INFRARED_ID],
        devices=devices,
    )

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN]["client"] = client
    hass.data[DOMAIN]["devices"] = devices

    async def _handle_send_button(call: ServiceCall) -> None:
        device = call.data["device"]
        button = call.data["button"]
        mapping = SOUNDBAR_BUTTON_TO_KEY if device == DEVICE_SOUNDBAR else PROJECTOR_BUTTON_TO_KEY
        if button not in mapping:
            raise ValueError(f"Unsupported button '{button}' for {device}")
        key = mapping[button]
        data = await client.send_key(device=device, key=key)
        if not data.get("success"):
            raise RuntimeError(f"Tuya command failed: {data}")

    async def _handle_send_key(call: ServiceCall) -> None:
        device = call.data["device"]
        key = call.data["key"]
        data = await client.send_key(device=device, key=key)
        if not data.get("success"):
            raise RuntimeError(f"Tuya command failed: {data}")

    hass.services.async_register(DOMAIN, SERVICE_SEND_BUTTON, _handle_send_button, schema=SEND_BUTTON_SCHEMA)
    hass.services.async_register(DOMAIN, SERVICE_SEND_KEY, _handle_send_key, schema=SEND_KEY_SCHEMA)

    _LOGGER.info("Tuya IR Remote loaded with devices: %s", ", ".join(devices.keys()))
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    return True
