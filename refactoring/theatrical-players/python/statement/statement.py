import math
from dataclasses import dataclass
from typing import TypedDict, List, Dict
from abc import ABC, abstractmethod


class Performance(TypedDict):
    playID: str
    audience: int


class Invoice(TypedDict):
    customer: str
    performances: List[Performance]


class Play(TypedDict):
    name: str
    type: str


class PlaySummary(TypedDict):
    name: str
    amount: int
    audience: int


class CompletedPlay(ABC):
    name: str
    audience: int

    @property
    @abstractmethod
    def amount(self) -> int:
        pass

    @property
    @abstractmethod
    def volume_credits(self) -> int:
        pass


def render_statement(
    customer: str,
    total_amount: int,
    volume_credits: int,
    play_list: List[CompletedPlay],
) -> str:
    result = f"Statement for {customer}\n"

    def format_as_dollars(amount) -> str:
        return f"${amount:0,.2f}"

    for play in play_list:
        result += f" {play.name}: {format_as_dollars(play.amount/100)} ({play.audience} seats)\n"

    result += f"Amount owed is {format_as_dollars(total_amount/100)}\n"
    result += f"You earned {volume_credits} credits\n"

    return result


@dataclass(frozen=True)
class ComedyCompletedPlay(CompletedPlay):
    name: str
    audience: int

    @property
    def amount(self) -> int:
        this_amount = 30000
        if self.audience > 20:
            this_amount += 10000 + 500 * (self.audience - 20)

        this_amount += 300 * self.audience
        return this_amount

    @property
    def volume_credits(self) -> int:
        credits = max(self.audience - 30, 0)
        # add extra credit for every ten comedy attendees
        credits += math.floor(self.audience / 5)
        return credits


@dataclass(frozen=True)
class TragedyCompletedPlay(CompletedPlay):
    name: str
    audience: int

    @property
    def amount(self) -> int:
        this_amount = 40000
        if self.audience > 30:
            this_amount += 1000 * (self.audience - 30)
        return this_amount

    @property
    def volume_credits(self) -> int:
        credits = max(self.audience - 30, 0)
        return credits


def map_to_completed_play(play: Play, performance: Performance) -> CompletedPlay:
    if play["type"] == "tragedy":
        return TragedyCompletedPlay(name=play["name"], audience=performance["audience"])
    elif play["type"] == "comedy":
        return ComedyCompletedPlay(name=play["name"], audience=performance["audience"])
    else:
        raise ValueError(f'unknown type: {play["type"]}')


def statement(invoice: Invoice, plays: Dict[str, Play]) -> str:
    total_amount = 0
    volume_credits = 0
    play_list: List[CompletedPlay] = []

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]

        completed_play = map_to_completed_play(play, perf)

        volume_credits += completed_play.volume_credits
        total_amount += completed_play.amount

        play_list.append(completed_play)

    result = render_statement(
        invoice["customer"],
        total_amount,
        volume_credits,
        play_list,
    )

    return result
