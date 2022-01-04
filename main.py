from csv import reader
from typing import List

from collections import namedtuple
from math import sqrt, atan, atan2, cos, sin


Vector = namedtuple('Vector', 'x, y, z')


def read_csv(path: str) -> List[Vector]:
    """Inputs a file from path to a list of coordinates

    Args:
        path (str): path to csv file

    Returns:
        List[Vector]: list of coordinates
    """
    positions = []
    with open(path) as file:
        for line in reader(file):
            x, y, z = map(float, line)
            positions.append(Vector(x, y, z))
    return positions


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
    complex_list = []
    for position in positions:
        x, y, z = position
        radius = sqrt(x * x + y * y)
        depth = height - z
        angle = atan2(y, x)
        magnitude = depth * depth_weight + radius * radius_weight
        result = magnitude * (cos(angle) + 1j * sin(angle))
        complex_list.append(result)
    return complex_list


COORDS_CSV_INPUT_FILE = "./coords_2021.csv"

if __name__ == "__main__":
    input_coordinates = read_csv(COORDS_CSV_INPUT_FILE)
    mapped_complex_values = convert_vectors_to_complex(input_coordinates)
