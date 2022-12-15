from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Pair:
    minimum: int
    maximum: int

    def contains(self, pair: "Pair") -> bool:
        return self.minimum >= pair.minimum and self.maximum <= pair.maximum

    def overlaps(self, pair: "Pair") -> bool:
        return self.minimum >= pair.minimum and self.minimum <= pair.maximum


def read_input(file_name: str) -> Iterator[Pair]:
    with open(file_name) as file:
        for line in file:
            first, second = line.strip().split(",")
            first_min, first_max = [int(number) for number in first.split("-")]
            second_min, second_max = [int(number) for number in second.split("-")]
            yield (Pair(first_min, first_max), Pair(second_min, second_max))


def count_pairs_fully_contain(pairs: Iterator[Pair]) -> int:
    count = 0

    for first, second in pairs:
        if first.contains(second) or second.contains(first):
            count += 1

    return count


def count_pairs_overlap(pairs: Iterator[Pair]) -> int:
    count = 0

    for first, second in pairs:
        if first.overlaps(second) or second.overlaps(first):
            count += 1

    return count


def solution() -> None:
    """Solution to https://adventofcode.com/2022/day/4"""

    print(count_pairs_fully_contain(read_input("input.txt")))
    print(count_pairs_overlap(read_input("input.txt")))


if __name__ == "__main__":
    solution()
