from blue_assistant.script.generic import GenericScript
from blue_assistant import env


def test_generic_script():
    script = GenericScript(
        object_name=env.BLUE_ASSISTANT_TEST_OBJECT,
        verbose=True,
    )
