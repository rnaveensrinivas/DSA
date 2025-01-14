from Stack import Stack
from typing import List
from tokenization import tokenizer, valid_token
from simpleBalancedParantheses import simple_parentheses_checker
import re

PRECEDENCE = {
    "(": 0,
    ")": 0,
    "-": 1, 
    "+": 1, 
    "*": 2, 
    "/": 2,
    "^": 3,  
}


def valid_infix_expression(infix_tokens: List[str]) -> bool:
    """Validate whether a given list of tokens represents a syntactically correct infix expression.

    Args:
        infix_tokens (List[str]): A list of tokens in infix notation. 
                                  Tokens may include numbers, operators (+, -, *, /, ^), and parentheses.

    Returns:
        bool: True if the infix expression is valid, otherwise False.

    Example:
        >>> valid_infix_expression(['3', '+', '(', '5', '*', '2', ')'])
        True
        >>> valid_infix_expression(['3', '+', '*', '5'])
        False

    Validation Criteria:
        - Parentheses must be balanced and properly nested.
        - Operators (+, -, *, /, ^) must appear between valid operands.
        - The expression must not start or end with an operator.
        - Consecutive operators are not allowed.
        - Each operand and operator must be correctly positioned.

    Notes:
        - This function assumes that the input is already tokenized.
        - Numeric tokens can include integers or floating-point numbers.
    """
    # Check for balanced parentheses
    if not simple_parentheses_checker("".join(infix_tokens)):
        raise ValueError("Invalid parentheses usage in the expression! Make sure parentheses are balanced.")

    # Check if all tokens are valid
    if not all(valid_token(token) for token in infix_tokens):
        raise ValueError("The expression contains invalid tokens! Only numbers, variables, operators, and parentheses are allowed.")
    
    # Ensure valid token transitions
    prev_token_type = None
    for token in infix_tokens: 
        if re.fullmatch(r"[0-9]+", token):
            current_token_type = "Number"
        elif re.fullmatch(r"[a-zA-Z]+", token):
            current_token_type = "Identifier"
        elif token in "*+/^-": 
            current_token_type = "Operator"
        elif token == "(": 
            current_token_type = "Opening Parenthesis"
        elif token == ")": 
            current_token_type = "Closing Parenthesis"
            
        # Check if expression starts with an operator
        if prev_token_type is None and current_token_type == "Operator":
            raise ValueError("Expression cannot start with an operator! An operator must follow a valid operand or parenthesis.")
            
        # Check if a closing parenthesis is immediately after an operator
        if current_token_type == "Closing Parenthesis" and prev_token_type == "Operator":
            raise ValueError("A closing parenthesis cannot follow an operator directly! Check for misplaced parentheses.")

        # Check if an operator follows an opening parenthesis
        if current_token_type == "Operator" and prev_token_type == "Opening Parenthesis":
            raise ValueError("An operator cannot follow an opening parenthesis! Operators must follow numbers or identifiers.")

        # Check for empty parentheses (e.g., ())
        if current_token_type == "Closing Parenthesis" and prev_token_type == "Opening Parenthesis":
            raise ValueError("Empty parentheses are not allowed! Ensure there is an expression inside the parentheses.")
        
        # Check for consecutive tokens of the same type
        if (current_token_type != "Opening Parenthesis" and 
            current_token_type != "Closing Parenthesis" and 
            prev_token_type == current_token_type):
            raise ValueError(f"Invalid expression: Consecutive {current_token_type.lower()}s are not allowed! Tokens like numbers, operators, or parentheses must be properly separated.")
        
        prev_token_type = current_token_type
    
    # Check if expression ends with an operator
    if current_token_type == "Operator":
        raise ValueError("Expression cannot end with an operator! The expression should end with a number, identifier, or closing parenthesis.")
    
    return True
    
    
def infix_to_postfix(infix_tokens: List[str]) -> List[str]:
    """Convert an infix expression (in tokenized form) to postfix (Reverse Polish Notation).

    Args:
        infix_tokens (List[str]): A list of tokens representing an infix expression. 
                                  Tokens may include numbers, operators (+, -, *, /, ^), and parentheses.

    Returns:
        List[str]: A list of tokens representing the expression in postfix notation.

    Example:
        >>> infix_to_postfix(['3', '+', '(', '5', '*', '2', ')'])
        ['3', '5', '2', '*', '+']

    Conversion Rules:
        - Operands (numbers) are placed directly into the output.
        - Operators are pushed onto a stack, but operators with higher precedence are placed before those with lower precedence.
        - Parentheses are handled by pushing left parentheses onto the stack and popping the stack until a right parenthesis is encountered.
        - At the end of the expression, any remaining operators on the stack are popped to the output.

    Notes:
        - This function assumes that the input is already tokenized into individual elements (numbers, operators, parentheses).
        - The precedence of operators is typically defined as:
          - `^` > `*` = `/` > `+` = `-`
        - Parentheses are used to indicate precedence grouping, and are not included in the output.
    """
    postfix_tokens = []
    stk = Stack()
    
    for token in infix_tokens: 
        if token == "(": 
            stk.push(token)
        elif token == ")": 
            
            while not stk.is_empty() and stk.peek() != "(": 
                postfix_tokens.append(stk.pop())
                
            if stk.is_empty():
                raise ValueError("Unmatched closing parenthesis in expression!")
            
            stk.pop() # removing the top element, "("
                
        elif token in "*/+-^": 
            
            while (not stk.is_empty() and 
                   (PRECEDENCE[stk.peek()] > PRECEDENCE[token] or 
                    (PRECEDENCE[stk.peek()] == PRECEDENCE[token] and token != "^"))):
                postfix_tokens.append(stk.pop())
                
            stk.push(token)
        else: # character or number
            postfix_tokens.append(token)
    
    while not stk.is_empty(): 
        if stk.peek() == "(": 
            raise ValueError("Unmatched opening parenthesis in expression!")
        postfix_tokens.append(stk.pop())
        
    return postfix_tokens


def convert_infix_to_postfix(expression: str) -> str:
    """Convert an infix expression to a postfix expression.

    Args:
        expression (str): A string representing the infix expression, containing numbers, operators 
                           (+, -, *, /, ^), and parentheses. Operators and operands are separated by spaces.

    Returns:
        str: The resulting postfix expression as a string, with operators and operands in the correct postfix order.

    Example:
        >>> convert_infix_to_postfix('3 + (5 * 2)')
        '3 5 2 * +'

    Algorithm:
        - Operands (numbers) are added directly to the output.
        - Operators are pushed onto a stack and placed in the output based on precedence and parenthesis rules.
        - Parentheses dictate operator precedence. Left parentheses are pushed onto the stack and right parentheses
          cause operators to be popped from the stack until the matching left parenthesis is found.
        - At the end of the expression, any remaining operators on the stack are popped to the output.

    Precedence:
        - Operators (`^`)  >  (`*` = `/`)  >  (`+` = `-`)
    
    Notes:
        - The function assumes valid infix notation, and that operands and operators are space-separated.
        - Parentheses are used for grouping and are not part of the output.

    """
    if expression == "":
        return ""
    infix_tokens = tokenizer(expression)
    if valid_infix_expression(infix_tokens):
        return " ".join(infix_to_postfix(infix_tokens))
    else:
        raise ValueError("Expression given is invalid!")


# Testing
assert valid_infix_expression(["x", "+", "y"]) == True, "Failed for valid expression 'x + y'"
assert valid_infix_expression(["1", "+", "2", "*", "var"]) == True, "Failed for valid expression '1 + 2 * var'"
assert valid_infix_expression(["(", "x", "+", "y", ")"]) == True, "Failed for valid expression '(x + y)'"
assert valid_infix_expression(["A", "+", "B", "*", "C"]) == True, "Test 1 Failed"
try:
    valid_infix_expression(["+", "A", "*", "B"])
except ValueError as e:
    assert str(e) == "Expression cannot start with an operator! An operator must follow a valid operand or parenthesis.", "Test 2 Failed"

try:
    valid_infix_expression(["(", "A", "+", "B", "*", ")"])
except ValueError as e:
    assert str(e) == "A closing parenthesis cannot follow an operator directly! Check for misplaced parentheses.", "Test 3 Failed"

try:
    valid_infix_expression(["(", "+", "A", ")"])
except ValueError as e:
    assert str(e) == "An operator cannot follow an opening parenthesis! Operators must follow numbers or identifiers.", "Test 4 Failed"

try:
    valid_infix_expression(["(", ")"])
except ValueError as e:
    assert str(e) == "Empty parentheses are not allowed! Ensure there is an expression inside the parentheses.", "Test 5 Failed"

try:
    valid_infix_expression(["1", "2", "3"])
except ValueError as e:
    assert str(e) == "Invalid expression: Consecutive numbers are not allowed! Tokens like numbers, operators, or parentheses must be properly separated.", "Test 6 Failed"

assert valid_infix_expression(["(", "A", "+", "B", ")", "*", "C"]) == True, "Test 7 Failed"

try:
    valid_infix_expression(["A", "+", "B", "*"])
except ValueError as e:
    assert str(e) == "Expression cannot end with an operator! The expression should end with a number, identifier, or closing parenthesis.", "Test 8 Failed"

assert valid_infix_expression(["(", "(", "A", "+", "B", ")", "*", "C", ")", "-", "D"]) == True, "Test 9 Failed"

try:
    valid_infix_expression(["(", "A", "+", "B", "*", "C", ")"])
except ValueError as e:
    assert str(e) == "Invalid parentheses usage in the expression! Make sure parentheses are balanced.", "Test 10 Failed"

try:
    valid_infix_expression(["A", "+", "*", "B"])
except ValueError as e:
    assert str(e) == "Invalid expression: Consecutive operators are not allowed! Tokens like numbers, operators, or parentheses must be properly separated.", "Test 11 Failed"

assert infix_to_postfix(tokenizer("1 + 2")) == ["1", "2", "+"], "Failed for simple addition: 1 + 2"
assert infix_to_postfix(tokenizer("A+B*C")) == ["A", "B", "C", "*", "+"], "Failed for simple addition and multiplication: A+B*C"
assert infix_to_postfix(tokenizer("(A+B)*C")) == ["A", "B", "+", "C", "*"], "Failed for parentheses with precedence: (A+B)*C"
assert infix_to_postfix(tokenizer("((A+B)*C)-D")) == ["A", "B", "+", "C", "*", "D", "-"], "Failed for nested parentheses: ((A+B)*C)-D"
assert infix_to_postfix(tokenizer("A+B*C-D/E")) == ["A", "B", "C", "*", "+", "D", "E", "/", "-"], "Failed for multiple operators with precedence: A+B*C-D/E"
assert infix_to_postfix(tokenizer("A")) == ["A"], "Failed for single operand: A"
assert infix_to_postfix(tokenizer("A+B*C/D-E^F")) == ["A", "B", "C", "*", "D", "/", "+", "E", "F", "^", "-"], "Failed for complex expression with all operators: A+B*C/D-E^F"
assert infix_to_postfix(tokenizer("A*(B+C*D)-E/F")) == ["A", "B", "C", "D", "*", "+", "*", "E", "F", "/", "-"], "Failed for parentheses altering precedence: A*(B+C*D)-E/F"
assert infix_to_postfix(tokenizer("A^B^C")) == ["A", "B", "C", "^", "^"], "Failed for power operator precedence: A^B^C"
assert infix_to_postfix(tokenizer("(A+(B*C))^D")) == ["A", "B", "C", "*", "+", "D", "^"], "Failed for multiple parentheses: (A+(B*C))^D"
assert infix_to_postfix(tokenizer("")) == [], "Failed for empty input"
assert infix_to_postfix(tokenizer("  A + B * C  ")) == ["A", "B", "C", "*", "+"], "Failed for whitespace handling: '  A + B * C  '"
assert infix_to_postfix(tokenizer("(((A+B)*C)+D)/E")) == ["A", "B", "+", "C", "*", "D", "+", "E", "/"], "Failed for complex deeply nested parentheses: (((A+B)*C)+D)/E"

assert convert_infix_to_postfix("A + B * C") == "A B C * +", "Expected 'ABC*+' for 'A + B * C'"
assert convert_infix_to_postfix("(A + B) * C") == "A B + C *", "Expected 'AB+C*' for '(A + B) * C'"
assert convert_infix_to_postfix("((A + B) * C) - D") == "A B + C * D -", "Expected 'AB+C*D-' for '((A + B) * C) - D'"
assert convert_infix_to_postfix("A + B * C - D / E") == "A B C * + D E / -", "Expected 'ABC*+DE/-' for 'A + B * C - D / E'"
assert convert_infix_to_postfix("A") == "A", "Expected 'A' for single operand 'A'"
assert convert_infix_to_postfix("A + B * C / D - E ^ F") == "A B C * D / + E F ^ -", "Expected 'ABC*D/+EF^-' for 'A + B * C / D - E ^ F'"
assert convert_infix_to_postfix("A * (B + C * D) - E / F") == "A B C D * + * E F / -", "Expected 'ABCD*+*EF/-' for 'A * (B + C * D) - E / F'"
assert convert_infix_to_postfix("A ^ B ^ C") == "A B C ^ ^", "Expected 'ABC^^' for 'A ^ B ^ C'"
assert convert_infix_to_postfix("(A + (B * C)) ^ D") == "A B C * + D ^", "Expected 'ABC*+D^' for '(A + (B * C)) ^ D'"
assert convert_infix_to_postfix("") == "", "Expected '' for empty input"
assert convert_infix_to_postfix("  A + B * C  ") == "A B C * +", "Expected 'ABC*+' for '  A + B * C  ' with whitespace"
assert convert_infix_to_postfix("(((A + B) * C) + D) / E") == "A B + C * D + E /", "Expected 'AB+C*D+E/' for '(((A + B) * C) + D) / E'"
assert convert_infix_to_postfix("A - B") == "A B -", "Expected 'AB-' for 'A - B'"
try:
    convert_infix_to_postfix("A + + B")
except ValueError as e:
    assert str(e) == "Invalid expression: Consecutive operators are not allowed! Tokens like numbers, operators, or parentheses must be properly separated.", "Expected 'Consecutive operators are not allowed!' error"

try:
    convert_infix_to_postfix("A + B @ C")
except ValueError as e:
    assert str(e) == "The expression contains invalid tokens! Only numbers, variables, operators, and parentheses are allowed.", "Expected 'Invalid token' error for '@' in 'A + B @ C'"

try:
    convert_infix_to_postfix("( + A )")
except ValueError as e:
    assert str(e) == "An operator cannot follow an opening parenthesis! Operators must follow numbers or identifiers.", "Expected 'Operator after opening parenthesis' error for '( + A )'"

try:
    convert_infix_to_postfix("A + ) B")
except ValueError as e:
    assert str(e) == "Invalid parentheses usage in the expression! Make sure parentheses are balanced.", "Expected 'Operator before closing parenthesis' error for 'A + ) B'"

try:
    convert_infix_to_postfix("(A + B * C")
except ValueError as e:
    assert str(e) == "Invalid parentheses usage in the expression! Make sure parentheses are balanced.", "Expected 'Mismatched parentheses' error for '(A + B * C'"

assert convert_infix_to_postfix("(A + B) ^ C") == "A B + C ^", "Expected 'AB+C^' for '(A + B) ^ C'"
assert convert_infix_to_postfix("A + (B * C) - (D / E) ^ F") == "A B C * + D E / F ^ -", "Expected 'ABC*+DE/F^-' for 'A + (B * C) - (D / E) ^ F'"
assert convert_infix_to_postfix("((A + B) * (C - D) / E) + F^G - H * (I + J) / (K - L)") == "A B + C D - * E / F G ^ + H I J + * K L - / -", "Failed for complex expression."