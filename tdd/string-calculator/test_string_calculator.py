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

    def test_returns_sum_if_delimiter_is_also_new_line(self):
        self.assertEqual(StringCalculator().add("1\n2,3"), 6)

    def test_returns_sum_if_delimiter_is_changed(self):
        self.assertEqual(StringCalculator().add("//;\n1;2"), 3)

    def test_throws_error_when_negative_number_is_given(self):
        with self.assertRaises(Exception) as context:
            StringCalculator().add("//;\n1;-2")
        self.assertEqual("negatives not allowed", str(context.exception))

    def test_throws_error_when_multiple_negative_numbers_is_given(self):
        with self.assertRaises(Exception) as context:
            StringCalculator().add("//;\n-1;-2")
        self.assertEqual("negatives not allowed, but found -1, -2", str(context.exception))


if __name__ == "__main__":
    unittest.main()
