from typing import Union

from blue_objects.metadata import post_to_object, get_from_object

from blue_assistant.logger import logger


class ChatContext:
    def __init__(
        self,
        object_name: str,
        load_history: bool = True,
    ):
        self.object_name = object_name

        self.history = (
            get_from_object(
                self.object_name,
                "history",
                [],
            )
            if load_history
            else []
        )

    def process(self, prompt: str) -> Union[True, False, None]:
        if prompt == "help":
            return self.show_help()

        if prompt == "quit":
            return None

        if prompt == "break":
            return False

        logger.info(f"🪄 {prompt}")

        return True

    def save(self) -> bool:
        return post_to_object(
            self.object_name,
            "history",
            self.history,
        )

    def show_help(self) -> bool:
        for command, description in {
            "help": "show this help.",
            "quit": "quit the chat.",
        }.items():
            logger.info(f"{command}: {description}")
        return True
