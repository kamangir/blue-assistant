from blue_options.env import load_config, load_env, get_env

load_env(__name__)
load_config(__name__)


BLUE_ASSISTANT_TEXT_DEFAULT_MODEL = get_env("BLUE_ASSISTANT_TEXT_DEFAULT_MODEL")

BLUE_ASSISTANT_TEXT_MAX_TOKENS = get_env("BLUE_ASSISTANT_TEXT_MAX_TOKENS", 2000)

BLUE_ASSISTANT_IMAGE_DEFAULT_MODEL = get_env("BLUE_ASSISTANT_IMAGE_DEFAULT_MODEL")

BLUE_ASSISTANT_IMAGE_DEFAULT_QUALITY = get_env("BLUE_ASSISTANT_IMAGE_DEFAULT_QUALITY")

BLUE_ASSISTANT_IMAGE_DEFAULT_SIZE = get_env("BLUE_ASSISTANT_IMAGE_DEFAULT_SIZE")

HUE_BRIDGE_IP_ADDRESS = get_env("HUE_BRIDGE_IP_ADDRESS")

HUE_BRIDGE_USERNAME = get_env("HUE_BRIDGE_USERNAME")
HUE_TEST_DEFAULT_INTERVAL = get_env("HUE_TEST_DEFAULT_INTERVAL", 0.01)
