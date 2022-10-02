import re
from dataclasses import dataclass
from decimal import Decimal

from babel.numbers import parse_decimal, format_currency


@dataclass
class Employee:
    id: str
    name: str
    annual_gross: Decimal

    @classmethod
    def from_formatted_annual_gross(
        cls, id: str, name: str, formatted_annual_gross: str, locale: str = "en_GB"
    ) -> "Employee":
        formatted_annual_gross_without_currency = re.sub(
            "[^0-9|.,]", "", formatted_annual_gross
        )

        annual_gross = parse_decimal(formatted_annual_gross_without_currency, locale)

        return cls(id, name, annual_gross)


@dataclass
class SalarySlip:
    employee_id: str
    employee_name: str
    gross_salary: Decimal

    def _format_value(
        self, value: Decimal, currency: str = "GBP", locale="en_GB"
    ) -> str:
        return format_currency(value, currency=currency, locale=locale)

    def __str__(self) -> str:
        lines = [
            f"Employee ID: {self.employee_id}",
            f"Employee Name: {self.employee_name}",
            f"Gross Salary: {self._format_value(self.gross_salary)}",
        ]

        return "\n".join(lines)


class SalarySlipCalculator:
    months_in_year = Decimal(12)

    @classmethod
    def calculate_monthly_gross_salary(cls, annual_gross: Decimal) -> Decimal:
        return annual_gross / cls.months_in_year


class SalarySlipGenerator:
    def generate_for(self, employee: Employee) -> SalarySlip:
        gross_salary = SalarySlipCalculator.calculate_monthly_gross_salary(
            employee.annual_gross
        )

        return SalarySlip(
            employee_id=employee.id,
            employee_name=employee.name,
            gross_salary=gross_salary,
        )
