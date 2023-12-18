import functools
import operator
from dataclasses import dataclass


@dataclass(frozen=True)
class Race:
    time: int
    distance: int

    def count_win_combinations(self) -> int:
        """
        Calcuate win combinations using brute force approach.
        TODO: Come up with more efficient solution
        """
        combinations_count = 0

        for holding_time in range(0, self.time + 1):
            remaining_time = self.time - holding_time
            travelled_distance = remaining_time * holding_time

            if travelled_distance > self.distance:
                combinations_count += 1

        return combinations_count


def read_input_as_multiple_races(file_name: str) -> list[Race]:
    races = []

    with open(file_name, "r") as file:
        raw_time, raw_distance = file.readlines()
        times = [
            int(element) for element in raw_time.strip().split(" ") if element.isdigit()
        ]
        distances = [
            int(element)
            for element in raw_distance.strip().split(" ")
            if element.isdigit()
        ]

        for time, distance in zip(times, distances):
            races.append(Race(time, distance))

    return races


def read_input_as_single_race(file_name: str) -> Race:
    with open(file_name, "r") as file:
        raw_time, raw_distance = file.readlines()
        time = int(
            "".join([part for part in raw_time.strip().split(" ") if part.isdigit()])
        )
        distance = int(
            "".join(
                [part for part in raw_distance.strip().split(" ") if part.isdigit()]
            )
        )

        return Race(time, distance)


def calculate_error_margin_from_multiple_races(races: list[Race]) -> int:
    return functools.reduce(
        operator.mul, (race.count_win_combinations() for race in races)
    )


def calculate_error_margin(race: Race) -> int:
    return race.count_win_combinations()


def solution() -> None:
    """Solution to https://adventofcode.com/2023/day/6"""

    print(
        calculate_error_margin_from_multiple_races(
            read_input_as_multiple_races("input.txt")
        )
    )
    print(calculate_error_margin(read_input_as_single_race("input.txt")))


if __name__ == "__main__":
    solution()
