"""Step definitions for calculator feature."""
from behave import given, when, then


class Calculator:
    """Simple calculator class."""
    
    def __init__(self):
        self.result = 0
    
    def add(self, a, b):
        """Add two numbers."""
        self.result = a + b
        return self.result
    
    def subtract(self, a, b):
        """Subtract b from a."""
        self.result = a - b
        return self.result
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        self.result = a * b
        return self.result
    
    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.result = a / b
        return self.result


@given('I have a calculator')
def step_given_calculator(context):
    """Initialize calculator."""
    context.calculator = Calculator()


@when('I add {a:d} and {b:d}')
def step_when_add(context, a, b):
    """Add two numbers."""
    context.calculator.add(a, b)


@when('I subtract {b:d} from {a:d}')
def step_when_subtract(context, a, b):
    """Subtract two numbers."""
    context.calculator.subtract(a, b)


@when('I multiply {a:d} by {b:d}')
def step_when_multiply(context, a, b):
    """Multiply two numbers."""
    context.calculator.multiply(a, b)


@when('I divide {a:d} by {b:d}')
def step_when_divide(context, a, b):
    """Divide two numbers."""
    context.calculator.divide(a, b)


@then('the result should be {expected:d}')
def step_then_result(context, expected):
    """Verify the result."""
    assert context.calculator.result == expected, \
        f"Expected {expected}, got {context.calculator.result}"
