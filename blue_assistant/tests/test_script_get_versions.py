import pytest

from blue_objects import objects

from blue_assistant.script.repository import list_of_script_classes
from blue_assistant.script.repository.base.classes import BaseScript
from blue_assistant.script.repository.functions import get_script_versions


@pytest.mark.parametrize(
    ["script_name"],
    [[script_class.name] for script_class in list_of_script_classes],
)
def test_script_get_versions(
    script_name: str,
):
    list_of_versions = get_script_versions(script_name)
    assert isinstance(list_of_versions, list)
