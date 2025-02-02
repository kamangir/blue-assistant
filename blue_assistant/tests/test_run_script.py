from blue_assistant.script.generic import GenericScript
from blue_assistant.script.functions import load_script
from blue_assistant import env


def test_run_script():
    success, script = load_script(
        object_name=env.BLUE_ASSISTANT_TEST_OBJECT,
        verbose=True,
    )
    assert success
    assert isinstance(script, GenericScript)

    assert script.run()
