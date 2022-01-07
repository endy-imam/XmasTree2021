from math import sqrt, sin, cos
from numbers import Real


def complex_magnitude(z: complex) -> Real:
    """Compute distance from origin of complex number.

    Args:
        z (complex): complex number input value.

    Returns:
        float: distance from origin (0+0j).
    """
    return sqrt(z.real * z.real + z.imag * z.imag)


def complex_polar(mag: Real, rad: Real) -> complex:
    """Create complex number from polar notation.

    Args:
        mag (Real): Magnitude component.
        rad (Real): Radian component.

    Returns:
        complex: Complex number for polar notation.
    """
    return mag * complex(cos(rad), sin(rad))


def clamp(val: Real, lo: Real = 0, hi: Real = 1, cycle: bool = False) -> Real:
    """Clamp value into a given inclusive boundary.
    
    Args:
        val (Real): input value.
        lo (Real, optional): Lower bound. Defaults to 0.
        hi (Real, optional): Upper bound. Defaults to 1.
        cycle (bool, optional): Allows modulus cycle for range.
            Defaults to False.

    Returns:
        Real: clamped value.
    """
    range = hi - lo
    t0 = (val - lo) / range
    t1 = t0 % 1 if cycle else max(0, min(1, t0))
    return lo + range * t1

def remap(
        val: Real, lo0: Real, hi0: Real, lo1: Real = 0, hi1: Real = 1,
        cycle: bool = False) -> Real:
    """Remap/Clamp values from one range to another.

    Args:
        val (Real): Input value.
        lo0 (Real): Lower input bound.
        hi0 (Real): Upper input bound.
        lo1 (Real, optional): Lower output bound. Defaults to 0.
        hi1 (Real, optional): Upper output bound. Defaults to 1.
        cycle (bool, optional): Allows modulus cycle for original range.
            Defaults to False.

    Returns:
        Real: Output value.
    """
    range0 = hi0 - lo0
    range1 = hi1 - lo1
    t0 = (val - lo0) / range0
    t1 = t0 % 1 if cycle else max(0, min(1, t0))
    return lo1 + range1 * t1
