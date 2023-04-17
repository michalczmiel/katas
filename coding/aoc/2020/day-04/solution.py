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


def count_valid_passports(passports: list[list[str]]) -> int:
    count = 0
    required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    for passport in passports:
        keys = {field.split(":")[0] for field in passport}

        if keys.issuperset(required_keys):
            print(passport)
            count += 1

    return count


def solution() -> None:
    """Solution to https://adventofcode.com/2020/day/4"""

    print(count_valid_passports(read_input()))


if __name__ == "__main__":
    solution()
