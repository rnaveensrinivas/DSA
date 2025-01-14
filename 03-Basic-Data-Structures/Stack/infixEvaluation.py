from infixToPostfix import convert_infix_to_postfix
from postfixEvaluation import evaluate_postfix_expression
from typing import Union

def infix_evaluator(infix_expression: str) -> Union[int, float]:
    """
    Convert an infix expression to postfix and evaluate it.
    
    Args:
        infix_expression (str): The infix expression as a string.
    
    Returns:
        Union[int, float]: The result of evaluating the postfix expression.
    """
    try:
        # Convert infix to postfix
        postfix_expression = convert_infix_to_postfix(infix_expression)
        
        # Evaluate the postfix expression
        return evaluate_postfix_expression(postfix_expression)
    except Exception as e:
        raise ValueError(f"Error processing expression '{infix_expression}': {e}")

# Valid expressions
assert infix_evaluator("3 + 4") == 7, "Simple addition failed"
assert infix_evaluator("10 + 2 * 6") == 22, "Operator precedence failed"
assert infix_evaluator("100 * 2 + 12") == 212, "Mixed precedence failed"
assert infix_evaluator("(100 * (2 + 12)) / 14") == 100, "Parentheses handling failed"
assert infix_evaluator("50 / (5 * (2 + 3))") == 2, "Nested parentheses failed"

# Edge cases
assert infix_evaluator("42") == 42, "Single operand failed"
assert infix_evaluator("1 + 0") == 1, "Addition with zero failed"
assert infix_evaluator("0 * 100") == 0, "Multiplication by zero failed"
assert infix_evaluator("0 / 1") == 0, "Division of zero failed"
assert infix_evaluator("1 / 1") == 1, "Division by one failed"

# Complex cases
assert infix_evaluator("3 + 4 * 2 / (1 - 5) ^ 2 ^ 3") == 3.0001220703125, "Complex precedence and power failed"
assert infix_evaluator("(6 + (3 * 2)) / (1 + 1)") == 6, "Deeply nested parentheses failed"

# Error handling
try:
    infix_evaluator("")  # Empty string
except ValueError as e:
    assert str(e).startswith("Error processing expression"), "Empty expression handling failed"

try:
    infix_evaluator("3 + ")  # Incomplete expression
except ValueError as e:
    assert str(e).startswith("Error processing expression"), "Incomplete expression handling failed"

try:
    infix_evaluator("3 + a")  # Invalid characters
except ValueError as e:
    assert str(e).startswith("Error processing expression"), "Invalid character handling failed"
