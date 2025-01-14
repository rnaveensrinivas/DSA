from typing import Any

class Stack:
    """Stack implementation as a list.
    
    Operations: push, pop, peek, is_empty, size.
    """
    
    def __init__(self) -> None:
        """Create a new stack."""
        self._items = []
        self._count = 0
        
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return self._count == 0
    
    def push(self, item: Any) -> None:
        """Add an item to the stack."""
        self._items.append(item)
        self._count += 1
        
    def pop(self) -> Any:
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("Pop from empty stack.")
        self._count -= 1
        return self._items.pop()
    
    def peek(self) -> Any:
        """Return the top item of the stack without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty stack.")
        return self._items[-1]
        
    def size(self) -> int:
        """Return the number of items in the stack."""
        return self._count