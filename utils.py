from math import sqrt
from numbers import Real


def complex_magnitude(z: complex) -> Real:
    """Compute distance from origin of complex number

    Args:
        z (complex): complex number input value.

    Returns:
        float: distance from origin (0+0j)
    """
    return sqrt(z.real * z.real + z.imag * z.imag)


def clamp(val: Real, low: Real=0.0, high: Real=1.0) -> Real:
    """Clamp value into a given inclusive boundary
    
    Args:
        val (Real): [description]
        low (Real, optional): Minimum value. Defaults to 0.0.
        high (Real, optional): Maximum value. Defaults to 1.0.

    Returns:
        Real: clamped value
    """
    return min(max(low, val), high)
