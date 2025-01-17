from typing import Any

class Node:
    """A class representing a node in a doubly linked list."""
    def __init__(self, item: Any = None, 
                 next: 'Node' = None,
                 prev: 'Node' = None): 
        """
        Initializes a new Node.

        Args:
            item (Any): The data to store in the node.
            next (Node): A reference to the next node in the list (default is None).
            prev (Node): A reference to the previous node in the list (default is None).
        """
        self.data = item
        self.next = next
        self.prev = prev
