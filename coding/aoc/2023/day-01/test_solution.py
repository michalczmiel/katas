import pytest

from solution import get_calibration_value

testdata = [
    ("1abc2", 12),
    ("pqr3stu8vwx", 38),
    ("a1b2c3d4e5f", 15),
    ("treb7uchet", 77),
    ("two1nine", 29),
    ("eightwothree", 83),
    ("abcone2threexyz", 13),
    ("xtwone3four", 24),
    ("4nineeightseven2", 42),
    ("zoneight234", 14),
    ("7pqrstsixteen", 76),
    ("oneight", 18),
    ("eighthree", 83),
    ("fourfourfour", 44),
    ("oneightwoneight", 18),
    ("sevenine", 79),
    ("9fgsixzkbscvbxdsfive6spjfhzxbzvgbvrthreeoneightn", 98),
    ("oneightwonethree", 13),
    ("oonethreee", 13),
]


@pytest.mark.parametrize("line,expected", testdata)
def test_get_calibration_value(line, expected):
    given = get_calibration_value(line)
    assert given == expected
