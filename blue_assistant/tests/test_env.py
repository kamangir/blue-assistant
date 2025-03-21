from abcli.tests.test_env import test_abcli_env
from blue_objects.tests.test_env import test_blue_objects_env

from blue_assistant import env


def test_required_env():
    test_abcli_env()
    test_blue_objects_env()


def test_blue_assistant_env():
    assert env.BLUE_ASSISTANT_TEXT_DEFAULT_MODEL
    assert env.BLUE_ASSISTANT_TEXT_MAX_TOKENS

    assert env.BLUE_ASSISTANT_IMAGE_DEFAULT_MODEL
    assert env.BLUE_ASSISTANT_IMAGE_DEFAULT_QUALITY
    assert env.BLUE_ASSISTANT_IMAGE_DEFAULT_SIZE

    assert env.HUE_BRIDGE_IP_ADDRESS
    assert env.HUE_BRIDGE_USERNAME
    assert env.HUE_MAX_SATURATION

    assert env.RAG_DEFAULT_DOCUMENTS_OBJECT_NAME

    assert env.HUGGINGFACEHUB_API_TOKEN
