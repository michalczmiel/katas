import re
from dataclasses import dataclass
from typing import Optional


def read_input() -> list[list[str]]:
    passports = []
    fields = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            fields.extend(field for field in line.split(" ") if field)

            if not line:
                passports.append(fields)
                fields = []

    passports.append(fields)
    return passports


EYE_COLOR_OPTIONS = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def is_valid_hex_color(color: str) -> bool:
    pattern = re.compile("#[0-9a-f]{6}")
    return bool(pattern.match(color))


@dataclass
class Passport:
    # Birth Year
    byr: Optional[str] = None
    # Issue Year
    iyr: Optional[str] = None
    # Expiration Year
    eyr: Optional[str] = None
    # Height
    hgt: Optional[str] = None
    # Hair Color
    hcl: Optional[str] = None
    # Eye Color
    ecl: Optional[str] = None
    # Passport ID
    pid: Optional[str] = None
    # Country ID
    cid: Optional[int] = None

    @property
    def is_birth_year_valid(self) -> bool:
        return 1920 <= int(self.byr) <= 2002

    @property
    def is_issue_year_valid(self) -> bool:
        return 2010 <= int(self.iyr) <= 2020

    @property
    def is_expiration_year_valid(self) -> bool:
        return 2020 <= int(self.eyr) <= 2030

    @property
    def is_height_valid(self) -> bool:
        (height, unit), _ = re.findall(r"([0-9]*)([a-z]*)", self.hgt)

        if unit == "cm":
            return 150 <= int(height) <= 193
        elif unit == "in":
            return 59 <= int(height) <= 76
        return False

    @property
    def is_hair_color_valid(self) -> bool:
        return is_valid_hex_color(self.hcl)

    @property
    def is_eye_color_valid(self) -> bool:
        return self.ecl in EYE_COLOR_OPTIONS

    @property
    def is_passport_id_valid(self) -> bool:
        return len(self.pid) == 9

    @property
    def is_valid(self) -> bool:
        try:
            return all(
                [
                    self.is_birth_year_valid,
                    self.is_issue_year_valid,
                    self.is_expiration_year_valid,
                    self.is_height_valid,
                    self.is_hair_color_valid,
                    self.is_eye_color_valid,
                    self.is_passport_id_valid,
                ]
            )
        except:
            return False


def count_valid_passports(passports: list[list[str]]) -> int:
    count = 0
    required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    for passport in passports:
        keys = {field.split(":")[0] for field in passport}

        if keys.issuperset(required_keys):
            count += 1

    return count


def count_valid_passports_with_improved_validation(passports: list[list[str]]) -> int:
    count = 0

    for raw_passport in passports:
        values = {}
        for field in raw_passport:
            key, value = field.split(":")
            values[key] = value

        passport = Passport(**values)

        if passport.is_valid:
            count += 1

    return count


def solution() -> None:
    """Solution to https://adventofcode.com/2020/day/4"""

    print(count_valid_passports(read_input()))
    print(count_valid_passports_with_improved_validation(read_input()))


if __name__ == "__main__":
    solution()
