class StringCalculator:
    def add(self, numbers: str):
        if not numbers:
            return 0
        if len(numbers) == 3:
            return int(numbers[0]) + int(numbers[2])
        return int(numbers[0])
