from typing import List

from blue_options.terminal import show_usage, xtra


def help_create_index(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~download,dryrun,~upload", mono=mono)

    return show_usage(
        [
            "@RAG",
            "create_index",
            f"[{options}]",
            "[.|<docs-object-name>]",
            "[-|<index-object-name>]",
        ],
        "<docs-object-name> -create-index-> <faiss-index-object-name>.",
        mono=mono,
    )


def help_query(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~download,dryrun,~upload", mono=mono)

    return show_usage(
        [
            "@RAG",
            "query",
            f"[{options}]",
            "<prompt>",
            "[.|<index-object-name>]",
            "[-|<response-object-name>]",
        ],
        "query on <prompt> using <index-object-name> -> <response-object-name>.",
        mono=mono,
    )


help_functions = {
    "create_index": help_create_index,
    "query": help_query,
}
