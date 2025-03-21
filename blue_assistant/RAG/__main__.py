import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_assistant import NAME
from blue_assistant.RAG.query_pdf import query_pdf
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="query_pdf",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--filename",
    type=str,
    default="document.pdf",
)
parser.add_argument(
    "--encoded_question",
    type=str,
    default="",
)
parser.add_argument(
    "--verbose",
    type=int,
    default=0,
    help="0 | 1",
)
args = parser.parse_args()

success = False
if args.task == "query_pdf":
    success, _ = query_pdf(
        object_name=args.object_name,
        filename=args.filename,
        question=args.encoded_question.replace("__", " "),
        verbose=args.verbose == 1,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
