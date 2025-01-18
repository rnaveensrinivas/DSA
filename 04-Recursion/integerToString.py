NUMBERS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def int_to_str(integer: int, base: int) -> str:
    """Convert an integer to its string representation in a given base."""
    if base < 2 or base > len(NUMBERS):
        raise ValueError(f"Base must be between 2 and {len(NUMBERS)}")

    # Handle negative numbers by adding the '-' sign before the result
    if integer < 0:
        return '-' + int_to_str(-integer, base)
    
    # Base case: when the integer is less than the base
    if integer < base:
        return NUMBERS[integer]
    
    # Recursive case: divide the integer and build the string
    return int_to_str(integer // base, base) + NUMBERS[integer % base]

# Base 10 (decimal) to other bases
assert int_to_str(10, 2) == "1010"  # Binary (base 2)
assert int_to_str(10, 8) == "12"    # Octal (base 8)
assert int_to_str(10, 16) == "A"    # Hexadecimal (base 16)
assert int_to_str(255, 16) == "FF"  # Hexadecimal (base 16)

# Base 10 positive numbers
assert int_to_str(1234, 10) == "1234"   # Decimal (base 10)
assert int_to_str(1234, 2) == "10011010010"  # Binary (base 2)

# Base 36 tests (max base supported by NUMBERS string)
assert int_to_str(35, 36) == "Z"      # Base 36 (highest valid single digit)
assert int_to_str(36, 36) == "10"     # Base 36 (two digits)

# Negative numbers
assert int_to_str(-10, 2) == "-1010"  # Binary negative
assert int_to_str(-255, 16) == "-FF"  # Hexadecimal negative
assert int_to_str(-1234, 8) == "-2322"  # Octal negative

# Zero case
assert int_to_str(0, 2) == "0"       # Binary zero
assert int_to_str(0, 16) == "0"      # Hexadecimal zero

# Large numbers
assert int_to_str(987654321, 10) == "987654321"  # Decimal large number
assert int_to_str(987654321, 36) == "GC0UY9"     # Base 36 large number

# Invalid base cases (should raise ValueError)
try:
    int_to_str(123, 1)
except ValueError:
    pass  # Expected
try:
    int_to_str(123, 37)
except ValueError:
    pass  # Expected
