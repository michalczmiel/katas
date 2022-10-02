from behave import given, when, then

from salary_slip import SalarySlipGenerator, Employee


@given("I have an employee {name} with an annual gross salary of {annual_gross}")
def step_impl(context, name, annual_gross):
    employee = Employee(id="12345", name=name, annual_gross=annual_gross)

    context.employee = employee


@when("I generate a monthly salary slip for the employee")
def step_impl(context):
    generator = SalarySlipGenerator()

    salary_slip = generator.generate_for(context.employee)

    context.salary_slip = salary_slip


@then("the monthly salary slip should contain the below")
def step_impl(context):
    assert context.text == str(context.salary_slip)
