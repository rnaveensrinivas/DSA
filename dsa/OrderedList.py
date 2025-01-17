from typing import Any
from LinkedList import LinkedList
from Node import Node

class OrderedList(LinkedList): 
    """A class that implements an ordered linked list, inheriting from the LinkedList class.
    
    Operations: remove, search, is_empty, size, append, index, insert, pop
                add
    """
    def __init__(self): 
        super().__init__()

    def add(self, item: Any) -> None: 
        """
        Adds an item to the ordered linked list while maintaining the sorted order.

        Args:
            item (Any): The item to insert into the list. It is assumed that the list
                        supports comparison between elements to determine the order.
        """
        new_node = Node(item)
        
        # Case 1: Empty list
        if not self.head: 
            self.head = self.tail = new_node
            return
        
        # Traverse the list to find the correct position
        current = self.head
        while current and current.data < item: 
            current = current.next
        
        # Case 2: Insert at the tail (end of the list)
        if not current: 
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            # Case 3: Insert in the middle or at the head
            new_node.next = current
            new_node.prev = current.prev
            if current.prev:
                current.prev.next = new_node
            else:
                # If current is the head, update the head
                self.head = new_node
            current.prev = new_node
