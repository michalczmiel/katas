import pytest

from solution import look_up_from_ranges, CategoryRange, process_seeds_as_if_range


@pytest.mark.parametrize(
    "source,expected", [(97, False), (98, True), (99, True), (100, False)]
)
def test_category_range_contains(source, expected):
    category_range = CategoryRange(destination_start=50, source_start=98, length=2)

    assert category_range.contains(source) is expected


@pytest.mark.parametrize(
    "source,expected_destination",
    [(0, 0), (1, 1), (50, 52), (51, 53), (96, 98), (97, 99), (98, 50), (99, 51)],
)
def test_category_range_get_mapping(source, expected_destination):
    ranges = [
        CategoryRange(destination_start=50, source_start=98, length=2),
        CategoryRange(destination_start=52, source_start=50, length=48),
    ]

    destination = look_up_from_ranges(ranges, source)

    assert destination == expected_destination


def test_process_seeds_as_if_range():
    seeds_range = [79, 14, 55, 13]

    seeds = process_seeds_as_if_range(seeds_range)

    assert len(seeds) == 27
    assert seeds == {
        55,
        56,
        57,
        58,
        59,
        60,
        61,
        62,
        63,
        64,
        65,
        66,
        67,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        91,
        92,
    }
