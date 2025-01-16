from Queue import Queue
from typing import List

def hot_potato(names: List[str], num: int) -> str:
    """Simulates the children's game hot potato.
    
    Args:
        names: List of people participating in the game.
        num: The count that determines who gets eliminated.

    Returns:
        The name of the last remaining person.
    """
    
    q = Queue()
    for name in names:
        q.enqueue(name)
        
    while q.size() != 1: 
        
        # rotate the queue by 'num' steps
        for _ in range(num): 
            q.enqueue(q.dequeue())
        
        # Eliminate the person at the end of 'num' steps
        q.dequeue()
        
    return q.dequeue() # return the last member in queue


# Case 1: Basic test with 6 players, elimination count 7
assert hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7) == "Susan"

# Case 2: Only 1 person, should return that person
assert hot_potato(["Bill"], 7) == "Bill"

# Case 3: Case with fewer players than the elimination number (elimination count 5)
assert hot_potato(["Bill", "David", "Susan", "Jane"], 5) == "Susan"

# Case 4: Small number of players, simple elimination
assert hot_potato(["Alice", "Bob", "Charlie"], 2) == "Bob"

# Case 5: Larger number of players, elimination count 3
assert hot_potato(["John", "Paul", "George", "Ringo", "Mick", "Keith", "Charlie"], 3) == "Paul"

# Case 6: Edge case where the elimination number equals number of players
assert hot_potato(["Anna", "Elsa", "Olaf"], 3) == "Elsa"

# Case 7: Test with elimination number being 1 (rotate and eliminate each one sequentially)
assert hot_potato(["A", "B", "C", "D"], 1) == "A"
