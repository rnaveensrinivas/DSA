from typing import List, Tuple

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


def num_coins_dp(change: int, 
                 coin_types: List[int], 
                 known_results: List[int]) -> int:
    """
    Calculate the minimum number of coins needed to make a given amount of change
    using dynamic programming.

    Args:
        change (int): The total amount of change to be made.
        coin_types (List[int]): A list of available coin denominations.
        known_results (List[int]): A list used for memoization, initialized with
                                   `float('inf')` for all values except `0`.

    Returns:
        int: The minimum number of coins required to make the given change.

    Example:
        >>> coin_types = [1, 5, 10, 21, 25]
        >>> change = 63
        >>> known_results = [float("inf")] * (change + 1)
        >>> known_results[0] = 0
        >>> num_coins_dp(change, coin_types, known_results)
        4  # (25 + 25 + 10 + 1 + 1)
    
    Notes:
        - The algorithm builds the solution iteratively for all amounts from 1 to `change`.
        - The `known_results` array stores the minimum coins needed for each amount.
        - This ensures that when computing `known_results[cents]`, all smaller amounts
          have already been computed.
    """
    for cents in range(1, change + 1): 
        for coin_type in [coin_type for coin_type in  coin_types if coin_type <= cents]: 
            known_results[cents] = min(known_results[cents],
                                       1 + known_results[cents-coin_type])
            
    return known_results[change]
    
    
def get_coins_dp(change: int, 
                 coin_types: List[int], 
                 known_results: List[int]) -> Tuple[int, List[int]]:
    """
    Calculate the minimum number of coins needed to make a given amount of change
    and track the coins used.

    Args:
        change (int): The total amount of change to be made.
        coin_types (List[int]): A list of available coin denominations.
        known_results (List[int]): A list used for memoization, initialized with
                                   `float('inf')` for all values except `0`.

    Returns:
        Tuple[int, List[int]]: A tuple containing the minimum number of coins required
                               and a list of the coins used.

    Example:
        >>> coin_types = [1, 5, 10, 21, 25]
        >>> change = 63
        >>> known_results = [float("inf")] * (change + 1)
        >>> known_results[0] = 0
        >>> get_coins_dp(change, coin_types, known_results)
        (3, [21, 21, 21])  # Three 21-cent coins
    """
    # Array to track which coin is used to achieve the minimum for each amount
    coins_used = [0] * (change + 1)
    
    for cents in range(1, change + 1): 
        for coin_type in [coin_type for coin_type in coin_types if coin_type <= cents]: 
            # Update known_results if using this coin provides a better solution
            if 1 + known_results[cents - coin_type] < known_results[cents]:
                known_results[cents] = 1 + known_results[cents - coin_type]
                # Record the coin used to achieve the minimum for the current amount
                coins_used[cents] = coin_type
            
    # Backtrack through coins_used to find the coins used to make the target change
    result = []
    cents = change
    while cents: 
        result.append(coins_used[cents])  # Append the coin used
        cents -= coins_used[cents]       # Reduce the amount by the coin's value
        
    return known_results[change], result  # Return the minimum coins and the list of coins used

    
# Example usage
coin_types = [1, 5, 10, 21, 25]
change = 99

# Initialize memoization table with -1 (indicating results are not computed yet)
known_results = [float("inf")] * (change + 1)
known_results[0] = 0

print(get_coins_dp(change, coin_types, known_results))  

# Exercise question 3: 
coin_types = [1, 5, 8, 10, 25]
change = 33

# Initialize memoization table with -1 (indicating results are not computed yet)
known_results = [float("inf")] * (change + 1)
known_results[0] = 0

print(get_coins_dp(change, coin_types, known_results)) # (2, [8, 25])

