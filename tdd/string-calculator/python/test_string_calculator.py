import pytest

from string_calculator import StringCalculator


@pytest.fixture
def calculator() -> StringCalculator:
    return StringCalculator()


def test_returns_zero_for_empty_string(calculator):
    assert calculator.add("") == 0


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ("0", 0),
        ("1", 1),
        ("2", 2),
    ],
)
def test_returns_number_if_single_number_is_given(calculator, numbers, expected):
    assert calculator.add(numbers) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ("0,1", 1),
        ("1,2,3", 6),
        ("1,2,3,4", 10),
    ],
)
def test_returns_sum_if_multiple_numbers_are_given(calculator, numbers, expected):
    assert calculator.add(numbers) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ("1\n2,3", 6),
        ("1\n2\n3", 6),
        ("1,2\n3,4", 10),
    ],
)
def test_returns_sum_if_delimiter_is_also_new_line(calculator, numbers, expected):
    assert calculator.add(numbers) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ("//;\n1;2;3", 6),
        ("//:\n1:2:3", 6),
        ("///\n1/2/3", 6),
    ],
)
def test_returns_sum_if_delimiter_is_changed(calculator, numbers, expected):
    assert calculator.add(numbers) == expected


def test_throws_error_when_negative_number_is_given(calculator):
    with pytest.raises(Exception) as exception_info:
        calculator.add("//;\n1;-2")
    assert "negatives not allowed" in str(exception_info.value)


def test_throws_error_when_multiple_negative_numbers_is_given(calculator):
    with pytest.raises(Exception) as exception_info:
        calculator.add("//;\n-1;-2")
    assert "negatives not allowed, but found -1, -2" in str(exception_info.value)


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ("2,1000", 1002),
        ("2,1001", 2),
        ("2,1001,1002", 2),
    ],
)
def test_ignores_big_numbers(calculator, numbers, expected):
    assert calculator.add(numbers) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ("//[***]\n1***2***3", 6),
        ("//[;;]\n1;;2;;3;;4", 10),
        ("//[%%%%]\n1%%%%2", 3),
    ],
)
def test_returns_sum_if_any_length_delimiter_is_changed(calculator, numbers, expected):
    assert calculator.add(numbers) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ("//[*][%]\n1*2%3", 6),
        ("//[*][%][&]\n1*2%3&4", 10),
        ("//[***][%%]\n1***2%%3", 6),
    ],
)
def test_returns_sum_if_multiple_delimiters_are_set(calculator, numbers, expected):
    assert calculator.add(numbers) == expected
