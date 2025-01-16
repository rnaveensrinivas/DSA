from typing import Any

class Queue:
    """Queue implementation as a list.
    Assuming front is at index 0 and rear is at index -1.
    
    Operations: enqueue, dequeue, size, and is_empty.
    """

    def __init__(self) -> None:
        """Initialize the queue with an empty list and _counter variable with 0."""
        self._items = []
        
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._items) == 0
    
    def enqueue(self, item: Any) -> None:
        """Add the given item to the back of the queue."""
        self._items.append(item)
        
    def dequeue(self) -> Any:
        """Remove and return the front element from the queue."""
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue.")
        return self._items.pop(0)
    
    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self._items)