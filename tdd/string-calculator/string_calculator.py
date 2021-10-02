import re
from typing import Optional, Tuple

class StringCalculator:
    def __init__(self) -> None:
        self._default_delimiters: Tuple[str] = (",", "\n")

    def _get_custom_delimiter(self, numbers: str) -> Optional[str]:
        if not numbers.startswith("//"):
            return
        custom_delimiter = numbers.split("\n")[0][2]
        return custom_delimiter

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
        return sum(numbers)
