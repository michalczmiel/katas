from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Employee:
    id: str
    name: str
    annual_gross: Decimal


@dataclass
class SalarySlip:
    employee_id: str
    employee_name: str
    gross_salary: Decimal


class SalarySlipGenerator:
    def generate_for(self, employee: Employee) -> SalarySlip:
        return SalarySlip(
            employee_id=employee.id,
            employee_name=employee.name,
            gross_salary=employee.annual_gross,
        )
