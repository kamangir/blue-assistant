from typing import Dict, Tuple, List
from openai import OpenAI
import pprint

from blueness import module
from blue_objects import file
from openai_commands.env import OPENAI_API_KEY

from blue_assistant import NAME
from blue_assistant.env import (
    BLUE_ASSISTANT_TEXT_DEFAULT_MODEL,
    BLUE_ASSISTANT_TEXT_MAX_TOKEN,
)
from blue_assistant.script.actions.generic import GenericAction
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)


class GenerateTextAction(GenericAction):
    name = file.name(__file__)

    # https://platform.openai.com/docs/guides/text-generation
    def perform(
        self,
        node_name: str,
    ) -> bool:
        if not OPENAI_API_KEY:
            logger.error("OPENAI_API_KEY is not set.")
            return False

        if not super().perform(node_name=node_name):
            return False

        messages: List = []
        list_of_context_nodes = self.script.get_history(node_name)
        logger.info("node context: {}".format(" <- ".join(list_of_context_nodes)))
        for context_node in reversed(list_of_context_nodes):
            messages += [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": self.script.apply_vars(
                                self.script.nodes[context_node]["prompt"]
                            ),
                        }
                    ],
                }
            ]

            if self.script.nodes[context_node].get("completed", False):
                messages += [
                    {
                        "role": "assistant",
                        "content": [
                            {
                                "type": "text",
                                "text": self.script.nodes[context_node]["output"],
                            }
                        ],
                    }
                ]

        if self.script.verbose:
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

        if self.script.verbose:
            logger.info("response: {}".format(response))

        if not response.choices:
            logger.error("no choice.")
            return False

        output = response.choices[0].message.content
        logger.info(f"🗣️ output: {output}")

        self.script.nodes[node_name]["output"] = output

        var_name = self.script.nodes[node_name].get("output", "")
        if var_name:
            self.script.vars[var_name] = output

        return True
