from typing import NewType


Report = NewType("Report", list[int])


def read_input(file_name: str) -> list[Report]:
    reports = []

    for line in open(file_name):
        reports.append([int(level) for level in line.split(" ")])

    return reports


def is_report_safe(report: Report) -> bool:
    previous_ordering = None

    for i in range(1, len(report)):
        current = report[i]
        previous = report[i - 1]

        difference = current - previous
        ordering = -1 if difference < 0 else 1

        if previous_ordering is None:
            previous_ordering = ordering
        elif previous_ordering is not None and previous_ordering != ordering:
            return False

        if abs(difference) < 1 or abs(difference) > 3:
            return False

    return True


def count_safe_reports(reports: list[Report]) -> int:
    count = 0

    for report in reports:
        if is_report_safe(report):
            count += 1
    return count


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/2"""

    data = read_input("2.txt")

    print(count_safe_reports(data))


if __name__ == "__main__":
    solution()
