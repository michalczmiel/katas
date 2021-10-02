import pytest

from string_calculator import StringCalculator


def test_returns_zero_for_empty_string():
    assert StringCalculator().add("") == 0

def test_returns_number_if_one_number_is_given():
    assert StringCalculator().add("1") == 1

def test_returns_sum_if_two_numbers_are_given():
    assert StringCalculator().add("1,2") == 3

def test_returns_sum_if_multiple_numbers_are_given():
    assert StringCalculator().add("1,2,3,4") == 10

def test_returns_sum_if_delimiter_is_also_new_line():
    assert StringCalculator().add("1\n2,3") == 6

def test_returns_sum_if_delimiter_is_changed():
    assert StringCalculator().add("//;\n1;2") == 3

def test_throws_error_when_negative_number_is_given():
    with pytest.raises(Exception) as exception_info:
        StringCalculator().add("//;\n1;-2")
    assert "negatives not allowed" in str(exception_info.value)

def test_throws_error_when_multiple_negative_numbers_is_given():
    with pytest.raises(Exception) as exception_info:
        StringCalculator().add("//;\n-1;-2")
    assert "negatives not allowed, but found -1, -2" in str(exception_info.value)

def test_ignores_numbers_bigger_than_1000():
    assert StringCalculator().add("2,1000") == 1002
    assert StringCalculator().add("2,1001") == 2

def test_returns_sum_if_any_length_delimiter_is_changed():
    assert StringCalculator().add("//[***]\n1***2***3") == 6

def test_returns_sum_if_multiple_delimiters_are_set():
    assert StringCalculator().add("//[*][%]\n1*2%3") == 6

def test_returns_sum_if_multiple_any_length_delimiters_are_set():
    assert StringCalculator().add("//[***][%%]\n1***2%%3") == 6
