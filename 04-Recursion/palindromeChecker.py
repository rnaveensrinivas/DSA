ALPHANUMERIC = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def is_palindrome(string: str, check_case: bool = False) -> bool:
    """Check if given string is palindrome, ignoring special symbols."""
    
    if len(string) <= 1: 
        return True
    elif string[0] not in ALPHANUMERIC: 
        return is_palindrome(string[1:], check_case) # ignore this character
    elif string[-1] not in ALPHANUMERIC:  
        return is_palindrome(string[:-1], check_case) # ignore this character
    else: 
        if check_case: 
            return string[0] == string[-1] and is_palindrome(string[1:-1], check_case)
        else: 
            return string[0].lower() == string[-1].lower() and is_palindrome(string[1:-1], check_case)
    
# Basic test cases
assert is_palindrome("madam") == True          # Simple palindrome
assert is_palindrome("racecar") == True        # Simple palindrome
assert is_palindrome("hello") == False         # Not a palindrome

# Palindromes with special characters and spaces
assert is_palindrome("A man, a plan, a canal, Panama!") == True  # Palindrome with punctuation and spaces
assert is_palindrome("Was it a car or a cat I saw?") == True    # Palindrome with punctuation and spaces
assert is_palindrome("No 'x' in Nixon") == True                 # Palindrome with quotes and spaces

# Single character string (should always be a palindrome)
assert is_palindrome("a") == True          # Single character string
assert is_palindrome("Z") == True          # Single character string

# Empty string (should be a palindrome)
assert is_palindrome("") == True           # Empty string

# Strings with mixed case
assert is_palindrome("MadAm") == True      # Palindrome with mixed case
assert is_palindrome("RaCecAr") == True    # Palindrome with mixed case

# Strings with non-alphabetic characters
assert is_palindrome("12321") == True      # Palindrome with numbers
assert is_palindrome("!@#$%^&*()") == True # Palindrome with symbols

# String with only ignored characters
assert is_palindrome(" ,!*()") == True     # String with only ignored characters

# Long palindrome with spaces and punctuation
assert is_palindrome("Able was I, ere I saw Elba!") == True   # Palindrome with spaces and punctuation

# Non-palindromes with special characters and spaces
assert is_palindrome("This is not a palindrome!") == False   # Not a palindrome with punctuation and spaces