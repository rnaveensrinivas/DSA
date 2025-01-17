from typing import Any
from Queue import Queue

class QueueWithRearAtStartOfList(Queue):
    """Queue implementation as a list.
    Assuming front is at index -1 and rear is at index 0.
    
    Operations: enqueue, dequeue, size, and is_empty.
    """
    def __init__(self) -> None:
        """Initialize the queue with an empty list and _counter variable with 0."""
        super().__init__()

    def enqueue(self, item: Any) -> None:
        """Add the given item to the back of the queue."""
        self._items.insert(0, item)
        
    def dequeue(self) -> Any:
        """Remove and return the front element from the queue."""
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue.")
        return self._items.pop()