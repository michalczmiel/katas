import re
from typing import Iterable, List, Tuple


class StringCalculator:
    def __init__(self) -> None:
        self._default_delimiters: Tuple[str] = (",", "\n")
        self._max_big_number: int = 1000
        self._delimiter_change_chars: str = "//"

    def _has_single_char_delimiter(self, delimiter_part: str) -> bool:
        return len(self._delimiter_change_chars) + 1 == len(delimiter_part)

    def _parse_raw_numbers(self, raw_numbers: str) -> Tuple[str, List[str]]:
        if not raw_numbers.startswith(self._delimiter_change_chars):
            return raw_numbers, []

        delimiter_part, numbers_part = raw_numbers.split("\n")

        if self._has_single_char_delimiter(delimiter_part):
            custom_delimiter = delimiter_part[len(self._delimiter_change_chars) :]
            return numbers_part, [custom_delimiter]

        custom_delimiters = re.findall(r"\[(.*?)\]", delimiter_part)
        return numbers_part, custom_delimiters

    def _assert_no_negative_numbers(self, numbers: Iterable[int]) -> None:
        negative_numbers = [str(number) for number in numbers if number < 0]
        if not negative_numbers:
            return
        elif len(negative_numbers) == 1:
            raise Exception("negatives not allowed")
        raise Exception(
            f"negatives not allowed, but found {', '.join(negative_numbers)}"
        )

    def _ignore_big_numbers(self, numbers: List[int]) -> List[int]:
        return [number for number in numbers if number <= self._max_big_number]

    def _split_numbers(
        self, raw_numbers: str, custom_delimiters: List[str]
    ) -> List[int]:
        numbers = raw_numbers
        for custom_delimiter in custom_delimiters:
            numbers = numbers.replace(custom_delimiter, self._default_delimiters[0])
        delimiters = "|".join(self._default_delimiters)
        numbers = re.split(delimiters, numbers)
        numbers = [int(number) for number in numbers]
        return numbers

    def add(self, raw_numbers: str) -> int:
        if not raw_numbers:
            return 0

        numbers, custom_delimiters = self._parse_raw_numbers(raw_numbers)
        numbers = self._split_numbers(numbers, custom_delimiters)

        self._assert_no_negative_numbers(numbers)
        numbers = self._ignore_big_numbers(numbers)

        return sum(numbers)