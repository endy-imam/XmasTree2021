from typing import List

from math import atan2, pi, sqrt

from colour import Color

from xmastree.datatypes import Frame, Animation
from xmastree.datatypes.vector import Vector

from xmastree.mathutils.utils import clamp, complex_magnitude, remap
from xmastree.transform import convert_vectors_to_complex


def animate(positions: List[Vector]) -> Animation:
    height = max(position.z for position in positions)
    slope = sqrt(height * height + 1)

    complex = convert_vectors_to_complex(positions)
    complex = [c / slope for c in complex]

    FRAME_COUNT = 120
    FRAME_RATE = 60
    
    frames: Animation = []
    for i in range(FRAME_COUNT):
        frame: Frame = []
        for c in complex:
            dist = complex_magnitude(c)
            rev = remap(atan2(c.imag, c.real), -pi, pi)
            r_delta = i / FRAME_COUNT
            angle = clamp(rev + r_delta, cycle=True)
            color = Color(hsl=(angle, dist, dist / 2))
            frame.append(color)
        frames.append(frame)

    return frames