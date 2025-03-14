from typing import List

from blue_options.terminal import show_usage, xtra

from blue_assistant import env


def help_create_user(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    args = [
        f"[--bridge_ip <{env.HUE_BRIDGE_IP_ADDRESS}>]",
    ]

    return show_usage(
        [
            "@hue",
            "create_user",
            f"[{options}]",
        ]
        + args,
        "create a hue user.",
        mono=mono,
    )


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    args = [
        f"[--bridge_ip <{env.HUE_BRIDGE_IP_ADDRESS}>]",
        f"[--username <{env.HUE_BRIDGE_USERNAME}>]",
        "[--verbose 1]",
    ]

    return show_usage(
        [
            "@hue",
            "list",
            f"[{options}]",
        ]
        + args,
        "list hue lights.",
        mono=mono,
    )


def help_set(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    args = [
        f"[--bridge_ip <{env.HUE_BRIDGE_IP_ADDRESS}>]",
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


def help_test(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    args = [
        f"[--bridge_ip <{env.HUE_BRIDGE_IP_ADDRESS}>]",
        f"[--username <{env.HUE_BRIDGE_USERNAME}>]",
        "[--light_id <light_id>]",
        "[--hue <65535>]",
        "[--verbose 1]",
    ]

    return show_usage(
        [
            "@hue",
            "hue",
            f"[{options}]",
            "[-|<object-name>]",
        ]
        + args,
        "test hue.",
        mono=mono,
    )


help_functions = {
    "create_user": help_create_user,
    "list": help_list,
    "set": help_set,
    "test": help_test,
}
