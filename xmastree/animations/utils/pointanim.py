from numbers import Real

from math import cos, pi

from xmastree.animations.utils.bezier import quadratic_bezier


def point_animation(t: Real) -> complex:
    """Animated curving point on t.

    Args:
        t (Real): "Time" value.

    Returns:
        complex: Output point on curve.
    """
    f = lambda t: (cos(pi * (t + 1)) + 1) / 2
    return quadratic_bezier(t, 1, 1.5j, -1, f=f)


def point_cycle_animation(
        t: Real,
        move_t: Real = 1,
        wait_t: Real = 0.5) -> complex:
    """Animating cycled curving point on t.

    Args:
        t (Real): "Time" value.
        move_t (Real, optional): Movement time. Defaults to 1.
        wait_t (Real, optional): Waiting time. Defaults to 0.5.

    Returns:
        complex: Output point on curve.
    """
    dur_t = move_t + wait_t
    r, t = divmod(t % (2 * dur_t), dur_t)
    return point_animation(t / move_t) * (1 - 2 * r)
