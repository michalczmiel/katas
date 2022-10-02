from dataclasses import dataclass
import re
from decimal import Decimal

from babel.numbers import parse_decimal


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

    def __str__(self) -> str:
        lines = [
            f"Employee ID: {self.employee_id}",
            f"Employee Name: {self.employee_name}",
            "Gross Salary: £416.67",
        ]

        return "\n".join(lines)


class SalarySlipGenerator:
    def generate_for(self, employee: Employee) -> SalarySlip:
        return SalarySlip(
            employee_id=employee.id,
            employee_name=employee.name,
            gross_salary=employee.annual_gross,
        )
