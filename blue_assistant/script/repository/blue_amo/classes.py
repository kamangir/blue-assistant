from typing import Dict
from tqdm import tqdm

from blue_objects import file, path
from blue_objects.metadata import post_to_object

from blue_assistant.script.repository.generic.classes import GenericScript
from blue_assistant.logger import logger


class BlueAmoScript(GenericScript):
    name = path.name(file.path(__file__))

    def run(
        self,
        object_name: str,
    ) -> bool:
        if not super().run(object_name=object_name):
            return False

        metadata: Dict[Dict] = {"nodes": {}}
        success: bool = False
        for node_name, node in tqdm(self.nodes.items()):
            logger.info(
                "{}{}".format(
                    node_name,
                    f": {node}" if self.verbose else " ...",
                )
            )

            action = node.get("action", "unknown")

            if action == "generate_image":
                logger.info("🪄 generating image ...")
                success = True
            elif action == "generate_text":
                logger.info("🪄 generating text ...")
                success = True
            else:
                logger.error(f"{action}: action not found.")
                success = False

            metadata["nodes"][node_name] = {
                "success": success,
            }
            if not success:
                break

        if not post_to_object(
            object_name,
            "output",
            metadata,
        ):
            return False

        return success
