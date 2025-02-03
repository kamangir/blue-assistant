from typing import Dict, List
import os
from tqdm import tqdm


from blueness import module
from blue_objects import file, path
from blue_objects.metadata import post_to_object

from blue_assistant import NAME
from blue_assistant.script.repository.base.classes import BaseScript
from blue_assistant.script.actions.functions import perform_action
from blue_assistant.logger import logger


NAME = module.name(__file__, NAME)


class GenericScript(BaseScript):
    name = path.name(file.path(__file__))

    def run(
        self,
        object_name: str,
    ) -> bool:
        if not super().run(object_name=object_name):
            return False

        metadata: Dict[Dict] = {"nodes": {}}
        success: bool = True
        for node_name, node in tqdm(self.nodes.items()):
            logger.info(
                "{}{}".format(
                    node_name,
                    f": {node}" if self.verbose else " ...",
                )
            )

            assert isinstance(node, dict)
            success, output = perform_action(
                action_name=node.get("action", "unknown"),
                script=self,
                node_name=node_name,
            )
            metadata["nodes"][node_name] = {
                "success": success,
                "output": output,
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
