from typing import List
from openai import OpenAI
import pprint

from blueness import module
from openai_commands.env import OPENAI_API_KEY

from blue_assistant import NAME
from blue_assistant.script.repository.base.classes import BaseScript
from blue_assistant.env import (
    BLUE_ASSISTANT_TEXT_DEFAULT_MODEL,
    BLUE_ASSISTANT_TEXT_MAX_TOKEN,
)
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)


# https://platform.openai.com/docs/guides/text-generation
def generate_text(
    script: BaseScript,
    node_name: str,
) -> bool:
    if not OPENAI_API_KEY:
        logger.error("OPENAI_API_KEY is not set.")
        return False

    logger.info(f"{NAME}: {script} @ {node_name} ...")

    messages: List = []
    list_of_context_nodes = script.get_context(node_name)
    logger.info("node context: {}".format(" <- ".join(list_of_context_nodes)))
    for context_node in reversed(list_of_context_nodes):
        messages += [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": script.apply_vars(script.nodes[context_node]["prompt"]),
                    }
                ],
            }
        ]

        if script.nodes[context_node].get("completed", False):
            messages += [
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": script.nodes[context_node]["output"],
                        }
                    ],
                }
            ]

    if script.verbose:
        logger.info(f"messages: {pprint.pformat(messages)}")

    client = OpenAI(api_key=OPENAI_API_KEY)

    try:
        response = client.chat.completions.create(
            messages=messages,
            model=BLUE_ASSISTANT_TEXT_DEFAULT_MODEL,
            max_tokens=BLUE_ASSISTANT_TEXT_MAX_TOKEN,
        )
    except Exception as e:
        logger.error(str(e))
        return False

    if script.verbose:
        logger.info("response: {}".format(response))

    if not response.choices:
        logger.error("no choice.")
        return False

    output = response.choices[0].message.content
    logger.info(f"🗣️ output: {output}")
    script.nodes[node_name]["output"] = output

    return True
