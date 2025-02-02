from blue_assistant.chat.context import ChatContext

from blue_objects import objects


def test_context():
    object_name = objects.unique_object("test_context")

    context = ChatContext(
        object_name,
        load_history=False,
    )

    assert context.chat(
        interactive=False,
        verbose=True,
    )

    assert context.save()
