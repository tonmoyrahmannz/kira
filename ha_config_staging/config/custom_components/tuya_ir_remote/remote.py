from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.remote import RemoteEntity
from homeassistant.const import CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import (
    DEVICE_PROJECTOR,
    DEVICE_SOUNDBAR,
    DOMAIN,
    PROJECTOR_BUTTON_TO_KEY,
    SOUNDBAR_BUTTON_TO_KEY,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(
    hass: HomeAssistant,
    config: dict[str, Any],
    async_add_entities: AddEntitiesCallback,
    discovery_info: dict[str, Any] | None = None,
) -> None:
    data = hass.data.get(DOMAIN)
    if not data:
        _LOGGER.error("%s is not configured. Add tuya_ir_remote: to configuration.yaml first.", DOMAIN)
        return

    client = data["client"]
    entities = [
        TuyaIRVirtualRemote(hass, client, DEVICE_SOUNDBAR, "Soundbar IR Remote", SOUNDBAR_BUTTON_TO_KEY),
        TuyaIRVirtualRemote(hass, client, DEVICE_PROJECTOR, "Projector IR Remote", PROJECTOR_BUTTON_TO_KEY),
    ]
    async_add_entities(entities)


class TuyaIRVirtualRemote(RemoteEntity):
    _attr_should_poll = False

    def __init__(self, hass: HomeAssistant, client, device: str, name: str, mapping: dict[str, str]) -> None:
        self.hass = hass
        self._client = client
        self._device = device
        self._mapping = mapping
        self._attr_name = name
        self._attr_unique_id = f"tuya_ir_remote_{device}"
        self._attr_is_on = True

    async def async_turn_on(self, **kwargs: Any) -> None:
        self._attr_is_on = True

    async def async_turn_off(self, **kwargs: Any) -> None:
        self._attr_is_on = False

    async def async_send_command(self, command: list[str], **kwargs: Any) -> None:
        for item in command:
            key = self._mapping.get(item, item)
            data = await self._client.send_key(device=self._device, key=key)
            if not data.get("success"):
                raise RuntimeError(f"Tuya command failed for {self._device}:{item} -> {data}")
