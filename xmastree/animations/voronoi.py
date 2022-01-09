from typing import List, Tuple
from numbers import Number, Real

from math import sqrt

from colour import Color

from xmastree.datatypes import Animation
from xmastree.datatypes.vector import Vector

from xmastree.animations.utils.pointanim import point_cycle_animation

from xmastree.transform import convert_vectors_to_complex
from xmastree.coloring import voronoi_coloring


def animate(positions: List[Vector]) -> Animation:
    height = max(position.z for position in positions)
    slope = sqrt(height * height + 1)

    zs = convert_vectors_to_complex(positions)
    zs = [z / slope for z in zs]

    POINT_SIZE = 0.15
    POINT_RANGE = 1 - POINT_SIZE * 2

    MOVE_TIME = 90
    STAGGER_TIME = 30
    TRANSPOSE_TIME = MOVE_TIME + STAGGER_TIME
    WAIT_TIME = TRANSPOSE_TIME + STAGGER_TIME
    
    FRAME_COUNT = (MOVE_TIME + WAIT_TIME) * 2
    FRAME_RATE = 60
    
    point_args: List[Tuple[Real, Number]] = [
        (0, 1),
        (STAGGER_TIME, -1),
        (TRANSPOSE_TIME, 1j),
        (WAIT_TIME, -1j),
    ]
    colors = list(map(Color, "red green yellow blue".split()))
    
    frames: Animation = []
    for i in range(FRAME_COUNT):
        centers = [
            point_cycle_animation(i - d, MOVE_TIME, WAIT_TIME)
                * z * POINT_RANGE
            for d, z in point_args
        ]

        frame = voronoi_coloring(zs, centers, colors)
        frames.append(frame)

    return frames
