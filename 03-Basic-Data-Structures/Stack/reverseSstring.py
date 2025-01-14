from Stack import Stack

def reverse_string(string: str) -> str:
    """Reverses the input string using stack."""
    stk = Stack()
    
    # Push all characters into stack
    for char in string: 
        stk.push(char)
        
    # Pop all the items and form the reversed string
    return "".join(stk.pop() for _ in range(stk.size()))

assert "racecar" == reverse_string("racecar"), "Logical error in reverse_string()"
assert "neevan" == reverse_string("naveen"), "Logical error in reverse_string()"
assert "a" == reverse_string("a"), "Logical error in reverse_string()"