import re
from typing import Iterable, List, Optional, Tuple


class StringCalculator:
    def __init__(self) -> None:
        self._default_delimiters: Tuple[str] = (",", "\n")

    def _get_custom_delimiter(self, numbers: str) -> Optional[str]:
        if not numbers.startswith("//"):
            return
        custom_delimiter = numbers.split("\n")[0][2]
        return custom_delimiter

    def _assert_no_negative_numbers(self, numbers: Iterable[int]) -> None:
        negative_numbers = [str(number) for number in numbers if number < 0]
        if not negative_numbers:
            return
        elif len(negative_numbers) == 1:
            raise Exception("negatives not allowed")
        raise Exception(f"negatives not allowed, but found {', '.join(negative_numbers)}")

    def _ignore_big_numbers(self, numbers: List[int]) -> List[int]:
        return [number for number in numbers if number <= 1000]

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        custom_delimiter = self._get_custom_delimiter(numbers)
        delimiters = "|".join(self._default_delimiters)
        if custom_delimiter:
            numbers = numbers[4:]
            delimiters += f"|{custom_delimiter}"
        numbers = re.split(delimiters, numbers)
        numbers = [int(number) for number in numbers]
        numbers = self._ignore_big_numbers(numbers)
        self._assert_no_negative_numbers(numbers)
        return sum(numbers)
