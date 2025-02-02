from blue_objects import objects

from blue_assistant.chat.functions import chat


def test_chat():
    object_name = objects.unique_object("test_chat")

    assert chat(
        object_name=object_name,
        interactive=False,
    )
