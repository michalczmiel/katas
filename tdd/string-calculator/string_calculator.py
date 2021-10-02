import re
from typing import Iterable, List, Optional, Tuple


class StringCalculator:
    def __init__(self) -> None:
        self._default_delimiters: Tuple[str] = (",", "\n")
        self._max_big_number: int = 1000

    def _parse_raw_numbers(self, numbers: str) -> Tuple[str, Optional[str]]:
        if not numbers.startswith("//"):
            return numbers, None
        delimiter_part, numbers_part = numbers.split("\n")

        if "[" not in delimiter_part and "]" not in delimiter_part:
            custom_delimiter = delimiter_part[2:]
            return numbers_part, custom_delimiter

        found_delimiter = re.findall(r"\[(.*?)\]", delimiter_part)
        custom_delimiter = found_delimiter[0]
        return numbers_part, custom_delimiter

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
        self, raw_numbers: str, custom_delimiter: Optional[str]
    ) -> List[int]:
        numbers = raw_numbers
        delimiters = "|".join(self._default_delimiters)
        if custom_delimiter:
            numbers = numbers.replace(custom_delimiter, self._default_delimiters[0])
        numbers = re.split(delimiters, numbers)
        numbers = [int(number) for number in numbers]
        return numbers

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        numbers, custom_delimiter = self._parse_raw_numbers(numbers)
        numbers = self._split_numbers(numbers, custom_delimiter)
        numbers = self._ignore_big_numbers(numbers)
        self._assert_no_negative_numbers(numbers)
        return sum(numbers)
