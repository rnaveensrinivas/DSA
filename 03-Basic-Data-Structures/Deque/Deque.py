from typing import Any

class Deque: 
    def __init__(self) -> None: 
        """Initalize Deque using list data structure.
        Assuming front is at index 0 and rear at index -1. 
        
        Operations: add_front, add_rear, pop_front, pop_rear, is_empty, size
        """
        self._items = []
        
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
        