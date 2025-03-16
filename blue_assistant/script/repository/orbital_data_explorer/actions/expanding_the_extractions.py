import copy

from blueness import module

from blue_assistant import NAME
from blue_assistant.script.repository.base.classes import BaseScript
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)


def expanding_the_extractions(
    script: BaseScript,
    node_name: str,
) -> bool:
    map_node_name = "extraction"
    max_nodes = script.nodes[node_name]["max_nodes"]
    logger.info(
        "{}: expanding {} X {}...".format(
            NAME,
            map_node_name,
            max_nodes,
        )
    )

    map_node = script.nodes[map_node_name]
    del script.nodes[map_node_name]
    script.G.remove_node(map_node_name)

    reduce_node_name = "generating_summary"
    for index in range(max_nodes):
        index_node_name = f"{map_node_name}_{index+1:03d}"

        script.nodes[index_node_name] = copy.deepcopy(map_node)

        script.G.add_node(index_node_name)
        script.G.add_edge(
            index_node_name,
            node_name,
        )
        script.G.add_edge(
            reduce_node_name,
            index_node_name,
        )

    script.nodes_changed = True

    return script.save_graph()
