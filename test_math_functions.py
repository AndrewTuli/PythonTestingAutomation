import unittest

from math_functions import add, multiply, power


class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 4), 9)
        self.assertEqual(add(5, 5), 10)
        self.assertEqual(3, add(2, 1))
        self.assertEqual(-1, add(2, -3))

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_power(self):
        self.assertEqual(power(2, 8), 256)


if __name__ == "__main__":
    unittest.main()
