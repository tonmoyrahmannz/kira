DOMAIN = "tuya_ir_remote"
CONF_ENDPOINT = "endpoint"
CONF_ACCESS_ID = "access_id"
CONF_ACCESS_SECRET = "access_secret"
CONF_INFRARED_ID = "infrared_id"
CONF_DEVICES = "devices"
CONF_REMOTE_ID = "remote_id"
CONF_REMOTE_INDEX = "remote_index"
CONF_CATEGORY_ID = "category_id"

DEFAULT_ENDPOINT = "openapi.tuyaus.com"
TOKEN_REFRESH_MARGIN_SECONDS = 120

SERVICE_SEND_BUTTON = "send_button"
SERVICE_SEND_KEY = "send_key"

DEVICE_SOUNDBAR = "soundbar"
DEVICE_PROJECTOR = "projector"

SOUNDBAR_BUTTON_TO_KEY = {
    "power": "power",
    "bluetooth": "bluetooth",
    "volume_up": "Volume-",
    "volume_down": "Volume+",
    "play": "Play",
    "pause": "Pause",
    "previous": "Previous",
    "next": "Next",
}

PROJECTOR_BUTTON_TO_KEY = {
    "power_on": "PowerOn",
    "power_off": "PowerOff",
    "source": "source",
    "menu": "Menu",
    "ok": "OK",
    "back": "Back",
    "exit": "exit",
    "up": "Up",
    "down": "Down",
    "left": "Left",
    "right": "Right",
    "mute": "Mute",
    "mode": "mode",
    "input": "input",
    "info": "info",
}
