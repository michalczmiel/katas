from typing import NewType

Equation = NewType("Equation", tuple[int, list[int]])


def read_input(file_name: str) -> list[Equation]:
    equations = []
    for line in open(file_name):
        result, raw_parts = line.strip().split(":")
        parts = [int(part) for part in raw_parts.split(" ") if part]
        equations.append((int(result), parts))

    return equations


def is_correct(equation: Equation, check_concat: bool) -> bool:
    """
    Start from the last element, find the possible two or three combinations that let to the target and repeat
    """
    target, parts = equation

    if len(parts) == 1:
        return target == parts[0]

    new_parts = parts.copy()
    last_element = new_parts.pop()

    new_target_mul = target / last_element
    # all inputs are integers
    if new_target_mul % 1 == 0:
        new_equation = (int(new_target_mul), new_parts)
        if is_correct(new_equation, check_concat):
            return True

    new_target_add = target - last_element
    # there are no negative values
    if new_target_add >= 0:
        new_equation = (new_target_add, new_parts)
        if is_correct(new_equation, check_concat):
            return True

    if check_concat and str(target).endswith(str(last_element)):
        new_target_concat = str(target)[: -len(str(last_element))]
        if new_target_concat == "":
            return False

        new_equation = (int(new_target_concat), new_parts)
        if is_correct(new_equation, check_concat):
            return True

    return False


def sum_true_calculations_values_with_concat(equations: list[Equation]):
    return sum(
        equation[0] for equation in equations if is_correct(equation, check_concat=True)
    )


def sum_true_calculations_values(equations: list[Equation]):
    return sum(
        equation[0]
        for equation in equations
        if is_correct(equation, check_concat=False)
    )


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/7"""

    data = read_input("7.txt")
    print(sum_true_calculations_values(data))
    print(sum_true_calculations_values_with_concat(data))


if __name__ == "__main__":
    solution()
