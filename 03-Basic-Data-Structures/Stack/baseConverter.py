from Stack import Stack

NUMBERS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Up to base 36

def base_converter(decimal: int, base: int) -> str:
    """Convert a given decimal number to any base."""
    
    # Special case
    if decimal == 0: 
        return "0"
    
    remainder_stk = Stack()
    while decimal: 
        
        remainder_stk.push(decimal % base)
        decimal //= base
        
    return "".join([NUMBERS[remainder_stk.pop()] for _  in range(remainder_stk.size())])


assert base_converter(0, 2) == "0", "Logical error in base_converter()"
assert base_converter(10, 2) == "1010", "Logical error in base_converter()"
assert base_converter(255, 2) == "11111111", "Logical error in base_converter()"
assert base_converter(255, 16) == "FF", "Logical error in base_converter()"
assert base_converter(100, 10) == "100", "Logical error in base_converter()"
assert base_converter(123, 8) == "173", "Logical error in base_converter()"
assert base_converter(123, 16) == "7B", "Logical error in base_converter()"
assert base_converter(1000, 2) == "1111101000", "Logical error in base_converter()"
assert base_converter(1000, 16) == "3E8", "Logical error in base_converter()"
assert base_converter(42, 36) == "16", "Logical error in base_converter()"
assert base_converter(100, 36) == "2S", "Logical error in base_converter()"
assert base_converter(129, 8) == "201", "Logical error in base_converter()"
assert base_converter(500, 3) == "200112", "Logical error in base_converter()"
assert base_converter(255, 36) == "73", "Logical error in base_converter()"
assert base_converter(456, 5) == "3311", "Logical error in base_converter()"
assert base_converter(1, 2) == "1", "Logical error in base_converter()"
assert base_converter(7, 8) == "7", "Logical error in base_converter()"
assert base_converter(8, 8) == "10", "Logical error in base_converter()"
assert base_converter(15, 2) == "1111", "Logical error in base_converter()"
assert base_converter(31, 2) == "11111", "Logical error in base_converter()"
assert base_converter(31, 3) == "1011", "Logical error in base_converter()"
assert base_converter(1001, 2) == "1111101001", "Logical error in base_converter()"
assert base_converter(999, 8) == "1747", "Logical error in base_converter()"
assert base_converter(5000, 16) == "1388", "Logical error in base_converter()"
assert base_converter(777, 10) == "777", "Logical error in base_converter()"
assert base_converter(999, 36) == "RR", "Logical error in base_converter()"
assert base_converter(1000000, 2) == "11110100001001000000", "Logical error in base_converter()"
assert base_converter(1000000, 16) == "F4240", "Logical error in base_converter()"
assert base_converter(2, 16) == "2", "Logical error in base_converter()"
assert base_converter(16, 16) == "10", "Logical error in base_converter()"
assert base_converter(50, 36) == "1E", "Logical error in base_converter()"
assert base_converter(85, 16) == "55", "Logical error in base_converter()"
assert base_converter(12345, 8) == "30071", "Logical error in base_converter()"
assert base_converter(987654321, 10) == "987654321", "Logical error in base_converter()"
