from Stack import Stack

def simple_parentheses_checker(symbol_string: str) -> bool:
    """Checks if all the parantheses are balanced in given code fragment."""
    
    stk = Stack()
    
    for symbol in symbol_string: 
        if symbol == "(": 
            stk.push(symbol)
        elif symbol == ")": 
            if stk.is_empty():
                return False
            else:
                stk.pop()
            
    return stk.is_empty()

assert_error_message = "Logical error in simple_parentheses_checker()"

assert (simple_parentheses_checker("()")) == True, assert_error_message
assert (simple_parentheses_checker("((())())")) == True, assert_error_message
assert (simple_parentheses_checker("((())")) == False, assert_error_message
assert (simple_parentheses_checker(")(")) == False, assert_error_message
assert (simple_parentheses_checker("")) == True, assert_error_message
assert (simple_parentheses_checker("()()()")) == True, assert_error_message
assert (simple_parentheses_checker("(()())")) == True, assert_error_message
assert (simple_parentheses_checker("((())()")) == False, assert_error_message
assert (simple_parentheses_checker("(()())()")) == True, assert_error_message


            
     