def read_input() -> list[int]:
    with open("input.txt") as file:
        return [int(value) for value in file.read().strip().split(",")]


ADD_OPCODE = 1
MULTIPLY_OPCODE = 2
HALT_OPCODE = 99


def process_program(values: list[int]) -> int:
    i = 0

    updated = values.copy()

    updated[1] = 12
    updated[2] = 2

    while i < len(updated):
        value = updated[i]

        if value == ADD_OPCODE:
            first_input_position = values[i + 1]
            second_input_position = values[i + 2]
            output_position = values[i + 3]

            updated[output_position] = (
                updated[first_input_position] + updated[second_input_position]
            )

            i += 4
        elif value == MULTIPLY_OPCODE:
            first_input_position = values[i + 1]
            second_input_position = values[i + 2]
            output_position = values[i + 3]

            updated[output_position] = (
                updated[first_input_position] * updated[second_input_position]
            )

            i += 4
        elif value == HALT_OPCODE:
            break

    return updated[0]


def solution() -> None:
    """Solution to https://adventofcode.com/2019/day/2"""

    print(process_program(read_input()))


if __name__ == "__main__":
    solution()
