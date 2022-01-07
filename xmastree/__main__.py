from xmastree.fileio import read_csv, write_frames_to_csv

from xmastree.animations.rainbow import animate


COORDS_CSV_INPUT_FILE = "./coords_2021.csv"
ANIMATION_CSV_OUTPUT_FILE = "./outputs/rainbow.csv"

if __name__ == "__main__":
    """Reads the GIFT file (input CSV) and output animation (output CSV)

    TODO: Maybe make a command program to take file input 
        and output path
    """
    positions = read_csv(COORDS_CSV_INPUT_FILE)
    output_frames = animate(positions)
    write_frames_to_csv(output_frames, ANIMATION_CSV_OUTPUT_FILE)
