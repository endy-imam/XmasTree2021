from typing import List

from math import sqrt, atan, atan2, cos, sin

from .datatypes import Vector


def convert_vectors_to_complex(positions: List[Vector]) -> List[complex]:
    """Convert list of positions on tree to mapped complex point on cone

    Args:
        positions (List[Vector]): List of positions on tree

    Returns:
        List[complex]: List of complex points on cone
    """
    height = max(position.z for position in positions)
    rad_from_tip = atan(1 / height)
    depth_weight = cos(rad_from_tip)
    radius_weight = sin(rad_from_tip)
    complex_list: List[complex] = []
    for position in positions:
        x, y, z = position
        radius = sqrt(x * x + y * y)
        depth = height - z
        angle = atan2(y, x)
        magnitude = depth * depth_weight + radius * radius_weight
        result = magnitude * (cos(angle) + 1j * sin(angle))
        complex_list.append(result)
    return complex_list