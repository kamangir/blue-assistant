from blue_assistant.script.functions import load_script
from blue_assistant import env


def test_generic_script():
    success, script = load_script(
        object_name=env.BLUE_ASSISTANT_TEST_OBJECT,
        verbose=True,
        download=True,
    )

    assert success

    assert script.run()
