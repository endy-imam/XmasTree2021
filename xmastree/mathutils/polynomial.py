from __future__ import annotations

from typing import NamedTuple, Sequence, List
from numbers import Number


class Polynomial(NamedTuple):
    """Representation and function for a polynomial

    Properties:
        coeffs (Sequence[Number]): Sequence of coefficients where c_i
            represents c_i * x^i
        var (str, optional): Variable representation. Defaults to 'x'.
    """

    coeffs: Sequence[Number]
    var: str = 'x'
    
    @property
    def d(self) -> Polynomial:
        """Derivative of the polynomial
        """
        return Polynomial(
            [c * i for i, c in enumerate(self.coeffs[1:], 1)],
            var=self.var
        )

    def __call__(self, x: Number) -> Number:
        """Calculate polynomial with x

        Args:
            x (Number): input value

        Returns:
            Number: output value
        """
        result: Number = 0
        x_exp: Number = 1
        for c in self.coeffs:
            result += c * x_exp
            x_exp *= x
        return result
    
    def __repr__(self) -> str:
        """String representation in Polynomial
        """
        repr: str = '0'
        if self.coeffs:
            nomials: List[str] = []
            for i, n in enumerate(self.coeffs):
                if n == 0:
                    continue
                xn = f'{self.var}^{i}' if i > 1 else self.var if i else ''
                n = n if isinstance(n, complex) or n >= 0 else f'({n})'
                nomials.append(f'{n}{xn}')
            repr = " + ".join(reversed(nomials))
        return f'{self.__class__.__name__}({repr})'
