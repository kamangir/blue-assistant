from abcli.tests.test_env import test_abcli_env
from blue_objects.tests.test_env import test_blue_objects_env

from blue_assistant import env


def test_required_env():
    test_abcli_env()
    test_blue_objects_env()


def test_blue_assistant_env():
    # assert env.BLUE_ASSISTANT_MODEL

    assert True
