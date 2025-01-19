from typing import Any
from LinkedList import LinkedList
from Node import Node

class UnorderedList(LinkedList): 
    """A class that implements an unordered linked list, inheriting from the LinkedList class.
    
    Operations: remove, search, is_empty, size, append, index, insert, pop
                add, insert
    """
    def __init__(self): 
        super().__init__()


    def add(self, item: Any) -> None: 
        """Adds an item to the beginning of the list.
        
        Arg: 
            item (Any): The item to insert.
        """
        self.insert(0, item)
        
    
    def append(self, item: Any) -> None: 
        """Adds an item to the end of the list.
        
        Arg: 
            item (Any): The item to insert.
        """
        self.insert(self.size(), item)


    def insert(self, index: int = 0, item: Any = None) -> None:
        """
        Inserts an item at a specific index in the list. If the index is negative,
        it is treated as counting from the end of the list.
        
        Args:
            item (Any): The item to insert.
            index (int): The index to insert at (default is 0).
        """
        # Adjust negative index to a valid position
        if index < 0:
            index = self.size() + index if index >= -self.size() else 0

        if index == 0:  # Insert at the head
            new_node = Node(item, self.head)
            
            if self.head:  # If list is not empty, update previous head's prev pointer
                self.head.prev = new_node
            
            self.head = new_node
            
            if self.tail is None:  # If the list was empty
                self.tail = new_node
                
        elif index == self.size():  # Insert at the tail
            new_node = Node(item, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node
            
        else:  # Insert at the middle
            current = self.head
            position = 0
            while current and position != index:
                current = current.next
                position += 1

            prev_node = current.prev
            new_node = Node(item, current, prev_node)
            prev_node.next = new_node
            current.prev = new_node

        self.count += 1  # Increment the size of the list

# Create the LinkedList object
ll = UnorderedList()

# Add elements to the linked list
for i in range(1, 11):
    ll.append(i)

# Test single index access
assert ll[0] == 1, "Test failed: Expected 1 at index 0"
assert ll[5] == 6, "Test failed: Expected 6 at index 5"
assert ll[-1] == 10, "Test failed: Expected 10 at index -1"
assert ll[-2] == 9, "Test failed: Expected 9 at index -2"

# Test out-of-range indices
try:
    ll[11]
except IndexError:
    pass  # Expected to raise IndexError

try:
    ll[-11]
except IndexError:
    pass  # Expected to raise IndexError

# Test slicing (start:stop)
assert ll[2:5] == [3, 4, 5], "Test failed: Expected [3, 4, 5] for slice 2:5"
assert ll[0:3] == [1, 2, 3], "Test failed: Expected [1, 2, 3] for slice 0:3"

# Test slicing with reverse order (start > stop)
# assert ll[5:2] == [6, 5, 4], "Test failed: Expected [6, 5, 4] for slice 5:2"

# Test slicing with negative indices
assert ll[-5:-2] == [6, 7, 8], "Test failed: Expected [6, 7, 8] for slice -5:-2"

# The below is a very important corner case.
assert ll[-2:-5] == [9, 8, 7, 6], "Test failed: Expected [9, 8, 7, 6] for slice -2:-5"

# Test empty list
empty_ll = LinkedList()
assert empty_ll[0:2] == [], "Test failed: Expected empty list for slice 0:2 on empty list"