import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_assistant import NAME
from blue_assistant.script.load import load_script
from blue_assistant.script.repository import list_of_script_names
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="list | run",
)
parser.add_argument(
    "--script_name",
    type=str,
    help=" | ".join(list_of_script_names),
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--verbose",
    type=int,
    default=0,
    help="0 | 1",
)
parser.add_argument(
    "--delim",
    type=str,
    default=", ",
)
parser.add_argument(
    "--log",
    type=int,
    default=1,
    help="0 | 1",
)
args = parser.parse_args()

delim = " " if args.delim == "space" else args.delim

success = False
if args.task == "list":
    success = True
    if args.log:
        logger.info(f"{len(list_of_script_names)} script(s)")
        for index, script_name in enumerate(list_of_script_names):
            logger.info(f"#{index + 1: 3d}: {script_name}")
    else:
        print(delim.join(list_of_script_names))
elif args.task == "run":
    success, script = load_script(
        script_name=args.script_name,
        verbose=args.verbose == 1,
    )

    if success:
        success = script.run(object_name=args.object_name)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
