from blue_assistant.script.repository import (
    list_of_script_classes,
    list_of_script_names,
)
from blue_assistant.script.repository.generic.classes import GenericScript


def test_script_list_of_script_classes():
    assert list_of_script_classes

    for script_class in list_of_script_classes:
        assert issubclass(script_class, GenericScript)


def test_script_list_of_script_names():
    assert list_of_script_names

    for script_name in list_of_script_names:
        assert isinstance(script_name, str)

    assert len(list_of_script_names) == len(list_of_script_classes)

    # no repeats
    assert len(list(set(list_of_script_names))) == len(list_of_script_names)
