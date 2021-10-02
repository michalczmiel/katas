import re

class StringCalculator:
    def add(self, numbers: str):
        if not numbers:
            return 0
        numbers = re.split(",|\n", numbers)
        numbers = (int(number) for number in numbers)
        return sum(numbers)
