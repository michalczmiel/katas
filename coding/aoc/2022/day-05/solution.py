from typing import NewType
from collections import deque

Stacks = NewType("Stacks", dict[int, deque])
Instruction = NewType("Instruction", tuple[int])
Plan = NewType("Plan", tuple[Stacks, list[Instruction]])


def read_input(file_name: str) -> Plan:
    stack = {}
    instructions = []
    parsing_instructions = False

    with open(file_name) as file:
        for line in file:
            if line == "\n":
                parsing_instructions = True
                continue

            if parsing_instructions:
                _, count, _, from_index, _, to_index = line.strip().split(" ")

                instructions.append(
                    (int(count), int(from_index) - 1, int(to_index) - 1)
                )
                continue

            if "[" not in line:
                continue

            for i in range(0, len(line), 4):
                crate = line[i + 1]
                if crate == " ":
                    continue
                stack_index = i // 4
                if stack_index not in stack:
                    stack[stack_index] = deque()
                stack[stack_index].append(crate)

    return stack, instructions


def get_top_stack_crates(plan: Plan) -> str:
    starting_stacks, instructions = plan
    stacks = starting_stacks.copy()

    for crates_to_move, from_stack, to_stack in instructions:
        for _ in range(crates_to_move):
            crate = stacks[from_stack].popleft()
            stacks[to_stack].appendleft(crate)

    top_crates = [stack.popleft() for _, stack in sorted(stacks.items())]

    return "".join(top_crates)


def solution() -> None:
    """Solution to https://adventofcode.com/2022/day/5"""

    print(get_top_stack_crates(read_input("input.txt")))


if __name__ == "__main__":
    solution()
