from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class CategoryRange:
    destination_start: int
    source_start: int
    length: int

    def contains(self, key) -> bool:
        lower_bound = self.source_start
        upper_bound = self.source_start + (self.length - 1)

        return lower_bound <= key <= upper_bound

    def get_destination(self, source: int) -> int:
        increase = source - self.source_start
        return self.destination_start + increase


@dataclass(frozen=True)
class Almanac:
    seeds: list[int]
    mappings: dict[str, list[CategoryRange]]


def look_up_from_ranges(ranges: list[CategoryRange], source: int) -> int:
    for range in ranges:
        if range.contains(source):
            return range.get_destination(source)
    return source


def read_input(file_name: str) -> Almanac:
    seeds = []
    mappings = defaultdict(list)
    current_mapping = ""

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith("seeds:"):
                _, raw_seeds = line.split("seeds:")
                seeds = [int(raw_seed) for raw_seed in raw_seeds.strip().split(" ")]
            elif line.endswith("map:"):
                mapping_key, _ = line.split("map:")
                _, category_key = mapping_key.strip().split("-to-")
                current_mapping = category_key
            else:
                destination_range_start, source_range_start, range_length = [
                    int(number) for number in line.split(" ")
                ]

                range = CategoryRange(
                    destination_start=destination_range_start,
                    source_start=source_range_start,
                    length=range_length,
                )

                mappings[current_mapping].append(range)

    return Almanac(seeds=seeds, mappings=mappings)


categories = [
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location",
]


def get_lowest_location_number(almanac: Almanac) -> int:
    locations = []

    for seed in almanac.seeds:
        temp = seed

        for category in categories:
            ranges = almanac.mappings[category]

            destination = look_up_from_ranges(ranges, temp)

            temp = destination

        locations.append(temp)

    return min(locations)


def process_seeds_as_if_range(original_seeds: list[int]) -> list[int]:
    seeds = set()

    i = 0

    while i < len(original_seeds):
        range_start = original_seeds[i]
        range_length = original_seeds[i + 1]

        for seed in range(range_start, range_start + range_length):
            seeds.add(seed)

        i += 2

    return seeds


def get_lowest_location_number_with_updated_seeds(almanac: Almanac) -> int:
    locations = []

    print(almanac)
    seeds = process_seeds_as_if_range(almanac.seeds)

    for seed in seeds:
        temp = seed

        for category in categories:
            ranges = almanac.mappings[category]

            destination = look_up_from_ranges(ranges, temp)

            temp = destination

        locations.append(temp)

    return min(locations)


def solution() -> None:
    """Solution to https://adventofcode.com/2023/day/5"""

    print(get_lowest_location_number(read_input("input.txt")))
    print(get_lowest_location_number_with_updated_seeds(read_input("input.txt")))


if __name__ == "__main__":
    solution()
