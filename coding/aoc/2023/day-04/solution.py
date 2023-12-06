from dataclasses import dataclass
from functools import cached_property


@dataclass(frozen=True)
class Card:
    id: str
    winning_numbers: set[str]
    numbers: set[str]

    @classmethod
    def from_str(cls, line: str) -> "Card":
        raw_card_label, all_numbers = line.split(":")
        *_, raw_card_id = raw_card_label.strip().split(" ")

        raw_winning_numbers, raw_numbers = all_numbers.split("|")

        winning_numbers = {
            number for number in raw_winning_numbers.strip().split(" ") if number
        }
        numbers = {number for number in raw_numbers.strip().split(" ") if number}

        return cls(id=raw_card_id, winning_numbers=winning_numbers, numbers=numbers)

    @cached_property
    def matches_count(self) -> int:
        return len(self.numbers.intersection(self.winning_numbers))

    @property
    def points(self) -> int:
        matches_count = self.matches_count

        if matches_count == 0:
            return 0

        return 2 ** (matches_count - 1)


def read_input(file_name: str) -> list[Card]:
    cards = []
    with open(file_name, "r") as file:
        for line in file:
            card = Card.from_str(line)
            cards.append(card)

    return cards


def calculate_total_points(cards: list[Card]) -> int:
    return sum(card.points for card in cards)


def calculate_total_scratchcards(cards: list[Card]) -> int:
    """
    Matches win copies of cards bellow the winning card
    """
    total_scratchcards = 0

    cards_to_process = cards.copy()

    while cards_to_process:
        total_scratchcards += 1

        card = cards_to_process.pop()

        matches_count = card.matches_count
        if matches_count == 0:
            continue

        card_id = int(card.id)
        for i in range(card_id + 1, card_id + matches_count + 1):
            cards_to_process.append(cards[i - 1])

    return total_scratchcards


def solution() -> None:
    print(calculate_total_points(read_input("input.txt")))
    print(calculate_total_scratchcards(read_input("input.txt")))


if __name__ == "__main__":
    solution()
