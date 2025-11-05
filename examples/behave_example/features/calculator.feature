Feature: Calculator
  As a user
  I want to perform basic arithmetic operations
  So that I can calculate results

  Scenario: Add two numbers
    Given I have a calculator
    When I add 2 and 3
    Then the result should be 5

  Scenario: Subtract two numbers
    Given I have a calculator
    When I subtract 3 from 10
    Then the result should be 7

  Scenario: Multiply two numbers
    Given I have a calculator
    When I multiply 4 by 5
    Then the result should be 20

  Scenario: Divide two numbers
    Given I have a calculator
    When I divide 20 by 4
    Then the result should be 5

  Scenario Outline: Add multiple numbers
    Given I have a calculator
    When I add <a> and <b>
    Then the result should be <result>

    Examples:
      | a  | b  | result |
      | 1  | 1  | 2      |
      | 5  | 10 | 15     |
      | -1 | 1  | 0      |
