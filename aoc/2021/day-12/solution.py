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


def visit(system: Dict[str, Set[str]], node: str, path: str, found_paths: Set[str]) -> None:
    """
    Perform DFS to compute all possible paths
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

        visit(system, neighbor, path, found_paths)


def get_at_most_once_small_caves_paths_count(connections: List[Tuple[str, str]]) -> int:
    system = build_system_map(connections)

    found_paths: Set[str] = set()
    path = ""

    visit(system, "start", path, found_paths)

    return len(found_paths)


def solution() -> None:
    """Solution to https://adventofcode.com/2021/day/12"""

    print(get_at_most_once_small_caves_paths_count(read_input()))


if __name__ == "__main__":
    solution()
