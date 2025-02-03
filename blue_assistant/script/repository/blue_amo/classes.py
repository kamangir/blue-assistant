from blue_objects import file, path
import copy

from blueness import module

from blue_assistant import NAME
from blue_assistant.script.repository.generic.classes import GenericScript
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)


class BlueAmoScript(GenericScript):
    name = path.name(file.path(__file__))

    def __init__(
        self,
        object_name: str,
        verbose: bool = False,
    ):
        super().__init__(
            object_name=object_name,
            verbose=verbose,
        )

        holder_node_name = "generating-the-frames"
        logger.info(
            "{}: expanding {} X {}...".format(
                NAME,
                holder_node_name,
                self.vars["frame_count"],
            )
        )

        holder_node = self.nodes[holder_node_name]
        del self.nodes[holder_node_name]
        self.G.remove_node(holder_node_name)

        for index in range(self.vars["frame_count"]):
            node_name = f"generating-frame-{index+1:03d}"

            self.nodes[node_name] = copy.deepcopy(holder_node)

            self.G.add_node(node_name)
            self.G.add_edge(
                node_name,
                "slicing-into-frames",
            )

        assert self.save_graph()

    def perform_action(
        self,
        node_name: str,
    ) -> bool:
        if not super().perform_action(node_name=node_name):
            return False

        if node_name == "slicing-into-frames":
            logger.info(f"{NAME}: processing the output...")

            list_of_frame_prompts = self.nodes[node_name]["output"].split("---")
            if len(list_of_frame_prompts) != self.vars["frame_count"]:
                logger.warning(
                    "{} != {}, frame count doesn't match, bad AI! 😁".format(
                        len(list_of_frame_prompts),
                        self.vars["frame_count"],
                    )
                )

            list_of_frame_prompts += self.vars["frame_count"] * [""]

            for index in range(self.vars["frame_count"]):
                node_name = f"generating-frame-{index+1:03d}"

                self.nodes[node_name]["prompt"] = self.nodes[node_name][
                    "prompt"
                ].replace(
                    ":::input",
                    list_of_frame_prompts[index],
                )

        return True
