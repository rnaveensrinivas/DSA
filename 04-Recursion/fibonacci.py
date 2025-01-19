def fibonacci_recursive(number: int) -> int:
    """
    Calculate the nth Fibonacci number using recursion.

    The Fibonacci sequence is defined as:
    - F(0) = 0
    - F(1) = 1
    - F(n) = F(n-1) + F(n-2) for n > 1

    Args:
        number (int): The index of the Fibonacci sequence to calculate.

    Returns:
        int: The Fibonacci number at the given index.

    Example:
        fibonacci(0) -> 0
        fibonacci(1) -> 1
        fibonacci(5) -> 5
    """
    if number <= 0:
        return 0

    if number == 1:
        return 1

    return fibonacci_recursive(number-1) + fibonacci_recursive(number-2)

def fibonacci_iterative(number: int) -> int:
    """
    Calculate the nth Fibonacci number iteratively.

    The Fibonacci sequence is defined as:
    - F(0) = 0
    - F(1) = 1
    - F(n) = F(n-1) + F(n-2) for n > 1

    Args:
        number (int): The index of the Fibonacci sequence to calculate.

    Returns:
        int: The Fibonacci number at the given index.

    Example:
        fibonacci(0) -> 0
        fibonacci(1) -> 1
        fibonacci(5) -> 5
    """
    if number <= 0:
        return 0

    if number == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, number+1): 
        a, b = b, a+b
    
    return b


def test(fibonacci: callable) -> None:
    assert fibonacci(0) == 0, "Test case 1 failed"
    assert fibonacci(1) == 1, "Test case 2 failed"
    assert fibonacci(2) == 1, "Test case 3 failed"
    assert fibonacci(3) == 2, "Test case 4 failed"
    assert fibonacci(4) == 3, "Test case 5 failed"
    assert fibonacci(5) == 5, "Test case 6 failed"
    assert fibonacci(6) == 8, "Test case 7 failed"
    assert fibonacci(7) == 13, "Test case 8 failed"
    assert fibonacci(8) == 21, "Test case 9 failed"
    assert fibonacci(9) == 34, "Test case 10 failed"
    assert fibonacci(10) == 55, "Test case 11 failed"

test(fibonacci_recursive)
test(fibonacci_iterative)