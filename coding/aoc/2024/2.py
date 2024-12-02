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

        if abs(difference) < 1 or abs(difference) > 3:
            return False

        ordering = -1 if difference < 0 else 1
        if previous_ordering is None:
            previous_ordering = ordering
            continue

        if previous_ordering != ordering:
            return False

    return True


def count_safe_reports(reports: list[Report]) -> int:
    count = 0

    for report in reports:
        if is_report_safe(report):
            count += 1
    return count


def count_safe_reports_with_tolerate(reports: list[Report]) -> int:
    count = 0

    for report in reports:
        variants = [report]

        for i in range(len(report)):
            # new variant without the given number
            variants.append([*report[:i], *report[i + 1 :]])

        if any(is_report_safe(report) for report in variants):
            count += 1

    return count


def solution() -> None:
    """Solution to https://adventofcode.com/2024/day/2"""

    data = read_input("2.txt")

    print(count_safe_reports(data))
    print(count_safe_reports_with_tolerate(data))


if __name__ == "__main__":
    solution()
