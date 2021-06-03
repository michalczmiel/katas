import math
from typing import TypedDict, List, Dict


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


def statement(invoice: Invoice, plays: Dict[str, Play]) -> str:
    total_amount = 0
    volume_credits = 0
    summaries: List[PlaySummary] = []

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]
        if play["type"] == "tragedy":
            this_amount = 40000
            if perf["audience"] > 30:
                this_amount += 1000 * (perf["audience"] - 30)
        elif play["type"] == "comedy":
            this_amount = 30000
            if perf["audience"] > 20:
                this_amount += 10000 + 500 * (perf["audience"] - 20)

            this_amount += 300 * perf["audience"]

        else:
            raise ValueError(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf["audience"] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf["audience"] / 5)

        summaries.append(
            {
                "name": play["name"],
                "amount": this_amount,
                "audience": perf["audience"],
            }
        )

        total_amount += this_amount

    result = render_statement(
        invoice["customer"],
        total_amount,
        volume_credits,
        summaries,
    )

    return result
