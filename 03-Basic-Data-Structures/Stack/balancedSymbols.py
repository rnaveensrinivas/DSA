from Stack import Stack

CLOSING_SYMBOLS = {
    ")": "(",
    "}": "{",
    "]": "[",
}

def symbol_balance_checker(symbol_string: str) -> bool: 
    """Checks if parentheses, braces, and brackets are balanced in the input string."""
    
    stk = Stack()
    for symbol in symbol_string: 
        if symbol in CLOSING_SYMBOLS.values(): # opening symbol
            stk.push(symbol) 
        elif symbol in CLOSING_SYMBOLS:
            if stk.is_empty() or stk.peek() != CLOSING_SYMBOLS[symbol]:
                return False
            else:
                stk.pop()
    
    return stk.is_empty()


assert_error_message = "Logical error in symbol_balance_checker()"

# Balanced cases
assert (symbol_balance_checker("()")) == True, assert_error_message
assert (symbol_balance_checker("()[]{}")) == True, assert_error_message
assert (symbol_balance_checker("([{}])")) == True, assert_error_message
assert (symbol_balance_checker("({[]})")) == True, assert_error_message
assert (symbol_balance_checker("({[()()]})")) == True, assert_error_message
assert (symbol_balance_checker("{[()]}")) == True, assert_error_message
assert (symbol_balance_checker("")) == True, assert_error_message  # Empty string is trivially balanced

# Unbalanced cases
assert (symbol_balance_checker("(()")) == False, assert_error_message
assert (symbol_balance_checker("((())")) == False, assert_error_message
assert (symbol_balance_checker("({[})")) == False, assert_error_message
assert (symbol_balance_checker("([)]")) == False, assert_error_message
assert (symbol_balance_checker("((())]")) == False, assert_error_message
assert (symbol_balance_checker("({[()]}")) == False, assert_error_message
assert (symbol_balance_checker("(()))")) == False, assert_error_message
assert (symbol_balance_checker(")(")) == False, assert_error_message

# Strings with no symbols
assert (symbol_balance_checker("a+b=c")) == True, assert_error_message  # No symbols should be balanced
assert (symbol_balance_checker("abc")) == True, assert_error_message  # No symbols should be balanced

# Strings with only one type of symbol
assert (symbol_balance_checker("((()))")) == True, assert_error_message
assert (symbol_balance_checker("[[]]")) == True, assert_error_message
assert (symbol_balance_checker("{()}")) == True, assert_error_message
assert (symbol_balance_checker("(((((")) == False, assert_error_message
assert (symbol_balance_checker("[[[[[]]]]")) == False, assert_error_message
assert (symbol_balance_checker("{((()))")) == False, assert_error_message

# Mixed symbols
assert (symbol_balance_checker("{[()()]}")) == True, assert_error_message
assert (symbol_balance_checker("{[()]}{}")) == True, assert_error_message
assert (symbol_balance_checker("([{}()])")) == True, assert_error_message
