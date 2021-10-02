import re

class StringCalculator:
    def add(self, numbers: str):
        if not numbers:
            return 0
        custom_delimiter = None
        if numbers.startswith("//"):
            custom_delimiter = numbers.split("\n")[0][2]
            numbers = numbers[4:]
        delimiters = ",|\n"
        if custom_delimiter:
            delimiters += f"|{custom_delimiter}"
        numbers = re.split(delimiters, numbers)
        numbers = [int(number) for number in numbers]
        return sum(numbers)
