
import unittest

from src.calculator import add, divide


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_add_negative(self):
        self.assertEqual(add(-2, 3), 1)

if __name__ == "__main__":
    unittest.main()

