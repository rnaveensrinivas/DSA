class Dictionary: 
    def __init__(self): 
        """
        Initializes an empty dictionary with a prime number size for the hash table.
        The hash table has two arrays: one for keys (self.slots) and one for values (self.data).
        """
        self.size = 11  # Any prime number suffices
        self.slots = [None] * self.size  # Holds keys
        self.data = [None] * self.size  # Holds values

    def _hash_function(self, key, size): 
        """
        Computes the hash value for a given key based on the provided table size.

        Parameters:
        key: The key to hash.
        size: The size of the hash table.

        Returns:
        The computed hash value.
        """
        return key % size
    
    def _rehash(self, old_hash, size): 
        """
        Computes the next slot in the hash table using linear probing.

        Parameters:
        old_hash: The hash value of the current slot.
        size: The size of the hash table.

        Returns:
        The next slot index computed using linear probing.
        """
        return (old_hash + 1) % size
    
    def put(self, key, data): 
        """
        Adds a key-value pair to the dictionary. If the key already exists, 
        its value is updated. Uses linear probing to resolve collisions.

        Parameters:
        key: The key to store in the dictionary.
        data: The associated value to store.
        """
        hash_pos = self._hash_function(key, self.size)
        
        # If the slot is empty, insert the key and data
        if self.slots[hash_pos] is None: 
            self.slots[hash_pos] = key
            self.data[hash_pos] = data
            
        elif self.slots[hash_pos] == key: 
            self.data[hash_pos] = data
        else: 
            next_slot = self._rehash(hash_pos, self.size)  # Correct rehashing
            while self.slots[next_slot] is not None and self.slots[next_slot] != key: 
                next_slot = self._rehash(next_slot, self.size)  # Update based on last slot
                if next_slot == hash_pos:  # If we loop back to the original position, table is full
                    raise RuntimeError("Dictionary is full.")
            
            # Inserting the key and data at the found slot
            self.slots[next_slot] = key
            self.data[next_slot] = data
    
    def get(self, key): 
        """
        Retrieves the value associated with a given key.

        Parameters:
        key: The key whose associated value is to be retrieved.

        Returns:
        The value associated with the key.

        Raises:
        ValueError: If the key is not found in the dictionary.
        """
        hash_pos = self._hash_function(key, self.size)
        
        # If key is at the hash position, return the data
        if self.slots[hash_pos] == key: 
            return self.data[hash_pos]
        
        else: 
            next_slot = self._rehash(hash_pos, self.size)
            while self.slots[next_slot] is not None and self.slots[next_slot] != key: 
                next_slot = self._rehash(next_slot, self.size)
                if next_slot == hash_pos:  # If we loop back to the original position, key doesn't exist
                    raise ValueError("Key doesn't exist.")
            
            if self.slots[next_slot] is None: 
                raise ValueError("Key doesn't exist.")
            elif self.slots[next_slot] == key: 
                return self.data[next_slot]

    def __getitem__(self, key):
        """
        Retrieves the value associated with the given key using the `[]` syntax.

        Parameters:
        key: The key whose associated value is to be retrieved.

        Returns:
        The value associated with the key.
        """
        return self.get(key)

    def __setitem__(self, key, data):
        """
        Adds or updates the key-value pair in the dictionary using the `[]` syntax.

        Parameters:
        key: The key to store in the dictionary.
        data: The associated value to store.
        """
        self.put(key, data)
        
    def __str__(self) -> str: 
        return f"Slots: {self.slots}\nValue: {self.data}"

# Create a new Dictionary object
my_dict = Dictionary()

# Add key-value pairs to the dictionary using the put method
my_dict.put(1, "apple")
my_dict.put(2, "banana")
my_dict.put(3, "cherry")

# Assert retrieval of values using the get method
assert my_dict.get(1) == "apple", "Test failed for key 1"
assert my_dict.get(2) == "banana", "Test failed for key 2"
assert my_dict.get(3) == "cherry", "Test failed for key 3"

# Add/update key-value pair using the __setitem__ method (square brackets)
my_dict[4] = "date"
assert my_dict[4] == "date", "Test failed for key 4"

# Update an existing key using the __setitem__ method (square brackets)
my_dict[2] = "blueberry"
assert my_dict[2] == "blueberry", "Test failed for key 2 after update"

# Retrieve a value using the __getitem__ method (square brackets)
assert my_dict[3] == "cherry", "Test failed for key 3"

# Try to get a value for a key that doesn't exist, expect ValueError
try:
    my_dict.get(5)
    assert False, "Test failed, expected ValueError for key 5"
except ValueError as e:
    assert str(e) == "Key doesn't exist.", f"Test failed with error message: {str(e)}"

# Try to get a value for a key that doesn't exist using square brackets, expect ValueError
try:
    my_dict[5]
    assert False, "Test failed, expected ValueError for key 5"
except ValueError as e:
    assert str(e) == "Key doesn't exist.", f"Test failed with error message: {str(e)}"

