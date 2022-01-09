from typing import List, Tuple
from numbers import Number, Real

from math import sqrt

from colour import Color

from xmastree.datatypes import Frame, Animation
from xmastree.datatypes.vector import Vector

from xmastree.animations.utils.pointanim import point_cycle_animation

from xmastree.mathutils.utils import complex_magnitude
from xmastree.transform import convert_vectors_to_complex


def animate(positions: List[Vector]) -> Animation:
    height = max(position.z for position in positions)
    slope = sqrt(height * height + 1)

    zs = convert_vectors_to_complex(positions)
    zs = [z / slope for z in zs]

    POINT_SIZE = 0.15
    POINT_RANGE = 1 - POINT_SIZE * 2

    MOVE_TIME = 60
    STAGGER_TIME = 15
    TRANSPOSE_TIME = MOVE_TIME + STAGGER_TIME
    WAIT_TIME = TRANSPOSE_TIME + STAGGER_TIME
    
    FRAME_COUNT = (MOVE_TIME + WAIT_TIME) * 2
    FRAME_RATE = 60
    
    point_funcs: List[Tuple[Real, Number, Color]] = [
        (0, 1, Color('red')),
        (STAGGER_TIME, -1, Color('green')),
        (TRANSPOSE_TIME, 1j, Color('yellow')),
        (WAIT_TIME, -1j, Color('blue')),
    ]
    
    frames: Animation = []
    for i in range(FRAME_COUNT):
        frame: Frame = []
        for c in zs:
            result = Color()
            for d, z, color in point_funcs:
                point = point_cycle_animation(i - d, MOVE_TIME, WAIT_TIME)
                point *= z * POINT_RANGE
                d = complex_magnitude(point - c)
                if d <= POINT_SIZE:
                    result = color
            frame.append(result)
        frames.append(frame)

    return frames
