from dataclasses import dataclass


@dataclass(frozen=True)
class GameSet:
    blue: int = 0
    green: int = 0
    red: int = 0


@dataclass(frozen=True)
class Game:
    id: int
    sets: list[GameSet]

    @classmethod
    def from_str(cls, line: str) -> "Game":
        game_raw, sets_raw = line.split(":")

        _, game_id = game_raw.split(" ")

        sets = []
        for raw_set in sets_raw.split(";"):
            cubes_in_set = {}

            for raw_cubes in raw_set.strip().split(", "):
                quantity, color = raw_cubes.split(" ")
                cubes_in_set[color] = int(quantity)

            sets.append(GameSet(**cubes_in_set))

        return cls(id=int(game_id), sets=sets)

    @property
    def highest_blue(self) -> int:
        return max([set.blue for set in self.sets])

    @property
    def highest_green(self) -> int:
        return max([set.green for set in self.sets])

    @property
    def highest_red(self) -> int:
        return max([set.red for set in self.sets])


def read_input(file_name: str) -> list[Game]:
    games = []

    with open(file_name, "r") as file:
        for line in file:
            games.append(Game.from_str(line.strip()))

    return games


def calculate_possible_games_outcome(
    games: list[Game], red: int, green: int, blue: int
) -> int:
    possible_games_ids = (
        game.id
        for game in games
        if game.highest_red <= red
        and game.highest_green <= green
        and game.highest_blue <= blue
    )

    return sum(possible_games_ids)


def calculate_power_of_fewest_number_sets(games: list[Game]) -> int:
    return sum(
        game.highest_blue * game.highest_green * game.highest_red for game in games
    )


def solution() -> None:
    """Solution to https://adventofcode.com/2023/day/2"""

    print(
        calculate_possible_games_outcome(
            read_input("input.txt"), red=12, green=13, blue=14
        )
    )
    print(calculate_power_of_fewest_number_sets(read_input("input.txt")))


if __name__ == "__main__":
    solution()
