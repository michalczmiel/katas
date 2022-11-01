import unittest

from solution import get_first_illegal_char_and_expected_chars


class Main(unittest.TestCase):
    def test_finding_first_illegal_chars(self) -> None:
        illegal_char, _ = get_first_illegal_char_and_expected_chars(
            "{([(<{}[<>[]}>{[]{[(<()>"
        )
        self.assertEqual(illegal_char, "}")

    def test_finding_expected_chars(self) -> None:
        _, expected_chars = get_first_illegal_char_and_expected_chars(
            "[({(<(())[]>[[{[]{<()<>>"
        )
        sorted_expected_chars = reversed(expected_chars)
        self.assertEqual(list(sorted_expected_chars), list("}}]])})]"))


if __name__ == "__main__":
    unittest.main()
