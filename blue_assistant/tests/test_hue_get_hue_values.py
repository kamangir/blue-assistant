import pytest
import cv2

from blue_assistant.script.repository.hue.colors import get_hue_values


@pytest.mark.parametrize(
    ["colormap"],
    [
        [cv2.COLORMAP_HOT],
    ],
)
@pytest.mark.parametrize(
    ["length"],
    [
        [10],
        [100],
    ],
)
def test_hue_get_hue_values(
    colormap: int,
    length: int,
):
    list_of_hue_values = get_hue_values(
        colormap=colormap,
        length=length,
    )

    assert len(list_of_hue_values) == length
