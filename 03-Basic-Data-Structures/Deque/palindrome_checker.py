from Deque import Deque

ALPHANUMERIC = set('abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')

def is_palindrome(string: str) -> bool:
    """
    Determines whether the given string is a palindrome using a deque.

    Args:
        string (str): The input string to be checked.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    

    d = Deque()
    
    # Add each character to the rear of the deque
    for char in string:
        if char in ALPHANUMERIC: # consider only alphabets
            d.add_rear(char)
    
    # Compare characters from the front and rear
    while d.size() > 1:
        left_char = d.pop_front()  
        right_char = d.pop_rear() 
        if left_char != right_char:
            return False  
    
    return True 

# Basic palindromes
assert is_palindrome("radar") == True
assert is_palindrome("madam") == True
assert is_palindrome("toot") == True

# Single-character and empty strings (edge cases)
assert is_palindrome("a") == True
assert is_palindrome("") == True

# Non-palindromes
assert is_palindrome("hello") == False
assert is_palindrome("world") == False
assert is_palindrome("python") == False

# Palindromes with mixed cases
assert is_palindrome("RaceCar".lower()) == True
assert is_palindrome("MadAm".lower()) == True

# Test with phrases containing spaces
assert is_palindrome("a man a plan a canal panama") == True, "Failed on input 'a man a plan a canal panama'."
assert is_palindrome("never odd or even") == True, "Failed on input 'never odd or even'."
assert is_palindrome("hello world") == False, "Failed on input 'hello world'."

# Non-palindromes with spaces and punctuation
assert is_palindrome("This is not a palindrome".replace(" ", "").lower()) == False
assert is_palindrome("Almost a palindrome, but not quite!".replace(" ", "").replace(",", "").lower()) == False

# Numbers as strings
assert is_palindrome("12321") == True
assert is_palindrome("12345") == False

# Complex edge cases
assert is_palindrome("Able was I ere I saw Elba".replace(" ", "").lower()) == True
assert is_palindrome("Was it a car or a cat I saw".replace(" ", "").lower()) == True