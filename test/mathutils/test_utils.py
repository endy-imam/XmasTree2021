import unittest

from math import pi

from xmastree.mathutils.utils import clamp, complex_polar, complex_magnitude, remap


def close_enough_complex(expect, actual, epsilon=1e-8):
    return complex_magnitude(actual - expect) < epsilon


class TestMathUtils(unittest.TestCase):

    def test_complex_polar(self):
        """Test convert from polar to complex
        """
        h_pi = pi / 2 # HALF PI
        self.assertTrue(close_enough_complex(complex_polar(1, 0), 1))
        self.assertTrue(close_enough_complex(complex_polar(1, pi), -1))
        self.assertTrue(close_enough_complex(complex_polar(1, h_pi), 1j))
        self.assertTrue(close_enough_complex(complex_polar(1, -h_pi), -1j))
        
        q_pi = pi / 4 # QUARTER PI
        sqrt2 = 2 ** -0.5
        actual, expect = complex_polar(1, q_pi), complex(sqrt2, sqrt2)
        self.assertTrue(close_enough_complex(expect, actual))
    
    def test_clamp(self):
        """Test clamping function
        """
        self.assertEqual(clamp(-0.5), 0.0)
        self.assertEqual(clamp( 0.0), 0.0)
        self.assertEqual(clamp( 0.5), 0.5)
        self.assertEqual(clamp( 1.0), 1.0)
        self.assertEqual(clamp( 1.5), 1.0)
        self.assertEqual(clamp( 0.0, lo=0.5), 0.5)
        self.assertEqual(clamp( 1.0, hi=0.5), 0.5)

    def test_remap(self):
        """Test remapping function
        """
        self.assertEqual(remap(0, -1, 1), 0.5)
        self.assertEqual(remap(-0.5, 0, 1, cycle=True), 0.5)
        self.assertEqual(remap(-0.5, 0, 1, lo1=0, hi1=2, cycle=True), 1)
