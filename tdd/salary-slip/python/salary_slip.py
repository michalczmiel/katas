import re
from dataclasses import dataclass
from decimal import Decimal

from babel.numbers import parse_decimal, format_currency

from calculators import SalarySlipCalculator, TaxCalculator, NationalInsuranceCalculator
from formatters import SalarySlipFormatter


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


class SalarySlipGenerator:
    def generate_for(self, employee: Employee) -> SalarySlip:
        calculator = SalarySlipCalculator(
            national_insurance_calculator=NationalInsuranceCalculator(),
            tax_calculator=TaxCalculator(),
        )

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
