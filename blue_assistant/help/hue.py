from typing import List

from blue_options.terminal import show_usage, xtra

from blue_assistant import env

bridge_args = [
    f"[--bridge_ip <{env.HUE_BRIDGE_IP_ADDRESS}>]",
]


def help_create_user(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@hue",
            "create_user",
            f"[{options}]",
        ]
        + bridge_args,
        "create a hue user.",
        mono=mono,
    )


def help_set(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    args = bridge_args + [
        f"[--username <{env.HUE_BRIDGE_USERNAME}>]",
        "[--light_id <light_id>]",
        "[--hue <65535>]",
        "[--saturation <254>]",
        "[--verbose 1]",
    ]

    return show_usage(
        [
            "@hue",
            "set",
            f"[{options}]",
        ]
        + args,
        "set hue lights.",
        mono=mono,
    )


help_functions = {
    "create_user": help_create_user,
    "set": help_set,
}
