from math import sqrt

from datatypes import Color, Frame, Animation

from fileio import read_csv, write_frames_to_csv
from transform import convert_vectors_to_complex


COORDS_CSV_INPUT_FILE = "./coords_2021.csv"

if __name__ == "__main__":
    positions = read_csv(COORDS_CSV_INPUT_FILE)
    mapped_complex_values = convert_vectors_to_complex(positions)
    height = max(position.z for position in positions)
    slope = sqrt(height * height + 1)
    output_colors: Frame = [
        Color((x + 1) / 2, (y + 1) / 2, z / height)
        for x, y, z in positions
    ]
    output_frames: Animation = [output_colors]
    write_frames_to_csv(output_frames)
