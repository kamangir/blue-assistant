from typing import List
import copy
import numpy as np
import cv2
from tqdm import trange

from blueness import module
from blue_options import string
from blue_objects import file, path, objects

from blue_assistant import NAME
from blue_assistant.script.repository.generic.classes import GenericScript
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)


class BlueAmoScript(GenericScript):
    name = path.name(file.path(__file__))

    def __init__(
        self,
        object_name: str,
        test_mode: bool = False,
        verbose: bool = False,
    ):
        super().__init__(
            object_name=object_name,
            test_mode=test_mode,
            verbose=verbose,
        )

        if self.test_mode:
            self.vars["frame_count"] = 1

        holder_node_name = "generating-the-frames"
        logger.info(
            "{}: expanding {} X {}...".format(
                NAME,
                holder_node_name,
                self.vars["frame_count"],
            )
        )

        holder_node = self.nodes[holder_node_name]
        del self.nodes[holder_node_name]
        self.G.remove_node(holder_node_name)

        reduce_node = "stitching-the-frames"
        self.G.add_node(reduce_node)
        self.nodes[reduce_node] = {"action": "skip"}

        for index in range(self.vars["frame_count"]):
            node_name = f"generating-frame-{index+1:03d}"

            self.nodes[node_name] = copy.deepcopy(holder_node)

            self.G.add_node(node_name)
            self.G.add_edge(
                node_name,
                "slicing-into-frames",
            )
            self.G.add_edge(
                reduce_node,
                node_name,
            )

        assert self.save_graph()

    def perform_action(
        self,
        node_name: str,
    ) -> bool:
        if not super().perform_action(node_name=node_name):
            return False

        if node_name == "slicing-into-frames":
            return self.slice_into_frames(node_name=node_name)

        if node_name == "stitching-the-frames":
            return self.stitch_the_frames(node_name=node_name)

        return True

    def slice_into_frames(
        self,
        node_name: str,
    ) -> bool:
        logger.info(f"{NAME}: processing the output...")

        list_of_frame_prompts = self.nodes[node_name]["output"].split("---")
        if len(list_of_frame_prompts) != self.vars["frame_count"]:
            logger.warning(
                "{} != {}, frame count doesn't match, bad AI! 😁".format(
                    len(list_of_frame_prompts),
                    self.vars["frame_count"],
                )
            )

        list_of_frame_prompts += self.vars["frame_count"] * [""]

        for index in range(self.vars["frame_count"]):
            node_name = f"generating-frame-{index+1:03d}"

            self.nodes[node_name]["prompt"] = self.nodes[node_name]["prompt"].replace(
                ":::input",
                list_of_frame_prompts[index],
            )

        return True

    def stitch_the_frames(
        self,
        node_name: str,
    ) -> bool:
        list_of_frames_filenames: List[str] = [
            filename
            for filename in [
                self.nodes[node_name_].get("filename", "")
                for node_name_ in [
                    f"generating-frame-{index+1:03d}"
                    for index in range(self.vars["frame_count"])
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
                    object_name=self.object_name,
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
                object_name=self.object_name,
            ),
            full_frame,
            log=True,
        )
