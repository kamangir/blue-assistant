from blue_objects.metadata import post_to_object, get_from_object

from blue_assistant.logger import logger


class ChatContext:
    def __init__(
        self,
        object_name: str,
        load_history: bool = True,
    ):
        self.ended: bool = False

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

    def process(self, prompt: str) -> bool:
        if prompt in ["help", "?", ""]:
            return self.show_help()

        if prompt in ["quit", "exit", "q"]:
            self.ended = True
            return True

        logger.info(f"🪄 {prompt}")

        self.history.append(
            {
                "prompt": prompt,
            }
        )

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
