import unittest

from xmastree.mathutils.polynomial import Polynomial


class TestPolynomial(unittest.TestCase):

    def test_define_polynomial(self):
        """Test that defining coefficient by list and optionally var
        """
        f = Polynomial([1, 2j, 3])
        self.assertEqual(f.coeffs, [1, 2j, 3])
        self.assertEqual(f.var, 'x')
        f = Polynomial([1j], var='z')
        self.assertEqual(f.coeffs, [1j])
        self.assertEqual(f.var, 'z')

    def test_compute_polynomial(self):
        """Test that given a polynomial and argument, it computes right
        """
        f = Polynomial([1, 2, 3j])
        self.assertEqual(f(2), 5 + 12j)
        self.assertEqual(f(1j), 1 - 1j)
    
    def test_derive_polynomial(self):
        """Test that a polynomial can return the correct derivative
        """
        # f = (1 + 1jx^2 + 1x^4)
        f = Polynomial([1, 0, 1j, 0, 1])
        # f` = (2jx + 4x^3)
        self.assertEqual(f.d.coeffs, [0, 2j, 0, 4])
        # f`` = (2j + 12x^2)
        self.assertEqual(f.d.d.coeffs, [2j, 0, 12])
        # f``` =  24x
        self.assertEqual(f.d.d.d.coeffs, [0, 24])
    
    def test_polynomial_from_roots_simple(self):
        """Test creating simpler polynomial from roots
        """
        # f = (x - 1); f(1) = 0
        f = Polynomial.from_roots(1)
        self.assertIsInstance(f, Polynomial)
        self.assertEqual(f.coeffs, [-1, 1])
        self.assertEqual(0, f(1))
        # f = (x - 1j); f(1j) = 0
        f = Polynomial.from_roots(1j)
        self.assertEqual(f.coeffs, [-1j, 1])
        self.assertEqual(0, f(1j))
        # f = (x - 1)(x - 2) = x^2 - 3x + 2; f(1) = 0; f(2) = 0
        f = Polynomial.from_roots(1, 2)
        self.assertEqual(f.coeffs, [2, -3, 1])
        self.assertEqual(0, f(1))
        self.assertEqual(0, f(2))

    def test_polynomial_from_roots_complex(self):
        """Test creating more complex polynomial from roots
        """
        roots = [1, 1j, -1, -1j]
        f = Polynomial.from_roots(*roots)
        self.assertIsInstance(f, Polynomial)
        self.assertEqual(f.coeffs, [-1, 0, 0, 0, 1])
        self.assertTrue(all(f(root) == 0 for root in roots))
