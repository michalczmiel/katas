from decimal import Decimal
from typing import List, Union

from babel.numbers import format_currency


class SalarySlipFormatter:
    def __init__(self) -> None:
        self.lines: List[str] = []

    def _format_value(
        self, value: Decimal, currency: str = "GBP", locale="en_GB"
    ) -> str:
        return format_currency(value, currency=currency, locale=locale)

    def add(self, key: str, value: Union[Decimal, str]) -> None:
        if not value:
            return

        formatted_value = (
            self._format_value(value) if isinstance(value, Decimal) else value
        )

        self.lines.append(f"{key}: {formatted_value}")

    def format(self) -> str:
        return "\n".join(self.lines)
