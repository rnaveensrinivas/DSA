from typing import List
import re

def tokenizer(expression: str) -> List[str]:
    """Split an expression into a list of tokens including operators, numbers, and parentheses.

    Args:
        expression (str): The input expression as a string. For example, "3 + 5 * (2 - 8)".

    Returns:
        List[str]: A list of tokens representing the components of the expression.
                   Tokens can include numbers, operators (+, -, *, /, ^), and parentheses.

    Example:
        >>> tokenizer("3 + 5 * (2 - 8)")
        ['3', '+', '5', '*', '(', '2', '-', '8', ')']

    Notes:
        - The tokenizer uses regular expressions to split the input while keeping operators,
          numbers, and parentheses as separate elements.
        - Whitespace is stripped, and empty tokens are removed.
    """
    tokens = re.split(r"([+\-*/^() ])", expression)
    # Strip whitespace and remove empty tokens
    return [token.strip() for token in tokens if token.strip()]

def html_tokenizer(html_script: str) -> List[str]:
    """Given an HTML script, return all the tags.

    Args:
        html_script (str): The HTML script as a string.

    Returns:
        List[str]: A list of HTML tags found in the script.
        
    Notes:
        - <[^>]+> matches any string that starts with <, includes any characters 
        except >, and ends with >.
    
    """
    # Regular expression to match HTML tags
    tag_pattern = r"<[^>]+>"
    return re.findall(tag_pattern, html_script)


def valid_token(token: str, 
                match_variables: bool = True,
                match_paranthesis: bool = True) -> bool:
    """Check if a token is valid.
    
    A valid token is:
    - An operator or a parenthesis: `*/+-^()`
    - A number: one or more digits (e.g., `1`, `123`)
    - A variable: one or more letters (e.g., `x`, `var`)
    
    Args:
        token (str): The token to validate.
        match_variables (bool): Flag to enable/disable variable matching (default is True).
        match_paranthesis (bool): Flag to enable/disable paranthesis matching (default is True).
        
    Returns:
        bool: True if the token is valid, False otherwise.
    """
    
    # Early return for empty token
    if not token:
        return False
    
    # Check if the token is an operator 
    if token in "*/+-^":
        return True
    
    # Check if the token is a parenthesis
    if match_paranthesis and token in "()":
        return True
    
    # Check if the token is a number (integer)
    if re.fullmatch(r"[0-9]+", token):
        return True
    
    # Optionally, check if the token is a variable (alphabetic)
    if match_variables and re.fullmatch(r"[a-zA-Z]+", token):
        return True
    
    return False


assert tokenizer("1 + 3") == ["1", "+", "3"]
assert tokenizer("A+B") == ["A", "+", "B"], "Test failed for 'A+B'"
assert tokenizer("A-B") == ["A", "-", "B"], "Test failed for 'A-B'"
assert tokenizer("(A+B)*C") == ["(", "A", "+", "B", ")", "*", "C"], "Test failed for '(A+B)*C'"
assert tokenizer("A+B*C") == ["A", "+", "B", "*", "C"], "Test failed for 'A+B*C'"
assert tokenizer("A/B^C") == ["A", "/", "B", "^", "C"], "Test failed for 'A/B^C'"
assert tokenizer("12+34") == ["12", "+", "34"], "Test failed for '12+34'"
assert tokenizer("x+y*z") == ["x", "+", "y", "*", "z"], "Test failed for 'x+y*z'"
assert tokenizer("  A  +   B   ") == ["A", "+", "B"], "Test failed for '  A  +   B   '"
assert tokenizer("( A + B ) * C") == ["(", "A", "+", "B", ")", "*", "C"], "Test failed for '( A + B ) * C'"
assert tokenizer("((A+B)*C)") == ["(", "(", "A", "+", "B", ")", "*", "C", ")"], "Test failed for '((A+B)*C)'"
assert tokenizer("((x+y)*(z-w))") == ["(", "(", "x", "+", "y", ")", "*", "(", "z", "-", "w", ")", ")"], \
       "Test failed for '((x+y)*(z-w))'"
assert tokenizer("") == [], "Test failed for an empty string"
assert tokenizer("A") == ["A"], "Test failed for 'A'"
assert tokenizer("(A)") == ["(", "A", ")"], "Test failed for '(A)'"
assert tokenizer("1+2*(3-4)/5") == ["1", "+", "2", "*", "(", "3", "-", "4", ")", "/", "5"], \
       "Test failed for '1+2*(3-4)/5'"
assert valid_token("1") == True, "Failed for single digit number '1'"
assert valid_token("123") == True, "Failed for multiple digit number '123'"
assert valid_token("x") == True, "Failed for single letter variable 'x'"
assert valid_token("var") == True, "Failed for multiple letter variable 'var'"
assert valid_token("*") == True, "Failed for operator '*'"
assert valid_token("/") == True, "Failed for operator '/'"
assert valid_token("+") == True, "Failed for operator '+'"
assert valid_token("-") == True, "Failed for operator '-'"
assert valid_token("^") == True, "Failed for operator '^'"
assert valid_token("(") == True, "Failed for parenthesis '('"
assert valid_token(")") == True, "Failed for parenthesis ')'"
assert valid_token("1x") == False, "Failed for invalid token '1x' (number and variable mixed)"
assert valid_token("123abc") == False, "Failed for invalid token '123abc' (number and letters mixed)"
assert valid_token("") == False, "Failed for empty string ''"
assert valid_token("!@#") == False, "Failed for invalid characters '!@#'"



# Basic HTML structure
assert html_tokenizer("<html><head></head><body></body></html>") == [
    "<html>", "<head>", "</head>", "<body>", "</body>", "</html>"
]

# Nested tags with content
assert html_tokenizer("<div><p>Hello, World!</p></div>") == [
    "<div>", "<p>", "</p>", "</div>"
]

# Self-closing tags
assert html_tokenizer("<img src='image.jpg' /><br/>") == [
    "<img src='image.jpg' />", "<br/>"
]

# Mixed tags and text
assert html_tokenizer("<h1>Title</h1><p>Paragraph</p>") == [
    "<h1>", "</h1>", "<p>", "</p>"
]

# Tags with attributes
assert html_tokenizer("<a href='https://example.com'>Link</a>") == [
    "<a href='https://example.com'>", "</a>"
]

# Multiple attributes
assert html_tokenizer("<input type='text' name='username' />") == [
    "<input type='text' name='username' />"
]

# Unusual spacing
assert html_tokenizer("< div >Content</ div >") == [
    "< div >", "</ div >"
]

# Empty string (edge case)
assert html_tokenizer("") == []

# No tags, only plain text
assert html_tokenizer("This is just plain text.") == []

# Malformed tags
assert html_tokenizer("<div><p>Unclosed div") == [
    "<div>", "<p>"
]

# Comments in HTML
assert html_tokenizer("<!-- This is a comment -->") == [
    "<!-- This is a comment -->"
]

# Special cases
assert html_tokenizer("<!DOCTYPE html>") == [
    "<!DOCTYPE html>"
]
assert html_tokenizer("<script>var x = 10;</script>") == [
    "<script>", "</script>"
]
