from Stack import Stack
from tokenization import tokenizer, valid_token
from typing import List, Union

def postfix_evaluator(postfix_tokens: List[str]) -> int:
    """Evaluate a postfix expression represented as a list of tokens.

    Args:
        postfix_tokens (List[str]): A list of tokens representing a postfix expression. 
                                    Each token can be an operand (e.g., "2", "3") or an 
                                    operator (e.g., "+", "*").

    Returns:
        int: The result of evaluating the postfix expression.

    Example:
        >>> postfix_evaluator(["2", "3", "*", "4", "+"])
        10
        >>> postfix_evaluator(["5", "6", "7", "+", "*"])
        65
    """
    operand_stk = Stack()
    
    for token in postfix_tokens:
        if token in "*/+-^": 
            if operand_stk.size() < 2:
                raise ValueError("Invalid Postfix Expression: Not enough " + 
                                 "operands for operator.")
                
            right_operand = operand_stk.pop()
            left_operand = operand_stk.pop()
            
            # Use a match-case statement to handle different operators
            match token: 
                case "*": result = left_operand * right_operand
                case "-": result = left_operand - right_operand
                case "+": result = left_operand + right_operand
                case "/": 
                    if right_operand == 0:
                        raise ValueError("Division by zero is not allowed.")
                    result = left_operand / right_operand
                case "^": result = left_operand ** right_operand  
                
            operand_stk.push(result)
        else:
            operand_stk.push(int(token))
    
    # After processing all tokens, the stack should contain exactly one result
    if operand_stk.size() != 1:
        raise ValueError("Invalid Postfix Expression: Too many operands left.")
    
    return operand_stk.pop()


def evaluate_postfix_expression(postfix_expression: str) -> Union[float, int]:
    """Evaluate a given postfix expression and return the result.

    Args:
        postfix_expression (str): A valid postfix expression in string format, 
                                  e.g., "1 35 2 * +".

    Returns:
        Union[float, int]: The result of evaluating the postfix expression, 
                           e.g., for "1 35 2 * +", the result is 71.

    Example:
        >>> evaluate_postfix_expression("2 3 * 4 +")
        10
        >>> evaluate_postfix_expression("5 6 7 + *")
        65
    """
    postfix_tokens = tokenizer(postfix_expression)
    
    # Validate that all tokens are valid and check for no parentheses or variables
    if all(valid_token(token=token, 
                       match_variables=False, 
                       match_paranthesis=False) for token in postfix_tokens):
        return postfix_evaluator(postfix_tokens)
    else:
        raise ValueError("Invalid Postfix Expression: One or more tokens are invalid.")


# Testing
assert evaluate_postfix_expression("2 3 + 4 *") == 20, "Expected result of (2 + 3) * 4 to be 20 (Basic arithmetic test for addition and multiplication)"
assert evaluate_postfix_expression("10 5 - 2 /") == 2.5, "Expected result of (10 - 5) / 2 to be 2.5 (Test for subtraction and division)"
assert evaluate_postfix_expression("5") == 5, "Expected result of single operand '5' to be 5 (Edge case with only one operand)"

try:
    evaluate_postfix_expression("5 0 /")
except ValueError as e:
    assert str(e) == "Division by zero is not allowed.", "Division by zero error message mismatch (Handling division by zero)"

try:
    evaluate_postfix_expression("5 +")
except ValueError as e:
    assert str(e) == "Invalid Postfix Expression: Not enough operands for operator.", "Invalid expression error message mismatch (Not enough operands)"

assert evaluate_postfix_expression("3 4 + 2 * 5 -") == 9, "Expected result of ((3 + 4) * 2) - 5 to be 11 (Complex expression with multiple operations)"

try:
    evaluate_postfix_expression("3 A +")
except ValueError as e:
    assert str(e) == "Invalid Postfix Expression: One or more tokens are invalid.", "Invalid token error message mismatch (Invalid token in the expression)"

assert evaluate_postfix_expression("2 3 ^ 4 *") == 32, "Expected result of (2 ^ 3) * 4 to be 64 (Testing power operator in postfix expression)"

try:
    evaluate_postfix_expression("")
except ValueError as e:
    assert str(e) == "Invalid Postfix Expression: Too many operands left.", "Empty expression error message mismatch (Empty expression handling)"

assert evaluate_postfix_expression("3 4 + 2 * 5 - 6 +") == 15, "Expected result of ((3 + 4) * 2 - 5) + 6 to be 11 (Complex expression with multiple operations and parentheses)"

try:
    evaluate_postfix_expression("3 4 + *")
except ValueError as e:
    assert str(e) == "Invalid Postfix Expression: Not enough operands for operator.", "Too many operators error message mismatch (Invalid postfix expression with too many operators)"

assert evaluate_postfix_expression("2 3 ^ 4 2 ^ ^ 6 3 ^ 5 2 ^ * + 7 +") == 281474976716063, "Failed in dual power"