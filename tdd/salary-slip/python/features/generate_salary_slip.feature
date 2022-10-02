Feature: Generate salary slip

  Scenario: For annual gross salary of £5,000.00
    Given I have an employee John J Doe with an annual gross salary of £5,000.00
    When I generate a monthly salary slip for the employee
    Then the monthly salary slip should contain the below:
      """
      Employee ID: 12345
      Employee Name: John J Doe
      Gross Salary: £416.67
      """

  Scenario: For annual gross salary of £9,060.00
    Given I have an employee John J Doe with an annual gross salary of £9,060.00
    When I generate a monthly salary slip for the employee
    Then the monthly salary slip should contain the below:
      """
      Employee ID: 12345
      Employee Name: John J Doe
      Gross Salary: £755.00
      National Insurance contributions: £10.00
      """

  Scenario: For annual gross salary of £12,000.00
    Given I have an employee John J Doe with an annual gross salary of £12,000.00
    When I generate a monthly salary slip for the employee
    Then the monthly salary slip should contain the below:
      """
      Employee ID: 12345
      Employee Name: John J Doe
      Gross Salary: £1,000.00
      National Insurance contributions: £39.40
      Tax-free allowance: £916.67
      Taxable income: £83.33
      Tax Payable: £16.67
      """

  Scenario: For annual gross salary of £45,000.00
    Given I have an employee John J Doe with an annual gross salary of 45,000.00
    When I generate a monthly salary slip for the employee
    Then the monthly salary slip should contain the below:
      """
      Employee ID: 12345
      Employee Name: John J Doe
      Gross Salary: £3,750.00
      National Insurance contributions: £352.73
      Tax-free allowance: £916.67
      Taxable income: £2,833.33
      Tax Payable: £600.00
      """
