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

    return any(
        can_bag_contain(rules, rule_color, searched_color)
        for rule_color in color_rules.keys()
    )


def count_bag_colors(rules: dict[Color, BagRule], searched_color: Color) -> int:
    count = 0

    for color in rules.keys():
        if can_bag_contain(rules, color, searched_color):
            count += 1

    return count


def count_bags_inside_bag(rules: dict[Color, BagRule], searched_color: Color) -> int:
    color_rules = rules[searched_color]

    if not color_rules:
        return 0

    total_count = 0

    for rule_color, rule_quantity in color_rules.items():
        total_count += rule_quantity

        count = count_bags_inside_bag(rules, rule_color)

        total_count += rule_quantity * count

    return total_count


def solution() -> None:
    """Solution to https://adventofcode.com/2020/day/7"""

    owned_color = "shiny gold"

    print(count_bag_colors(read_input(), owned_color))
    print(count_bags_inside_bag(read_input(), owned_color))


if __name__ == "__main__":
    solution()
