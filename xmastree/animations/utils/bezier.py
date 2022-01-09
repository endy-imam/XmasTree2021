from typing import Callable
from numbers import Real, Number

from xmastree.mathutils.utils import clamp


def quadratic_bezier(
        t: Real,
        p0: Number,
        p1: Number,
        p2: Number,
        f: Callable[[Real], Number] = lambda t: t) -> Number:
    """Calculate quadratic bezier.

    Args:
        t (Real): "Time" value clamp to 0 to 1.
        p0 (Number): 0th control point.
        p1 (Number): 1st control point.
        p2 (Number): 2nd control point.
        f (Callable[[Real], Number], optional): Function to modify t for
            speed modification. Defaults to f(t) = t.

    Returns:
        Number: Output value on curve.
    """
    t = f(clamp(t))
    nt = 1 - t
    return nt * nt * p0 + nt * t * p1 + t * t * p2
