Feature: Generate salary slip

  Scenario: For annual salary of £5,000.00
    Given I have an employee John J Doe with an annual gross salary of £5,000.00
    When I generate a monthly salary slip for the employee
    Then the monthly salary slip should contain the below:
      """
      Employee ID: 12345
      Employee Name: John J Doe
      Gross Salary: £416.67
      """

  Scenario: For annual salary of £9,060.00
    Given I have an employee John J Doe with an annual gross salary of £9,060.00
    When I generate a monthly salary slip for the employee
    Then the monthly salary slip should contain the below:
      """
      Employee ID: 12345
      Employee Name: John J Doe
      Gross Salary: £755.00
      National Insurance contributions: £10.00
      """