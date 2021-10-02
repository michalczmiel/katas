import unittest

from string_calculator import StringCalculator


class StringCalculatorTestCase(unittest.TestCase):
    def test_returns_zero_for_empty_string(self):
        self.assertEqual(StringCalculator().add(""), 0)


if __name__ == "__main__":
    unittest.main()
