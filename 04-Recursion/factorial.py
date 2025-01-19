def factorial(n: int) -> int:
    """Calculate the factorial of the number n."""
    
    if n <= 1: 
        return 1
    
    return n * factorial(n-1)

assert factorial(0) == 1, "Test case failed for n = 0"
assert factorial(1) == 1, "Test case failed for n = 1"
assert factorial(2) == 2, "Test case failed for n = 2"
assert factorial(3) == 6, "Test case failed for n = 3"
assert factorial(4) == 24, "Test case failed for n = 4"
assert factorial(5) == 120, "Test case failed for n = 5"
assert factorial(6) == 720, "Test case failed for n = 6"
assert factorial(7) == 5040, "Test case failed for n = 7"
assert factorial(10) == 3628800, "Test case failed for n = 10"