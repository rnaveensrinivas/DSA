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
        self.insert(item, 0)
        
    
    def append(self, item: Any) -> None: 
        """Adds an item to the end of the list.
        
        Arg: 
            item (Any): The item to insert.
        """
        self.insert(item, self.size())


    def insert(self, item: Any, index: int = 0) -> None:
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
