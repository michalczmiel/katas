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


def render_statement(
    customer: str, total_amount: int, volume_credits: int, summaries: List[PlaySummary]
) -> str:
    result = f"Statement for {customer}\n"

    def format_as_dollars(amount) -> str:
        return f"${amount:0,.2f}"

    for summary in summaries:
        result += f' {summary["name"]}: {format_as_dollars(summary["amount"]/100)} ({summary["audience"]} seats)\n'

    result += f"Amount owed is {format_as_dollars(total_amount/100)}\n"
    result += f"You earned {volume_credits} credits\n"

    return result


class CompletedPlay(ABC):
    @property
    @abstractmethod
    def audience(self) -> int:
        pass

    @property
    @abstractmethod
    def amount(self) -> int:
        pass


@dataclass(frozen=True)
class ComedyCompletedPlay(CompletedPlay):
    audience: int

    @property
    def amount(self) -> int:
        this_amount = 30000
        if self.audience > 20:
            this_amount += 10000 + 500 * (self.audience - 20)

        this_amount += 300 * self.audience
        return this_amount


@dataclass(frozen=True)
class TragedyCompletedPlay(CompletedPlay):
    audience: int

    @property
    def amount(self) -> int:
        this_amount = 40000
        if self.audience > 30:
            this_amount += 1000 * (self.audience - 30)
        return this_amount


def map_to_completed_play(play: Play, performance: Performance) -> CompletedPlay:
    if play["type"] == "tragedy":
        return TragedyCompletedPlay(audience=performance["audience"])
    elif play["type"] == "comedy":
        return ComedyCompletedPlay(audience=performance["audience"])
    else:
        raise ValueError(f'unknown type: {play["type"]}')


def statement(invoice: Invoice, plays: Dict[str, Play]) -> str:
    total_amount = 0
    volume_credits = 0
    summaries: List[PlaySummary] = []

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]

        completed_play = map_to_completed_play(play, perf)

        # add volume credits
        volume_credits += max(perf["audience"] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf["audience"] / 5)

        summaries.append(
            {
                "name": play["name"],
                "amount": completed_play.amount,
                "audience": completed_play.audience,
            }
        )

        total_amount += completed_play.amount

    result = render_statement(
        invoice["customer"],
        total_amount,
        volume_credits,
        summaries,
    )

    return result
