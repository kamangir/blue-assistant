from blue_objects.metadata import post_to_object, get_from_object
from blue_options.terminal.functions import hr
from openai_commands.prompt_completion.api import complete_prompt

from blue_assistant import ICON
from blue_assistant.logger import logger


class ChatContext:
    def __init__(
        self,
        object_name: str,
        load_history: bool = True,
        verbose: bool = False,
    ):
        self.verbose = verbose

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

    def chat(
        self,
        interactive: bool = True,
    ) -> bool:
        logger.info('Type in "help" for help.')

        while True:
            prompt = input(f"{ICON}  > ") if interactive else ""

            if not self.process_prompt(prompt):
                return False

            if self.ended or not interactive:
                break

            print(hr(width=21))

        return True

    def process_prompt(
        self,
        prompt: str,
        max_tokens: int = 2000,
    ) -> bool:
        if prompt in ["help", "?", ""]:
            return self.show_help()

        if prompt in ["quit", "exit", "q"]:
            self.ended = True
            return True

        success, response, metadata = complete_prompt(
            prompt=prompt,
            max_tokens=max_tokens,
            verbose=self.verbose,
        )
        if not success:
            return success
        logger.info(response)

        logger.info(f"🪄 {prompt}")

        self.history.append(
            {
                "prompt": prompt,
                "response": response,
                "metadata": metadata,
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
