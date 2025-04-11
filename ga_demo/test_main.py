# test_calculator.py
import unittest

from main import add, divide, multiply, subtract


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(-3, -4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(10, 5), 2)
        self.assertAlmostEqual(divide(1, 3), 0.3333333333333333)
        with self.assertRaises(ValueError):
            divide(10, 0)

    # This test will fail deliberately for demonstration
    def test_failing(self):
        self.assertEqual(add(2, 2), 5, "This test is deliberately set to fail")


if __name__ == "__main__":
    unittest.main()
