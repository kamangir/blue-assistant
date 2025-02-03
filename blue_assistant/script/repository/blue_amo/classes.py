from blue_objects import file, path
import copy

from blue_assistant.script.repository.generic.classes import GenericScript
from blue_assistant.logger import logger


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
