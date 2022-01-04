from csv import reader
from typing import List

from collections import namedtuple


Vector = namedtuple('Vector', 'x, y, z')


def read_csv(path: str) -> List[Vector]:
    """Inputs a file from path to a list of coordinates"""
    vector_list = []
    with open(path) as file:
        for line in reader(file):
            x, y, z = map(float, line)
            vector_list.append(Vector(x, y, z))
    return vector_list


COORDS_CSV_INPUT_FILE = "./coords_2021.csv"

if __name__ == "__main__":
    input_coordinates = read_csv(COORDS_CSV_INPUT_FILE)
    print("\n".join(map(repr, input_coordinates)))
