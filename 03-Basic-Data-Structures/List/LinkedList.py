from typing import Any

class LinkedList:
    """A class representing a doubly linked list.
    
    Operations: remove, search, is_empty, size, append, index, insert, pop
    """

    def __init__(self):
        """Initializes an empty linked list with no head, tail, and a count of 0."""
        self.head = None
        self.tail = None
        self.count = 0


    def is_empty(self) -> bool:
        """Checks if the linked list is empty.
        
        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self.head is None


    def size(self) -> int:
        """Returns the number of elements in the linked list.
        
        Returns:
            int: The number of elements in the list.
        """
        return self.count


    def __len__(self) -> int:
        """Returns the number of elements in the linked list.
        
        Returns:
            int: The number of elements in the list.
        """
        return self.size()


    def search(self, item: Any) -> bool:
        """Searches for an item in the linked list.
        
        Args:
            item (Any): The item to search for in the list.
        
        Returns:
            bool: True if the item is found, False otherwise.
        """
        try:
            self.index(item)  # Try to find the index of the item
            return True
        except ValueError:
            return False


    def index(self, item: Any) -> int:
        """Finds the index of an item in the linked list.
        
        Args:
            item (Any): The item whose index to find.
        
        Raises:
            ValueError: If the item is not found in the list.
        
        Returns:
            int: The index of the item in the list.
        """
        current = self.head
        position = 0
        while current and current.data != item:
            current = current.next
            position += 1

        if not current:
            raise ValueError(f"{item} is not in list")  # Item not found
        return position


    def remove(self, item: Any) -> None:
        """Removes an item from the linked list.
        
        Args:
            item (Any): The item to remove from the list.
        
        Raises:
            ValueError: If the item is not found in the list.
        """
        current = self.head
        position = 0
        while current and current.data != item:
            current = current.next
            position += 1

        if not current:
            raise ValueError(f"{item} not found!")  # Item not found
        else:
            self.pop(position)  # Remove the item by its index


    def pop(self, index: int = 0) -> Any:
        """Removes and returns the element at the specified index in the linked list.
        
        Args:
            index (int): The index (default is 0) of the element to pop.
        
        Raises:
            IndexError: If the index is out of range or the list is empty.
        
        Returns:
            Any: The data of the removed node.
        """
        # Handle the case where the list is empty
        if self.is_empty():
            raise IndexError("Cannot pop from empty list.")

        # Check if index is valid (within the range)
        if not (0 <= index < self.size() or -self.size() <= index < 0):
            raise IndexError(f"{index} is out of range.")

        # Convert negative index to positive
        if index < 0:
            index = self.size() + index

        position = 0
        current = self.head

        # Removing from the head of the list
        if index == 0:
            self.head = self.head.next
            if self.head is None:  # If the list becomes empty
                self.tail = None
            else:
                self.head.prev = None
        else:
            # Traverse to the node at the specified index
            while current and position != index:
                current = current.next
                position += 1

            # Removing from the tail of the list
            if current == self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
            else:  # Removing from the middle
                prev_node = current.prev
                next_node = current.next
                prev_node.next = next_node
                next_node.prev = prev_node

        self.count -= 1  # Decrease the count of the list
        return current.data  # Return the data of the removed node


    def __str__(self):
        """Returns a string representation of the linked list.
        
        Returns:
            str: A string representing the linked list (e.g., "1->2->3").
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))  # Collect the data of each node
            current = current.next
        return "->".join(nodes)  # Join the data as a string with arrows
