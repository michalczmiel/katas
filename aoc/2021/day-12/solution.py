from typing import Dict, List, Set, Tuple
from collections import defaultdict


def read_input() -> List:
    """
    Read and parse input from text file
    """
    with open("input.txt") as file:
        connections = []

        for line in file.readlines():
            beginning, end = line.strip().split("-")
            connections.append((beginning, end))

        return connections


def build_system_map(connections: List[Tuple[str, str]]) -> Dict:
    """
    Create graph from connections
    """
    system = defaultdict(set)

    for beginning, end in connections:
        system[beginning].add(end)
        system[end].add(beginning)

    return system


def visit_once(
    system: Dict[str, Set[str]], node: str, path: str, found_paths: Set[str]
) -> None:
    """
    Perform DFS to compute all possible paths if small cave can be visited at most once
    """
    path += node + ","

    if node == "end":
        found_paths.add(path)
        return

    neighbors = system[node]

    for neighbor in neighbors:
        # check if small cave has been already visited
        if neighbor.islower() and neighbor in path.split(","):
            continue

        visit_once(system, neighbor, path, found_paths)


def get_at_most_once_small_caves_paths_count(connections: List[Tuple[str, str]]) -> int:
    system = build_system_map(connections)

    found_paths: Set[str] = set()
    path = ""

    visit_once(system, "start", path, found_paths)

    return len(found_paths)


def visit_twice(
    system: Dict[str, Set[str]],
    node: str,
    path: str,
    found_paths: Set[str],
    visited_small_cave_twice: bool,
) -> None:
    """
    Perform DFS to compute all possible paths if one small cave can be visited at most twice
    """
    path += node + ","

    if node == "end":
        found_paths.add(path)
        return

    neighbors = system[node]

    caves_in_path = path.split(",")

    for neighbor in neighbors:
        is_small_cave = neighbor.islower()

        if (
            neighbor == "end"
            or neighbor.isupper()
            or (is_small_cave and not neighbor in caves_in_path)
            or (
                is_small_cave
                and neighbor not in {"start", "end"}
                and not visited_small_cave_twice
            )
        ):
            new_visited_small_cave_twice = visited_small_cave_twice

            if (
                not visited_small_cave_twice
                and is_small_cave
                and neighbor in caves_in_path
            ):
                new_visited_small_cave_twice = True

            visit_twice(
                system, neighbor, path, found_paths, new_visited_small_cave_twice
            )


def get_at_most_twice_single_caves_paths_count(
    connections: List[Tuple[str, str]]
) -> int:
    system = build_system_map(connections)

    found_paths: Set[str] = set()
    path = ""

    visit_twice(system, "start", path, found_paths, False)

    return len(found_paths)


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/12"""

    print(get_at_most_once_small_caves_paths_count(read_input()))
    print(get_at_most_twice_single_caves_paths_count(read_input()))


if __name__ == "__main__":
    solution()
