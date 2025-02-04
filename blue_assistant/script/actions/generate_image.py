from blue_objects import file, objects
from openai_commands.image_generation.api import OpenAIImageGenerator

from blue_assistant.env import (
    BLUE_ASSISTANT_IMAGE_DEFAULT_MODEL,
    BLUE_ASSISTANT_IMAGE_DEFAULT_SIZE,
    BLUE_ASSISTANT_IMAGE_DEFAULT_QUALITY,
)
from blue_assistant.script.actions.generic import GenericAction
from blue_assistant.script.repository.base.classes import BaseScript
from blue_assistant.logger import logger


class GenerateImageAction(GenericAction):
    name = file.name(__file__)

    def __init__(
        self,
        script: BaseScript,
    ):
        super().__init__(script=script)

        self.generator = OpenAIImageGenerator(
            model=BLUE_ASSISTANT_IMAGE_DEFAULT_MODEL,
            verbose=self.script.verbose,
        )

    # https://platform.openai.com/docs/guides/images
    def perform(
        self,
        node_name: str,
    ) -> bool:
        if not super().perform(node_name=node_name):
            return False

        filename = f"{node_name}.png"

        success = self.generator.generate(
            prompt=self.script.nodes[node_name]["prompt"],
            filename=objects.path_of(
                filename=filename,
                object_name=self.script.object_name,
                create=True,
            ),
            quality=(
                BLUE_ASSISTANT_IMAGE_DEFAULT_QUALITY if self.script.test_mode else "hd"
            ),
            size=(
                BLUE_ASSISTANT_IMAGE_DEFAULT_SIZE
                if self.script.test_mode
                else "1792x1024"
            ),
        )[0]

        if success:
            self.script.nodes[node_name]["filename"] = filename

        return success
