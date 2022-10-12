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

  Scenario Outline: For annual gross salary largre than £100,000.00
    Given I have an employee John J Doe with an annual gross salary of "<annual gross salary>"
    When I generate a monthly salary slip for the employee
    Then the monthly salary slip should contain the below:
      """
      Employee ID: 12345
      Employee Name: John J Doe
      Gross Salary: <gross salary>
      National Insurance contributions: <insurance>
      Tax-free allowance: <tax free allowance>
      Taxable income: <taxable income>
      Tax Payable: <tax payable>
      """

    Examples:
      | annual gross salary | gross salary | insurance | tax free allowance | taxable income | tax payable |
      | £101,000.00         | £8,416.67    | £446.07   | £875.00            | £7,541.67      | £2,483.33   |
      | £111,000.00         | £9,250.00    | £462.73   | £458.33            | £8,791.67      | £2,983.33   |
      | £122,000.00         | £10,166.67   | £481.07   | £0.00              | £10,166.67     | £3,533.33   |
      | £150,000.00         | £12,500.00   | £527.73   | £0.00              | £12,500.00     | £4,466.67   |
