import re


def read_input(file_name: str) -> str:
    with open(file_name) as f:
        return f.read()


def evaluate_mul_instruction(instruction: str) -> int:
    first, second = re.findall(r"\d+", instruction)

    return int(first) * int(second)


def sum_of_multiplications(data: str) -> int:
    result = 0

    instructions = re.findall(r"mul\(\d+,\d+\)", data)

    result = sum(evaluate_mul_instruction(instruction) for instruction in instructions)

    return result


ENABLE_INSTRUCTION = "do()"
DISABLE_INSTRUCTION = "don't()"


def sum_of_multiplications_with_conditional_instructions(data: str) -> int:
    result = 0
    enabled = True

    instructions = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", data)

    for instruction in instructions:
        if instruction == ENABLE_INSTRUCTION:
            enabled = True
        elif instruction == DISABLE_INSTRUCTION:
            enabled = False
        elif enabled:
            result += evaluate_mul_instruction(instruction)

    return result


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/3"""

    data = read_input("3.txt")

    print(sum_of_multiplications(data))
    print(sum_of_multiplications_with_conditional_instructions(data))


if __name__ == "__main__":
    solution()
