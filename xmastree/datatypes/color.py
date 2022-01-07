from typing import NamedTuple
from numbers import Real


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
