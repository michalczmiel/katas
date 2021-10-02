import unittest

from string_calculator import StringCalculator


class StringCalculatorTestCase(unittest.TestCase):
    def test_returns_zero_for_empty_string(self):
        self.assertEqual(StringCalculator().add(""), 0)

    def test_returns_number_if_one_number_is_given(self):
        self.assertEqual(StringCalculator().add("1"), 1)

    def test_returns_sum_if_two_numbers_are_given(self):
        self.assertEqual(StringCalculator().add("1,2"), 3)

    def test_returns_sum_if_multiple_numbers_are_given(self):
        self.assertEqual(StringCalculator().add("1,2,3,4"), 10)


if __name__ == "__main__":
    unittest.main()
