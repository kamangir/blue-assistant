from typing import Dict, Callable

from blue_assistant.script.repository.base.classes import BaseScript
from blue_assistant.script.repository.blue_amo.actions import (
    slice_into_frames,
    stitch_the_frames,
)


dict_of_actions: Dict[str, Callable[[BaseScript, str], bool]] = {
    "slice_into_frames": slice_into_frames.slice_into_frames,
    "stitch_the_frames": stitch_the_frames.stitch_the_frames,
}
