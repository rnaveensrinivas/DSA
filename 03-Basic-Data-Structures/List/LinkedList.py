from typing import Any, List, Union
from Node import Node

class LinkedList:
    """A class representing a doubly linked list.
    
    Operations: remove, search, is_empty, size, append, index, insert, pop
    """

    def __init__(self) -> None:
        """Initializes an empty linked list with no head, tail, and a count of 0."""
        self.head : Node = None
        self.tail : Node = None
        self.count : int = 0


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


    def pop(self, index: int = -1) -> Any:
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


    def _get_list_items(self) -> List[Node]: 
        """Return a list of nodes in the linked list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(current)  # Collect the nodes themselves
            current = current.next
        return nodes


    def _stringify(self, 
                   nodes: List[Node], 
                   start: str = "[", 
                   end: str = "]", 
                   separator: str = ", ") -> str:
        """Return a string representation of the nodes with custom formatting."""
        # Join the string representation of node data with the separator
        node_data = separator.join(str(node.data) for node in nodes)
        return f"{start}{node_data}{end}"


    def __str__(self) -> str:
        """Returns a string representation of the linked list with arrows."""
        nodes = self._get_list_items()
        return self._stringify(nodes, start="Head | ", end=" | Ground", separator=" -> ")


    def __repr__(self) -> str:
        """Returns a detailed representation of the linked list."""
        nodes = self._get_list_items()
        return self._stringify(nodes, start="[", end="]", separator=", ")
    
    def __getitem__(self, index: Union[int, slice] = 0) -> Union[Any, List[Any]]:
        """
        Retrieve an item by its index in the linked list.

        This method supports both direct indexing and slicing, allowing access
        to elements by index or a range of elements.

        Args:
            index (Union[int, slice]): The index of the item to retrieve, or a slice 
                                        object for a range of items.
                                        - If an integer is provided, it retrieves the 
                                        element at that index.
                                        - If a slice object is provided, it returns a 
                                        list of elements from the start to the stop index 
                                        (inclusive of start, exclusive of stop).

        Returns:
            Union[Any, List[Any]]:
                - If an integer index is provided, returns the element at that index.
                - If a slice object is provided, returns a list of elements from the 
                linked list within the specified range.

        Raises:
            IndexError: If the index is out of range.
        
        Example:
            >>> ll = LinkedList()
            >>> for i in range(1, 11):
            >>>     ll.append(i)
            >>> ll[2]
            3
            >>> ll[2:5]
            [3, 4, 5]
        """
        if isinstance(index, int): 
            # Check if index is valid (within the range)
            if not (0 <= index < self.size() or -self.size() <= index < 0):
                raise IndexError(f"{index} is out of range.")
            
            if index == -1: 
                return self.tail.data
            
            if index == 0: 
                return self.head.data
            
            if index < 0:
                index = self.size() + index

            position = 0
            current = self.head
            
            while current and position != index: 
                current = current.next
                position += 1
                
            return current.data
        else: # Handle slicing
            
            if index.step: 
                raise NotImplementedError
             
            start = index.start
            stop = index.stop
            
            # Edge case
            if start > 0 and stop > 0 and start > stop: 
                return []
                        
            if start < 0:
                start = self.size() + start
            
            if stop < 0: 
                stop = self.size() + stop
                
            starting_index = min(start, stop)
            ending_index = max(start, stop)
            
            position = 0
            current = self.head
            items = []
            
            while current and position < starting_index: 
                current = current.next
                position += 1
                
            if not current or not current.next: 
                return items
            
            while current and position <= ending_index: 
                items.append(current.data)
                current = current.next
                position += 1
                
            return items[:-1] if start < stop else items[::-1]
            # ll[-2:-5] == [9, 8, 7, 6] "<=" in while and [-1] - corner case