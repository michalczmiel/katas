class StringCalculator:
    def add(self, numbers: str):
        if not numbers:
            return 0
        return sum(int(number) for number in numbers.split(","))
