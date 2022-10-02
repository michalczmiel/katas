from behave import given, when, then


@given("I have an employee {name} with an annual gross salary of {gross_salary}")
def step_impl(context, name, gross_salary):
    raise NotImplementedError(
        "STEP: Given I have an employee John J Doe with an annual gross salary of £5,000.00"
    )


@when("I generate a monthly salary slip for the employee")
def step_impl(context):
    raise NotImplementedError(
        "STEP: When I generate a monthly salary slip for the employee"
    )


@then("the monthly salary slip should contain the below")
def step_impl(context):
    raise NotImplementedError(
        "STEP: Then the monthly salary slip should contain the below"
    )
