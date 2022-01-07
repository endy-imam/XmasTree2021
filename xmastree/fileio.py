from typing import List

from csv import reader

from .datatypes import Animation
from .datatypes.vector import Vector


def read_csv(path: str) -> List[Vector]:
    """Inputs a file from path to a list of coordinates

    Args:
        path (str): path to csv file

    Returns:
        List[Vector]: list of coordinates
    """
    positions: List[Vector] = []
    with open(path) as file:
        for line in reader(file):
            x, y, z = map(float, line)
            positions.append(Vector(x, y, z))
    return positions


def write_frames_to_csv(frames: Animation, path: str) -> None:
    """Output frames into csv file.

    Args:
        frames (Animation): Input frames.
        path (str): Path for output csv file.
    """
    count = len(frames[0])
    header = ['FRAME_ID'] + [f'{C}_{i}' for i in range(count) for C in 'RGB']

    lines = [header]
    for i, frame in enumerate(frames):
        line = [i] + [int(c * 255) for rgb in frame for c in rgb.rgb]
        lines.append([str(val) for val in line])

    with open(path, 'w') as file:
        file.write('\n'.join(','.join(line) for line in lines))
