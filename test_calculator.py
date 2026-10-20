import unittest

from calculator import add, divide, multiply, subtract


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(subtract(7, 4), 3)

    def test_multiplication(self):
        self.assertEqual(multiply(6, 5), 30)

    def test_division(self):
        self.assertEqual(divide(8, 2), 4)

    def test_decimal_values(self):
        self.assertAlmostEqual(add(1.5, 2.25), 3.75)
        self.assertAlmostEqual(divide(7.5, 2.5), 3)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()
