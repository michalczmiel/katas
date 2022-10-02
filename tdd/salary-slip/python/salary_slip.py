import re
from dataclasses import dataclass
from decimal import Decimal, getcontext
from typing import List, Union

from babel.numbers import parse_decimal, format_currency


getcontext().prec = 16


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


@dataclass
class SalarySlip:
    employee_id: str
    employee_name: str
    gross_salary: Decimal
    national_insurance_contribution: Decimal
    tax_free_allowance: Decimal
    taxable_income: Decimal
    tax_payable: Decimal

    def _format_value(
        self, value: Decimal, currency: str = "GBP", locale="en_GB"
    ) -> str:
        return format_currency(value, currency=currency, locale=locale)

    def __str__(self) -> str:
        formatter = SalarySlipFormatter()

        formatter.add("Employee ID", self.employee_id)
        formatter.add("Employee Name", self.employee_name)
        formatter.add("Gross Salary", self.gross_salary)
        formatter.add(
            "National Insurance contributions", self.national_insurance_contribution
        )
        formatter.add("Tax-free allowance", self.tax_free_allowance)
        formatter.add("Taxable income", self.taxable_income)
        formatter.add("Tax Payable", self.tax_payable)

        return formatter.format()


class SalarySlipCalculator:
    months_in_year = Decimal(12)
    insurance_contribution_minimum_annual_gross = Decimal(8060)
    insurance_contribution_rate = Decimal(0.12)
    max_tax_allowance = Decimal(11000)
    tax_rate = Decimal(0.20)

    def _should_pay_national_insurance_contributions(
        self, annual_gross: Decimal
    ) -> bool:
        return annual_gross > self.insurance_contribution_minimum_annual_gross

    def _is_income_taxable(self, annual_gross: Decimal) -> bool:
        return annual_gross > self.max_tax_allowance

    def calculate_national_insurance_contribution(
        self, annual_gross: Decimal
    ) -> Decimal:
        if not self._should_pay_national_insurance_contributions(annual_gross):
            return Decimal(0)

        taxable_amount = annual_gross - self.insurance_contribution_minimum_annual_gross

        return taxable_amount * self.insurance_contribution_rate / self.months_in_year

    def calculate_taxable_income(self, annual_gross: Decimal) -> Decimal:
        if not self._is_income_taxable(annual_gross):
            return Decimal(0)

        annual_taxable_income = annual_gross - self.max_tax_allowance

        return annual_taxable_income / self.months_in_year

    def calculate_tax_free_allowance(self, annual_gross: Decimal) -> Decimal:
        if not self._is_income_taxable(annual_gross):
            return Decimal(0)

        return self.max_tax_allowance / self.months_in_year

    def calculate_tax_payable(self, annual_gross: Decimal) -> Decimal:
        taxable_income = self.calculate_taxable_income(annual_gross)

        return taxable_income * self.tax_rate

    def calculate_gross_salary(self, annual_gross: Decimal) -> Decimal:
        return annual_gross / self.months_in_year


class SalarySlipGenerator:
    def generate_for(self, employee: Employee) -> SalarySlip:
        calculator = SalarySlipCalculator()

        return SalarySlip(
            employee_id=employee.id,
            employee_name=employee.name,
            gross_salary=calculator.calculate_gross_salary(employee.annual_gross),
            national_insurance_contribution=calculator.calculate_national_insurance_contribution(
                employee.annual_gross
            ),
            tax_free_allowance=calculator.calculate_tax_free_allowance(
                employee.annual_gross
            ),
            tax_payable=calculator.calculate_tax_payable(employee.annual_gross),
            taxable_income=calculator.calculate_taxable_income(employee.annual_gross),
        )
