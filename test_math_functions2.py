import unittest
import math_functions

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(math_functions.add(5, 4), 9)
        
    def test_multiply(self):
        self.assertEqual(math_functions.multiply(3, 4), 12)

    def test_power(self):
        self.assertEqual(math_functions.power(2, 8), 256)

if __name__ == '__main__':
    unittest.main()
