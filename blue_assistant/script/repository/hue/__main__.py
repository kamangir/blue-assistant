import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_assistant.script.repository.hue.functions import set_light_color
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="set",
)
parser.add_argument(
    "--color",
    type=str,
)
parser.add_argument(
    "--light",
    type=str,
)
parser.add_argument(
    "--verbose",
    type=int,
    default=0,
    help="0 | 1",
)
args = parser.parse_args()

success = False
if args.task == "task":
    success = set_light_color(
        color=args.color,
        light=args.light,
        verbose=args.verbose == 1,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
