from typing import Any
from UnorderedList import UnorderedList

class Deque: 
    def __init__(self) -> None: 
        """Initalize Deque using Doubly Linked List.
        Assuming front is at index 0 and rear at index -1. 
        
        Operations: add_front, add_rear, pop_front, pop_rear, is_empty, size
        """
        self._items = UnorderedList()
        
    def is_empty(self) -> int: 
        """Check if the Deque is empty"""
        return len(self._items) == 0
    
    def add_front(self, item: Any) -> None: 
        """Remove an item from the front of the deque"""
        self._items.insert(0, item)
        
    def add_rear(self, item: Any) -> None: 
        """Add an item to the rear of the deque"""
        self._items.append(item)
        
    def pop_front(self) -> Any: 
        """Remove the item at front of Deque."""
        return self._items.pop(0)
        
    def pop_rear(self) -> Any: 
        """Remove an item from the rear of the deque"""
        return self._items.pop()
    
    def size(self) -> None: 
        """Get the number of items in the deque"""
        return len(self._items)
        
# Create a deque instance
deque = Deque()

# Test is_empty on a new deque
assert deque.is_empty() == True, "Deque should be empty initially."

# Test size on a new deque
assert deque.size() == 0, "Size of the deque should be 0 initially."

# Test add_front operation
deque.add_front(10)
assert deque.is_empty() == False, "Deque should not be empty after adding an item."
assert deque.size() == 1, "Size of the deque should be 1 after adding an item to the front."
assert deque.pop_front() == 10, "pop_front should return the item added to the front."

# Test add_rear operation
deque.add_rear(20)
assert deque.size() == 1, "Size of the deque should be 1 after adding an item to the rear."
assert deque.pop_rear() == 20, "pop_rear should return the item added to the rear."

# Test add_front and add_rear together
deque.add_front(30)
deque.add_rear(40)
assert deque.size() == 2, "Size of the deque should be 2 after adding items to front and rear."
assert deque.pop_front() == 30, "pop_front should return the item added to the front."
assert deque.pop_rear() == 40, "pop_rear should return the item added to the rear."

# Test multiple operations
deque.add_rear(50)
deque.add_rear(60)
deque.add_front(40)
deque.add_front(30)
assert deque.size() == 4, "Size of the deque should be 4 after multiple additions."
assert deque.pop_front() == 30, "pop_front should return the first front item added (30)."
assert deque.pop_rear() == 60, "pop_rear should return the last rear item added (60)."
assert deque.size() == 2, "Size of the deque should be 2 after two pops."
assert deque.pop_front() == 40, "pop_front should return the next front item (40)."
assert deque.pop_rear() == 50, "pop_rear should return the next rear item (50)."
assert deque.is_empty() == True, "Deque should be empty after popping all items."

# Test pop on an empty deque
try:
    deque.pop_front()
    assert False, "pop_front on an empty deque should raise IndexError."
except IndexError:
    pass

try:
    deque.pop_rear()
    assert False, "pop_rear on an empty deque should raise IndexError."
except IndexError:
    pass

