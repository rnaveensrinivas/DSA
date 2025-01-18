def reverse_string(string: str) -> str: 
    """Recursively reverse the given string."""
    if len(string) == 0: 
        return string
    else: 
        # Reverse rest and add first character
        return reverse_string(string[1:]) + string[0]
    
    
# Basic tests
assert reverse_string("hello") == "olleh"         # Simple word
assert reverse_string("world") == "dlrow"         # Another simple word
assert reverse_string("Python") == "nohtyP"       # A programming language

# Single character strings
assert reverse_string("a") == "a"                 # Single character (should be the same)
assert reverse_string("Z") == "Z"                 # Single uppercase character

# Empty string
assert reverse_string("") == ""                   # Edge case: empty string

# Strings with spaces
assert reverse_string("hello world") == "dlrow olleh"  # Word with space
assert reverse_string(" a b c ") == " c b a "          # String with spaces

# Palindromes (should remain the same)
assert reverse_string("madam") == "madam"         # Palindrome
assert reverse_string("racecar") == "racecar"     # Another palindrome

# Strings with digits and symbols
assert reverse_string("12345") == "54321"         # Digits
assert reverse_string("!@#$%") == "%$#@!"           # Symbols
assert reverse_string("abc123XYZ") == "ZYX321cba"  # Mixed characters

# Case sensitivity
assert reverse_string("AbC") == "CbA"             # Mixed case

# Long strings
assert reverse_string("a" * 500) == "a" * 500    # Long string with the same character
assert reverse_string("1234567890" * 50) == ("0987654321" * 50)  # Long string with numbers