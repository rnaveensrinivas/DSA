from typing import Any
from UnorderedList import UnorderedList

class Queue:
    """Queue implementation as a doubly.
    Assuming front is at index 0 and rear is at index -1.
    
    Operations: enqueue, dequeue, size, and is_empty.
    """

    def __init__(self) -> None:
        """Initialize the queue with an empty list and _counter variable with 0."""
        self._items = UnorderedList()
        
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._items) == 0
    
    def enqueue(self, item: Any) -> None:
        """Add the given item to the back of the queue."""
        self._items.append(item)
        # if rear at start of list
        # self._items.insert(0, item)
        
    def dequeue(self) -> Any:
        """Remove and return the front element from the queue."""
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue.")
        return self._items.pop(0)
        # if front at end of list
        # return self._items.pop()
    
    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self._items)
    
    

# Create a queue instance
queue = Queue()

# Test is_empty on a new queue
assert queue.is_empty() == True, "Queue should be empty initially."

# Test size on a new queue
assert queue.size() == 0, "Size of the queue should be 0 initially."

# Test enqueue operation
queue.enqueue(10)
assert queue.is_empty() == False, "Queue should not be empty after enqueuing an item."
assert queue.size() == 1, "Size of the queue should be 1 after one enqueue."

queue.enqueue(20)
queue.enqueue(30)
assert queue.size() == 3, "Size of the queue should be 3 after three enqueues."

# Test dequeue operation
assert queue.dequeue() == 10, "Dequeue should return the first enqueued item (10)."
assert queue.size() == 2, "Size of the queue should be 2 after one dequeue."

assert queue.dequeue() == 20, "Dequeue should return the next enqueued item (20)."
assert queue.size() == 1, "Size of the queue should be 1 after another dequeue."

assert queue.dequeue() == 30, "Dequeue should return the last enqueued item (30)."
assert queue.is_empty() == True, "Queue should be empty after dequeuing all items."

# Test dequeue on an empty queue
try:
    queue.dequeue()
    assert False, "Dequeue on an empty queue should raise ValueError."
except ValueError:
    pass

# Test enqueue and dequeue with multiple types
queue.enqueue("string")
queue.enqueue(42)
queue.enqueue(3.14)
queue.enqueue({"key": "value"})

assert queue.size() == 4, "Size of the queue should be 4 after enqueuing multiple items."
assert queue.dequeue() == "string", "Dequeue should return the first enqueued item ('string')."
assert queue.dequeue() == 42, "Dequeue should return the next enqueued item (42)."
assert queue.dequeue() == 3.14, "Dequeue should return the next enqueued item (3.14)."
assert queue.dequeue() == {"key": "value"}, "Dequeue should return the last enqueued item (dictionary)."
assert queue.is_empty() == True, "Queue should be empty after dequeuing all items."

# Test enqueue after emptying the queue
queue.enqueue(100)
queue.enqueue(200)
assert queue.size() == 2, "Size of the queue should be 2 after enqueuing items again."
assert queue.dequeue() == 100, "Dequeue should return the first item enqueued after resetting (100)."
assert queue.dequeue() == 200, "Dequeue should return the second item enqueued after resetting (200)."
assert queue.is_empty() == True, "Queue should be empty again after dequeuing all items."

