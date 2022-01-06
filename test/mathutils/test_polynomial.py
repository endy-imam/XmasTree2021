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
        f = Polynomial([1, 0, 1j, 0, 1])
        self.assertEqual(f.d.coeffs, [0, 2j, 0, 4])
        self.assertEqual(f.d.d.coeffs, [2j, 0, 12])
        self.assertEqual(f.d.d.d.coeffs, [0, 24])
        

if __name__ == '__main__':
    unittest.main()
