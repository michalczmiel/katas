from typing import NewType

Color = NewType("Color", str)
BagRule = NewType("BagRule", dict[Color, int])


def read_input() -> dict[Color, BagRule]:
    rules = {}

    with open("input.txt") as file:
        for rule in file:
            rule = rule.strip().replace(".", "")
            rule_color, rule_bags_raw = rule.split(" bags contain ")

            rules[rule_color] = {}

            for raw_bag_rule in rule_bags_raw.split(", "):
                if raw_bag_rule == "no other bags":
                    continue
                raw_count, first_name, second_name, _ = raw_bag_rule.split(" ")
                name = f"{first_name} {second_name}"
                rules[rule_color][name] = int(raw_count)

    return rules


def can_bag_contain(
    rules: dict[Color, BagRule], color: Color, searched_color: Color
) -> bool:
    color_rules = rules[color]

    if not color_rules:
        return False

    if searched_color in color_rules:
        return True

    for rule_color, rule_quantity in color_rules.items():
        if can_bag_contain(rules, rule_color, searched_color):
            return True

    return False


def count_bag_colors(rules: dict[Color, BagRule]) -> int:
    count = 0

    owned_color = "shiny gold"

    for color, color_rules in rules.items():
        if can_bag_contain(rules, color, owned_color):
            count += 1

    return count


def solution() -> None:
    """Solution to https://adventofcode.com/2020/day/7"""

    print(count_bag_colors(read_input()))


if __name__ == "__main__":
    solution()
