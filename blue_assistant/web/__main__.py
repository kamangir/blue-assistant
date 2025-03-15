import argparse

from blueness import module
from blueness.argparse.generic import sys_exit
from blue_options.logger import log_dict

from blue_assistant import NAME
from blue_assistant.web.crawl import crawl_list_of_urls, fetch_links_and_content
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="crawl | fetch",
)
parser.add_argument(
    "--max_iterations",
    type=int,
    default=10,
)
parser.add_argument(
    "--verbose",
    type=int,
    default=0,
    help="0 | 1",
)
parser.add_argument(
    "--url",
    type=str,
)
parser.add_argument(
    "--seed_urls",
    type=str,
)
parser.add_argument(
    "--object_name",
    type=str,
)
args = parser.parse_args()

success = False
if args.task == "crawl":
    success = True

    output = crawl_list_of_urls(
        seed_urls=args.seed_urls.split("+"),
        object_name=args.object_name,
        max_iterations=args.max_iterations,
    )

    if args.verbose == 1:
        log_dict(logger, output, "url(s)")

elif args.task == "fetch":
    success = True
    links, plain_text = fetch_links_and_content(
        url=args.url,
        verbose=True,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
