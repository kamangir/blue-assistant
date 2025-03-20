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
            "[.|<documents-object-name>]",
            "[-|<faiss-index-object-name>]",
        ],
        "<documents-object-name> -create-index-> <faiss-index-object-name>.",
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
            "[.|<faiss-index-object-name>]",
            "[-|<response-object-name>]",
        ],
        "query on <prompt> using <faiss-index-object-name> -> <response-object-name>.",
        mono=mono,
    )


help_functions = {
    "create_index": help_create_index,
    "query": help_query,
}
