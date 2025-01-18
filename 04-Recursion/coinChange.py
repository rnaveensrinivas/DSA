from typing import List

def num_coins(change: int, coin_types: List[int]) -> int:
    """
    Compute the minimum number of coins needed to make the given change.

    Args:
        change (int): The amount of change to make.
        coin_types (List[int]): A list of available coin denominations.

    Returns:
        int: The minimum number of coins needed to make the change.
    """
    # Base case: If no change is required, no coins are needed
    if change == 0: 
        return 0
    
    # Initialize minimum coins to infinity for comparison
    min_coins = float("inf")
    
    # Iterate through each coin denomination
    for coin_type in coin_types:
        if coin_type <= change:  # Ensure the coin type does not exceed the current change
            # Recursively compute the number of coins for the remaining change
            min_coins = min(min_coins, 1 + num_coins(change - coin_type, 
                                                     coin_types))
        
    return min_coins
from typing import List

def num_coins_memo(change: int, 
                   coin_types: List[int], 
                   known_results: List[int]) -> int:
    """
    Compute the minimum number of coins needed to make the given change using memoization.

    Args:
        change (int): The amount of change to make.
        coin_types (List[int]): A list of available coin denominations.
        known_results (List[int]): A memoization table to store results for subproblems.

    Returns:
        int: The minimum number of coins needed to make the change.
    """
    # Base case: If no change is required, no coins are needed
    if change == 0: 
        return 0
    
    # If the result is already in the table, return it
    if known_results[change] != -1:
        return known_results[change]
    
    # Initialize minimum coins to infinity for comparison
    min_coins = float("inf")
    
    # Iterate through each coin denomination
    for coin_type in coin_types:
        if coin_type <= change:  # Ensure the coin type does not exceed the current change
            # Recursively find the result for the remaining change
            num_coins = num_coins_memo(change - coin_type, coin_types, known_results)
            # Update the minimum coins needed
            min_coins = min(min_coins, 1 + num_coins)
    
    # Store the result in the memoization table
    known_results[change] = min_coins
    return min_coins


# Example usage
coin_types = [1, 5, 10, 25]
change = 37

# Initialize memoization table with -1 (indicating results are not computed yet)
known_results = [-1] * (change + 1)

print(num_coins_memo(change, coin_types, known_results))  # Output: 4 (25 + 10 + 1 + 1)
