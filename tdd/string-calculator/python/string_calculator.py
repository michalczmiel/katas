import abc
import re


class NumbersParser:
    def __init__(self) -> None:
        self._default_delimiters: tuple[str] = (",", "\n")
        self._delimiter_change_chars: str = "//"

    def _has_single_char_delimiter(self, delimiter_part: str) -> bool:
        return len(self._delimiter_change_chars) + 1 == len(delimiter_part)

    def _extract_delimiters(self, raw_numbers: str) -> tuple[str, list[str]]:
        if not raw_numbers.startswith(self._delimiter_change_chars):
            return raw_numbers, []

        delimiter_part, numbers_part = raw_numbers.split("\n")

        if self._has_single_char_delimiter(delimiter_part):
            custom_delimiter = delimiter_part[len(self._delimiter_change_chars) :]
            return numbers_part, [custom_delimiter]

        custom_delimiters = re.findall(r"\[(.*?)\]", delimiter_part)
        return numbers_part, custom_delimiters

    def _split_numbers(
        self, raw_numbers: str, custom_delimiters: list[str]
    ) -> list[int]:
        numbers = raw_numbers
        for custom_delimiter in custom_delimiters:
            numbers = numbers.replace(custom_delimiter, self._default_delimiters[0])
        delimiters = "|".join(self._default_delimiters)
        numbers = re.split(delimiters, numbers)
        numbers = [int(number) for number in numbers]
        return numbers

    def parse(self, raw_numbers: str) -> list[int]:
        numbers, custom_delimiters = self._extract_delimiters(raw_numbers)
        numbers = self._split_numbers(numbers, custom_delimiters)

        return numbers


class Validator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def validate(self, numbers: list[int]) -> list[int]:
        raise NotImplementedError


class NoNegativeNumbersValidator(Validator):
    def validate(self, numbers: list[int]) -> list[int]:
        negative_numbers = [str(number) for number in numbers if number < 0]

        if not negative_numbers:
            return numbers
        elif len(negative_numbers) == 1:
            raise Exception("negatives not allowed")
        raise Exception(
            f"negatives not allowed, but found {', '.join(negative_numbers)}"
        )


class MaxNumberValidator(Validator):
    def __init__(self, max_number: int) -> None:
        self._max_number = max_number

    def validate(self, numbers: list[int]) -> list[int]:
        return [number for number in numbers if number <= self._max_number]


class StringCalculator:
    def __init__(self) -> None:
        self._parser = NumbersParser()
        self._validators = [
            NoNegativeNumbersValidator(),
            MaxNumberValidator(max_number=1000),
        ]

    def add(self, raw_numbers: str) -> int:
        if not raw_numbers:
            return 0

        numbers = self._parser.parse(raw_numbers)

        for validator in self._validators:
            numbers = validator.validate(numbers)

        return sum(numbers)
