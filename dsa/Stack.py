from typing import Any
from UnorderedList import UnorderedList

class Stack:
    """Stack implementation as a Doubly Linked List.
    
    Operations: push, pop, peek, is_empty, size.
    """
    
    def __init__(self) -> None:
        """Create a new stack."""
        self._items = UnorderedList()
        
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._items) == 0
    
    def push(self, item: Any) -> None:
        """Add an item to the stack."""
        self._items.append(item)
        
    def pop(self) -> Any:
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("Pop from empty stack.")
        return self._items.pop()
    
    def peek(self) -> Any:
        """Return the top item of the stack without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty stack.")
        return self._items[-1]
        
    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)
    
    
# Create a stack instance
stack = Stack()

# Test is_empty on a new stack
assert stack.is_empty() == True, "Stack should be empty initially."

# Test size on a new stack
assert stack.size() == 0, "Size of the stack should be 0 initially."

# Test push operation
stack.push(10)
assert stack.is_empty() == False, "Stack should not be empty after pushing an item."
assert stack.size() == 1, "Size of the stack should be 1 after one push."
assert stack.peek() == 10, "Peek should return the last pushed item (10)."

stack.push(20)
assert stack.size() == 2, "Size of the stack should be 2 after two pushes."
assert stack.peek() == 20, "Peek should return the last pushed item (20)."

# Test pop operation
assert stack.pop() == 20, "Pop should return the last pushed item (20)."
assert stack.size() == 1, "Size of the stack should be 1 after one pop."
assert stack.peek() == 10, "Peek should now return the remaining item (10)."

assert stack.pop() == 10, "Pop should return the last remaining item (10)."
assert stack.is_empty() == True, "Stack should be empty after popping all items."

# Test pop on an empty stack
try:
    stack.pop()
    assert False, "Pop on empty stack should raise IndexError."
except IndexError:
    pass

# Test peek on an empty stack
try:
    stack.peek()
    assert False, "Peek on empty stack should raise IndexError."
except IndexError:
    pass

