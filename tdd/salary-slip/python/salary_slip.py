import re
from dataclasses import dataclass
from decimal import Decimal, getcontext
from typing import Optional

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


@dataclass
class SalarySlip:
    employee_id: str
    employee_name: str
    gross_salary: Decimal
    national_insurance_contribution: Optional[Decimal]
    tax_free_allowance: Decimal
    taxable_income: Decimal
    tax_payable: Decimal

    def _format_value(
        self, value: Decimal, currency: str = "GBP", locale="en_GB"
    ) -> str:
        return format_currency(value, currency=currency, locale=locale)

    def __str__(self) -> str:
        lines = [
            f"Employee ID: {self.employee_id}",
            f"Employee Name: {self.employee_name}",
            f"Gross Salary: {self._format_value(self.gross_salary)}",
            f"National Insurance contributions: {self._format_value(self.national_insurance_contribution)}"
            if self.national_insurance_contribution
            else None,
            f"Tax-free allowance: {self._format_value(self.tax_free_allowance)}"
            if self.tax_free_allowance
            else None,
            f"Taxable income: {self._format_value(self.taxable_income)}"
            if self.taxable_income
            else None,
            f"Tax Payable: {self.tax_payable}" if self.tax_payable else None,
        ]

        return "\n".join(filter(bool, lines))


class SalarySlipCalculator:
    months_in_year = Decimal(12)
    insurance_contribution_minimum_annual_gross = Decimal(8060)
    insurance_contribution_rate = Decimal(0.12)
    max_tax_allowance = Decimal(11000)

    @classmethod
    def should_pay_national_insurance_contributions(
        self, annual_gross: Decimal
    ) -> bool:
        return annual_gross > self.insurance_contribution_minimum_annual_gross

    @classmethod
    def calculate_national_insurance_contribution(
        cls, annual_gross: Decimal
    ) -> Decimal:
        taxable_amount = annual_gross - cls.insurance_contribution_minimum_annual_gross

        return taxable_amount * cls.insurance_contribution_rate / cls.months_in_year

    @classmethod
    def calculate_taxable_income(cls, annual_gross: Decimal) -> Decimal:
        if annual_gross < cls.max_tax_allowance:
            return Decimal(0)

        annual_taxable_income = annual_gross - cls.max_tax_allowance

        return annual_taxable_income / cls.months_in_year

    @classmethod
    def calculate_tax_free_allowance(cls, annual_gross: Decimal) -> Decimal:
        return Decimal(0)

    @classmethod
    def calculate_tax_payable(cls, annual_gross: Decimal) -> Decimal:
        return Decimal(0)

    @classmethod
    def calculate_gross_salary(cls, annual_gross: Decimal) -> Decimal:
        return annual_gross / cls.months_in_year


class SalarySlipGenerator:
    def generate_for(self, employee: Employee) -> SalarySlip:
        gross_salary = SalarySlipCalculator.calculate_gross_salary(
            employee.annual_gross
        )

        should_pay_national_insurance_contributions = (
            SalarySlipCalculator.should_pay_national_insurance_contributions(
                employee.annual_gross
            )
        )

        national_insurance_contribution = (
            SalarySlipCalculator.calculate_national_insurance_contribution(
                employee.annual_gross
            )
            if should_pay_national_insurance_contributions
            else None
        )

        tax_free_allowance = SalarySlipCalculator.calculate_tax_free_allowance(
            employee.annual_gross
        )

        taxable_income = SalarySlipCalculator.calculate_taxable_income(
            employee.annual_gross
        )

        tax_payable = SalarySlipCalculator.calculate_tax_payable(employee.annual_gross)

        return SalarySlip(
            employee_id=employee.id,
            employee_name=employee.name,
            gross_salary=gross_salary,
            national_insurance_contribution=national_insurance_contribution,
            tax_free_allowance=tax_free_allowance,
            tax_payable=tax_payable,
            taxable_income=taxable_income,
        )
