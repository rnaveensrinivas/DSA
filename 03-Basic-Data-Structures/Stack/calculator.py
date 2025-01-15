from infixEvaluation import infix_evaluator

opening_prompt = """Welcome to the interactive calculator
An expression can contain
- paranthesis: '(' and ')'
- operators: '+`, `-`, `/`, `^`, and '*'
- operands: Only numerical, for example, '23'

Example:
>>> 1 + 2 * 3
7

Expression can span multiple lines using the line continuation character '\\'
Example:\n>>> 1 + 2 * \\
... 3
7

To quit - type 'exit'
---- ---- ---- ----
"""

def get_input() -> str:
    """Handles multi-line user input."""
    input_list = []
    ip = input(">>> ")
    
    while ip[-1] == "\\":
        input_list.append(ip[:-1])
        ip = input("... ")
    
    input_list.append(ip)
            
    return "".join(input_list)
        
    
def interactive_calculator() -> None:
    """Interactive calculator loop."""
    print(opening_prompt)
    while True: 
        
        expression = get_input()
        if expression.lower() == "exit": 
            break
        
        try:
            result = infix_evaluator(expression)
            print(result)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception as e:
            print(f"Error evaluating expression: {e}")
            
if __name__ == "__main__": 
    interactive_calculator()