from csv import reader
from typing import List

from collections import namedtuple
from math import sqrt, atan, atan2, cos, sin


Vector = namedtuple('Vector', 'x, y, z')
Color = namedtuple('Color', 'r, g, b')


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


def clamp(val, low=0, high=1):
    return low if val < low else high if val > high else val


def write_frames_to_csv(
        frames: List[List[Color]],
        path: str='./outputs/res.csv') -> None:
    """Output frames into csv file.

    Args:
        frames (List[List[Color]]): Input frames.
        path (str, optional): Path for output csv file.
            Defaults to './outputs/res.csv'.
    """
    count = len(frames[0])
    header = ['FRAME_ID'] + [f'{C}_{i}' for i in range(count) for C in 'RGB']

    lines = [header]
    for i, frame in enumerate(frames):
        line = [i] + [int(clamp(c) * 255) for rgb in frame for c in rgb]
        lines.append([str(val) for val in line])

    with open(path, 'w') as file:
        file.write('\n'.join(','.join(line) for line in lines))


COORDS_CSV_INPUT_FILE = "./coords_2021.csv"

if __name__ == "__main__":
    positions = read_csv(COORDS_CSV_INPUT_FILE)
    mapped_complex_values = convert_vectors_to_complex(positions)
    height = max(position.z for position in positions)
    slope = sqrt(height * height + 1)
    output_colors = [
        Color((x + 1) / 2, (y + 1) / 2, z / height)
        for x, y, z in positions
    ]
    output_frames = [output_colors]
    write_frames_to_csv(output_frames)
