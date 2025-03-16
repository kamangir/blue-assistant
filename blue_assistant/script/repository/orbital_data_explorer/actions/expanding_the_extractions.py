import copy
from typing import Dict

from blueness import module
from blue_options.logger import log_dict, log_list
from blue_objects.metadata import get_from_object

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

    crawl_cache: Dict[str, str] = get_from_object(
        script.object_name,
        "web_crawl_cache",
        {},
    )
    log_dict(logger, "using", crawl_cache, "crawled url(s)")

    list_of_urls = [
        url for url, content_type in crawl_cache.items() if "html" in content_type
    ]
    log_list(logger, "using", list_of_urls, "crawled html(s)")

    # import ipdb

    # ipdb.set_trace()

    map_node = script.nodes[map_node_name]
    del script.nodes[map_node_name]
    script.G.remove_node(map_node_name)

    reduce_node_name = "generating_summary"
    for index in range(max_nodes):
        index_node_name = f"{map_node_name}_{index+1:03d}"

        script.nodes[index_node_name] = copy.deepcopy(map_node)

        script.nodes[index_node_name]["prompt"] = map_node["prompt"].replace(
            ":::page_content",
            "wip",
        )

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
