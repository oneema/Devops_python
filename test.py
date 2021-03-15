import unittest
from python_calculator import add, subtract, divide, multiply

class TestFactorial(unittest.TestCase):
    """
    Our basic test class
    """

    def test_add(self):
        res = add(5,5)
        self.assertEqual(res, 10)
    
    def test_subtract(self):
        res = subtract(5,5)
        self.assertEqual(res, 0)

    def test_multiply(self):
        res = multiply(5,5)
        self.assertEqual(res, 25)

    def test_divide(self):
        res = divide(5,5)
        self.assertEqual(res, 1)

if __name__ == '__main__':
    unittest.main()
