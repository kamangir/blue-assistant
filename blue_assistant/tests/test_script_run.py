import pytest

from blue_objects import objects

from blue_assistant.script.repository import list_of_script_classes
from blue_assistant.script.repository.base.classes import BaseScript
from blue_assistant.script.load import load_script


@pytest.mark.parametrize(
    ["script_name"],
    [[script_class.name] for script_class in list_of_script_classes] + [["void"]],
)
def test_scripts_run(script_name: str):
    expected_success: bool = script_name != "void"

    object_name = objects.unique_object(f"test_scripts_run-{script_name}")

    success, script = load_script(
        script_name=script_name,
        object_name=object_name,
        test_mode=True,
        verbose=True,
    )
    assert success == expected_success
    assert script.test_mode
    assert isinstance(script, BaseScript)

    if expected_success:
        assert script.run()
