from typing import NamedTuple, List
from numbers import Real


class Vector(NamedTuple):
    """Representation of 3D vectors and points.

    Properties:
        x (Real, optional): X component of the vector.
            Defaults to 0.0.
        y (Real, optional): Y component of the vector.
            Defaults to 0.0.
        z (Real, optional): Z component of the vector.
            Defaults to 0.0.
    """
    x: Real = 0.0
    y: Real = 0.0
    z: Real = 0.0

class Color(NamedTuple):
    """Representation of RGB colors.

    Properties:
        r (Real, optional): Red component of the color.
            Defaults to 0.0.
        g (Real, optional): Green component of the color.
            Defaults to 0.0.
        b (Real, optional): Blue component of the color.
            Defaults to 0.0.
    """
    r: Real = 0.0
    g: Real = 0.0
    b: Real = 0.0


Frame = List[Color]
Animation = List[Frame]
