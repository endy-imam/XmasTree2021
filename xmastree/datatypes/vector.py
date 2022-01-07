from typing import NamedTuple
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
    x: Real = 0
    y: Real = 0
    z: Real = 0
