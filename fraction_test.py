import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_innit(self):
        with self.assertRaises(TypeError):
            Fraction("NUMERA", 13)
            Fraction(44, "DENO")
            Fraction(1.2, 0)
            Fraction(2, 4.9)
            Fraction([], 23)
            Fraction("LUV", [])
            Fraction([], [])
            Fraction("WOW", "ISP")

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3, 4), Fraction(1, 12) + Fraction(2, 3))
        self.assertEqual(Fraction(212, 9), Fraction(23) + Fraction(10, 18))
        self.assertEqual(Fraction(9, 2), Fraction(8, 4) + Fraction(5, 2))
        self.assertEqual(Fraction(-22, 7), Fraction(-4) + Fraction(6, 7))
        self.assertEqual(Fraction(-85, 8), Fraction(11, -1) + Fraction(-3, -8))
        self.assertEqual(Fraction(1, 0), Fraction(16, 9) + Fraction(1, 0))
        self.assertEqual(Fraction(-1, 0), Fraction(-1, 0) + Fraction(32, -4))

    def test_mul(self):
        self.assertEqual(Fraction(5, 24), Fraction(10, 12)*Fraction(3, 12))
        self.assertEqual(Fraction(80, 3), Fraction(-2)*Fraction(-40, 3))
        self.assertEqual(Fraction(-30, 7), Fraction(-5, 2)*Fraction(12, 7))
        self.assertEqual(Fraction(1, 0), Fraction(34, 0)*Fraction(3, 5))
        self.assertEqual(Fraction(1, 0), Fraction(8, 0)*Fraction(2, 5))
        self.assertEqual(Fraction(-1, 0), Fraction(-10, -4)*Fraction(6, 0))

    def test_sub(self):
        self.assertEqual(Fraction(3, 5), Fraction(8, 4) - Fraction(7, 5))
        self.assertEqual(Fraction(1, 3), Fraction(10, 15) - Fraction(6, 18))
        self.assertEqual(Fraction(38, 3), Fraction(14) - Fraction(4, 3))
        self.assertEqual(Fraction(-71, 52), Fraction(5, 13) - Fraction(14, 8))
        self.assertEqual(Fraction(-75), Fraction(-50) - Fraction(25))
        self.assertEqual(Fraction(21, 4), Fraction(100, 400) - Fraction(-5))
        self.assertEqual(Fraction(1, 0), Fraction(4, 15) - Fraction(1, 0))
        self.assertEqual(Fraction(-1, 0), Fraction(-1, 0) - Fraction(-24, 124))

    def test_eq(self):
        f = Fraction(1, 2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))

        f = Fraction(5, 6)
        g = Fraction(150, 180)
        h = Fraction(15000, 300)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))

        f = Fraction(128, 0)
        g = Fraction(1, 0)
        h = Fraction(0)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))

        f = Fraction(-19, 0)
        g = Fraction(-1, 0)
        h = Fraction(-19)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))

        f = Fraction(-2, 18)
        g = Fraction(14, -126)
        h = Fraction(6, 54)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))

if __name__ == '__main__':
     unittest.main(verbosity=2)



