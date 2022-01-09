from typing import List

from colour import Color

from xmastree.datatypes import Frame
from xmastree.mathutils.utils import complex_magnitude


def nearest_point_coloring(
        point: complex,
        centers: List[complex],
        colors: List[Color]) -> Color:
    """Get color for the nearest region center.

    Args:
        point (complex): Input position.
        centers (List[complex]): Region centers to compare to.
        colors (List[Color]): Color for the given region.

    Returns:
        Color: Associated to the nearest region.
    """
    min_distance, res_color = float("inf"), Color()
    for center, color in zip(centers, colors):
        distance = complex_magnitude(point - center)
        if distance < min_distance:
            min_distance = distance
            res_color = color
    return res_color


def voronoi_coloring(
        points: List[complex],
        centers: List[complex],
        colors: List[Color]) -> Frame:
    """Convert the list of complex points to color output frame.

    Args:
        points (List[complex]): Input "image".
        centers (List[complex]): Region centers to compare to.
        colors (List[Color]): Color for the given region.

    Returns:
        Frame: Output "Image".
    """
    return [nearest_point_coloring(point, centers, colors) for point in points]