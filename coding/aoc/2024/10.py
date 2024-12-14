from typing import NewType

TopographicMap = NewType("TopographicMap", dict[tuple[int, int], int])


def read_input(file_name: str) -> TopographicMap:
    data = {}

    with open(file_name) as file:
        for y, line in enumerate(file):
            for x, height in enumerate(line.strip()):
                point = (int(x), int(y))
                data[point] = int(height)
    return data


def calculate_trail_head_score(start: tuple[int, int], data: TopographicMap) -> int:
    directions = {(-1, 0), (0, -1), (1, 0), (0, 1)}
    path = [start]
    top_positions = set()

    while path:
        point = path.pop()
        height = data[point]

        if height == 9:
            top_positions.add(point)

        for dx, dy in directions:
            x, y = point
            new_point = (x + dx, y + dy)
            new_point_height = data.get(new_point)
            if new_point_height is None or new_point_height - 1 != height:
                continue
            path.append(new_point)

    return len(top_positions)


def calculate_sum_of_trail_head_scores(data: TopographicMap) -> int:
    score_sum = 0

    trail_heads = [point for point, height in data.items() if height == 0]

    score_sum = sum(
        calculate_trail_head_score(trail_head, data) for trail_head in trail_heads
    )

    return score_sum


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/9"""

    data = read_input("10.txt")
    print(calculate_sum_of_trail_head_scores(data))


if __name__ == "__main__":
    solution()
