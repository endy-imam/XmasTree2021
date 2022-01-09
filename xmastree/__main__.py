from xmastree.fileio import read_csv, write_frames_to_csv

from xmastree.animations.newton import animate


COORDS_CSV_INPUT_FILE = "./coords_2021.csv"
ANIMATION_CSV_OUTPUT_FILE = "./outputs/res.csv"

if __name__ == "__main__":
    """Reads the input CSV positions and output CSV animation.

    TODO: Maybe make a command program to take file input 
        and output path.
    """
    positions = read_csv(COORDS_CSV_INPUT_FILE)
    output_frames = animate(positions)
    write_frames_to_csv(output_frames, ANIMATION_CSV_OUTPUT_FILE)
