from typing import List
import numpy as np
import cv2
from tqdm import trange

from blueness import module
from blue_objects import file, objects
from blue_options import string

from blue_assistant import NAME
from blue_assistant.script.repository.base.classes import BaseScript
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)


def stitch_the_frames(
    script: BaseScript,
    node_name: str,
) -> bool:
    list_of_frames_filenames: List[str] = [
        filename
        for filename in [
            script.nodes[node_name_].get("filename", "")
            for node_name_ in [
                f"generating-frame-{index+1:03d}"
                for index in range(script.vars["frame_count"])
            ]
        ]
        if filename
    ]
    if not list_of_frames_filenames:
        return True

    logger.info(
        "{} frames to stitch: {}".format(
            len(list_of_frames_filenames),
            ", ".join(list_of_frames_filenames),
        )
    )

    list_of_frames: List[np.ndarray] = []
    for filename in list_of_frames_filenames:
        success, frame = file.load_image(
            objects.path_of(
                filename=filename,
                object_name=script.object_name,
            )
        )

        if success:
            list_of_frames += [frame]

    if not list_of_frames:
        return True

    common_height = list_of_frames[0].shape[0]
    for index in trange(len(list_of_frames)):
        if list_of_frames[index].shape[0] != common_height:
            aspect_ratio = (
                list_of_frames[index].shape[1] / list_of_frames[index].shape[0]
            )
            new_width = int(common_height * aspect_ratio)

            list_of_frames[index] = cv2.resize(
                list_of_frames[index],
                (new_width, common_height),
                interpolation=cv2.INTER_AREA,
            )

    full_frame = np.concatenate(list_of_frames, axis=1)
    logger.info(f"full_frame: {string.pretty_shape_of_matrix(full_frame)}")

    return file.save_image(
        objects.path_of(
            filename=f"{node_name}.png",
            object_name=script.object_name,
        ),
        full_frame,
        log=True,
    )
