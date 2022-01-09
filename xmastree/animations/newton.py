from typing import List, Tuple
from numbers import Number, Real

from math import sqrt

from colour import Color

from xmastree.datatypes import Animation
from xmastree.datatypes.vector import Vector
from xmastree.mathutils.polynomial import Polynomial

from xmastree.animations.utils.pointanim import point_cycle_animation

from xmastree.transform import convert_vectors_to_complex
from xmastree.coloring import voronoi_coloring


def animate(positions: List[Vector]) -> Animation:
    height = max(position.z for position in positions)
    slope = sqrt(height * height + 1)

    zs = convert_vectors_to_complex(positions)
    zs = [z / slope for z in zs]

    NEWTON_ITER_COUNT = 5

    POINT_RANGE = 1

    FRAME_RATE = 60

    MOVE_TIME = FRAME_RATE * 3
    STAGGER_TIME = 0
    HALT_TIME = FRAME_RATE * 1
    TRANSPOSE_TIME = MOVE_TIME + STAGGER_TIME
    WAIT_TIME = TRANSPOSE_TIME + STAGGER_TIME

    CYCLE_TIME = (MOVE_TIME + WAIT_TIME + HALT_TIME) * 2

    FRAME_COUNT = CYCLE_TIME
    
    point_args: List[Tuple[Real, Number]] = [
        (0, 1),
        (STAGGER_TIME, -1),
        (TRANSPOSE_TIME, 1j),
        (WAIT_TIME, -1j),
    ]
    colors = list(map(Color, "#A91F03 #FDB850 #2D5052 #51BCE2".split()))
    
    frames: Animation = []
    for i in range(FRAME_COUNT):
        centers = [
            point_cycle_animation(i - d, MOVE_TIME, WAIT_TIME + HALT_TIME)
                * z * POINT_RANGE
            for d, z in point_args
        ]

        f = Polynomial.from_roots(*centers)
        df = f.d
        
        newton_z: List[complex] = []
        for z in zs:
            for _ in range(NEWTON_ITER_COUNT):
                z -= f(z) / df(z)
            newton_z.append(z)

        frame = voronoi_coloring(newton_z, centers, colors)
        frames.append(frame)

    return frames
