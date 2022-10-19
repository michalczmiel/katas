from decimal import Decimal, getcontext

getcontext().prec = 16


class TaxCalculator:
    max_tax_allowance = Decimal(11000)
    tax_rate = Decimal(0.20)
    higher_max_tax_allowance = Decimal(43000)
    higher_tax_rate = Decimal(0.40)

    def calculate_annual_taxable_income(self, annual_gross: Decimal) -> Decimal:
        annual_tax_allowance = self.calculate_annual_tax_free_allowance(annual_gross)

        return annual_gross - annual_tax_allowance

    def calculate_annual_tax_free_allowance(self, annual_gross: Decimal) -> Decimal:
        if annual_gross > self.max_tax_allowance:
            return self.max_tax_allowance
        else:
            return annual_gross

    def _calculate_annual_higher_taxable_income(self, annual_gross: Decimal) -> Decimal:
        if annual_gross < self.higher_max_tax_allowance:
            return Decimal(0)

        annual_taxable_income = annual_gross - self.higher_max_tax_allowance

        return annual_taxable_income

    def _calculate_annual_normal_taxable_income(self, annual_gross: Decimal) -> Decimal:
        annual_tax_allowance = self.calculate_annual_tax_free_allowance(annual_gross)

        if annual_gross <= annual_tax_allowance:
            return Decimal(0)

        if annual_gross > self.higher_max_tax_allowance:
            maximum_taxable_income = self.higher_max_tax_allowance
        else:
            maximum_taxable_income = annual_gross

        annual_taxable_income = maximum_taxable_income - annual_tax_allowance

        return annual_taxable_income

    def calculate_annual_tax_payable(self, annual_gross: Decimal) -> Decimal:
        higher_taxable_income = self._calculate_annual_higher_taxable_income(
            annual_gross
        )
        normal_taxable_income = self._calculate_annual_normal_taxable_income(
            annual_gross
        )

        return (
            normal_taxable_income * self.tax_rate
            + higher_taxable_income * self.higher_tax_rate
        )


class NationalInsuranceCalculator:
    insurance_contribution_minimum_annual_gross = Decimal(8060)
    insurance_contribution_rate = Decimal(0.12)
    higher_insurance_contribution_minimum_annual_gross = Decimal(43000)
    higher_insurance_contribution_rate = Decimal(0.02)

    def _calculate_higher_national_insurance_contribution(
        self, annual_gross: Decimal
    ) -> Decimal:
        if annual_gross < self.higher_insurance_contribution_minimum_annual_gross:
            return Decimal(0)

        annual_taxable_amount = (
            annual_gross - self.higher_insurance_contribution_minimum_annual_gross
        )

        return annual_taxable_amount * self.higher_insurance_contribution_rate

    def _calculate_normal_national_insurance_contribution(
        self, annual_gross: Decimal
    ) -> Decimal:
        if annual_gross < self.insurance_contribution_minimum_annual_gross:
            return Decimal(0)

        if annual_gross > self.higher_insurance_contribution_minimum_annual_gross:
            maximum_taxable_income = (
                self.higher_insurance_contribution_minimum_annual_gross
            )
        else:
            maximum_taxable_income = annual_gross

        taxable_amount = (
            maximum_taxable_income - self.insurance_contribution_minimum_annual_gross
        )

        return taxable_amount * self.insurance_contribution_rate

    def calculate_annual_national_insurance_contribution(
        self, annual_gross: Decimal
    ) -> Decimal:
        normal_contribution = self._calculate_normal_national_insurance_contribution(
            annual_gross
        )
        higher_contribution = self._calculate_higher_national_insurance_contribution(
            annual_gross
        )

        return normal_contribution + higher_contribution


class SalarySlipCalculator:
    months_in_year = Decimal(12)

    def __init__(
        self,
        national_insurance_calculator: NationalInsuranceCalculator,
        tax_calculator: TaxCalculator,
    ) -> None:
        self._national_insurance_calculator = national_insurance_calculator
        self._tax_calculator = tax_calculator

    def calculate_national_insurance_contribution(
        self, annual_gross: Decimal
    ) -> Decimal:
        return (
            self._national_insurance_calculator.calculate_annual_national_insurance_contribution(
                annual_gross
            )
            / self.months_in_year
        )

    def calculate_taxable_income(self, annual_gross: Decimal) -> Decimal:
        return (
            self._tax_calculator.calculate_annual_taxable_income(annual_gross)
            / self.months_in_year
        )

    def calculate_tax_free_allowance(self, annual_gross: Decimal) -> Decimal:
        return (
            self._tax_calculator.calculate_annual_tax_free_allowance(annual_gross)
            / self.months_in_year
        )

    def calculate_tax_payable(self, annual_gross: Decimal) -> Decimal:
        return (
            self._tax_calculator.calculate_annual_tax_payable(annual_gross)
            / self.months_in_year
        )

    def calculate_gross_salary(self, annual_gross: Decimal) -> Decimal:
        return annual_gross / self.months_in_year
