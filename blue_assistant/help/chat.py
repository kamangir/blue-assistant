from typing import List

from blue_options.terminal import show_usage, xtra


def help_chat(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~download,dryrun,~interact,~upload", mono=mono)

    chat_options = xtra("~interact", mono=mono)

    return show_usage(
        [
            "@assistant",
            "chat",
            f"[{options}]",
            f"[{chat_options}]",
            "[-|<object-name>]",
        ],
        "chat with @assistant.",
        mono=mono,
    )
