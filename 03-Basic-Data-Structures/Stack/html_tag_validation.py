from Stack import Stack
from tokenization import html_tokenizer
from typing import List

HTML_TAGS = {
    "</html>": "<html>",
    "</head>": "<head>",
    "</body>": "<body>",
    "</title>": "<title>",
    "</style>": "<style>",
    "</script>": "<script>",
    "</h1>": "<h1>",
    "</h2>": "<h2>",
    "</h3>": "<h3>",
    "</h4>": "<h4>",
    "</h5>": "<h5>",
    "</h6>": "<h6>",
    "</p>": "<p>",
    "</b>": "<b>",
    "</i>": "<i>",
    "</u>": "<u>",
    "</strong>": "<strong>",
    "</em>": "<em>",
    "</mark>": "<mark>",
    "</small>": "<small>",
    "</sub>": "<sub>",
    "</sup>": "<sup>",
    "</a>": "<a>",
    "</video>": "<video>",
    "</audio>": "<audio>",
    "</ul>": "<ul>",
    "</ol>": "<ol>",
    "</li>": "<li>",
    "</dl>": "<dl>",
    "</dt>": "<dt>",
    "</dd>": "<dd>",
    "</table>": "<table>",
    "</tr>": "<tr>",
    "</th>": "<th>",
    "</td>": "<td>",
    "</caption>": "<caption>",
    "</thead>": "<thead>",
    "</tbody>": "<tbody>",
    "</tfoot>": "<tfoot>",
    "</form>": "<form>",
    "</textarea>": "<textarea>",
    "</button>": "<button>",
    "</label>": "<label>",
    "</select>": "<select>",
    "</option>": "<option>",
    "</optgroup>": "<optgroup>",
    "</fieldset>": "<fieldset>",
    "</legend>": "<legend>",
    "</header>": "<header>",
    "</footer>": "<footer>",
    "</section>": "<section>",
    "</article>": "<article>",
    "</aside>": "<aside>",
    "</nav>": "<nav>",
    "</main>": "<main>",
    "</figure>": "<figure>",
    "</figcaption>": "<figcaption>",
    "</div>": "<div>",
    "</span>": "<span>",
    "</iframe>": "<iframe>",
    "</canvas>": "<canvas>",
    "</details>": "<details>",
    "</summary>": "<summary>",
    "</time>": "<time>",
}


def preprocess_html_token(token: str) -> str:
    """
    Preprocess an HTML-like token by extracting the tag name
    and ensuring it ends with '>'.
    
    Args:
        token (str): The input HTML-like token.
    
    Returns:
        str: The preprocessed token.
    """
    if not token: 
        return ""
    token = token.split(" ")[0]
    return token if token.endswith(">") else token + ">"


def validator(html_tokens: List[str]) -> bool:
    """
    Validates whether the given list of HTML tokens contains properly matched 
    opening and closing tags.

    Args:
        html_tokens (List[str]): A list of HTML tokens, where each token is either 
                                  an opening or closing tag (e.g., '<html>', '</html>').

    Returns:
        bool: True if all HTML tags are properly matched, nested, and balanced. 
              False if there are unmatched tags.

    Raises:
        ValueError: If an invalid or unmatched HTML tag is encountered.

    Example:
        html_tokens_valid = ["<html>", "<head>", "</head>", "<body>", "</body>", "</html>"]
        print(validator(html_tokens_valid))  # Expected output: True

        html_tokens_invalid = ["<html>", "<head>", "</body>", "</head>", "</html>"]
        print(validator(html_tokens_invalid))  # Expected output: ValueError("Invalid Token: </body>")
    """
    stk = Stack()
    
    for token in html_tokens:
        
        if token in HTML_TAGS.values(): # if it's an opening tag
            stk.push(token)
        elif token in HTML_TAGS: # if it's a closing tag
            
            if stk.is_empty(): 
                raise ValueError("Invalid Token: No matching opening tag found.")
            
            # Check if the top of the stack matches the corresponding opening tag
            if HTML_TAGS[token] == stk.peek():
                stk.pop()
            else:
                return False
            
    return stk.is_empty()  # Stack should be empty if all tags are balanced

    
    
def html_tag_validator(html_script: str) -> bool:
    """
    Validates the HTML tags in the given HTML script by checking if they are 
    properly nested and balanced.

    This function tokenizes the HTML script, processes the tokens, and then 
    validates the HTML tags by ensuring that each opening tag has a corresponding 
    closing tag and that they are properly nested.

    Args:
        html_script (str): A string containing the HTML script to be validated.

    Returns:
        bool: True if all HTML tags are correctly nested, balanced, and valid. 
              False if there are any unmatched or invalid tags.

    Example:
        html_script_valid = "<html><head><title>Title</title></head><body><h1>Hello</h1></body></html>"
        print(html_tag_validator(html_script_valid))  # Expected output: True

        html_script_invalid = "<html><head><title>Title</head><body><h1>Hello</body></html>"
        print(html_tag_validator(html_script_invalid))  # Expected output: False
    """
    html_tokens = html_tokenizer(html_script)
    processed_html_tokens = [preprocess_html_token(token) for token in html_tokens]
    return validator(processed_html_tokens)


# Simple valid HTML document with tags properly nested
html_valid_1 = """
<html>
    <head>
        <title>Sample Title</title>
    </head>
    <body>
        <h1>Main Heading</h1>
        <p>Paragraph content.</p>
    </body>
</html>
"""
assert html_tag_validator(html_valid_1) == True, "Logical error in html_tag_validator()"

# HTML with multiple nested tags, including <div> and <span>
html_valid_2 = """
<html>
    <body>
        <div>
            <p>This is inside a div.</p>
            <span>Inline text in span.</span>
        </div>
    </body>
</html>
"""
assert html_tag_validator(html_valid_2) == True, "Logical error in html_tag_validator()"

# HTML document with an unclosed <h1> tag (invalid)
html_invalid_1 = """
<html>
    <body>
        <h1>Unclosed header
        <p>Following paragraph.</p>
    </body>
</html>
"""
assert html_tag_validator(html_invalid_1) == False, "Logical error in html_tag_validator()"

# Missing closing tag for <body> (invalid)
html_invalid_2 = """
<html>
    <head>
        <title>Sample Title</title>
    </head>
    <body>
        <h1>Body content without closing body tag
</html>
"""
assert html_tag_validator(html_invalid_2) == False, "Logical error in html_tag_validator()"

# Self-closing tag for image (valid, in modern HTML5)
html_valid_3 = """
<html>
    <body>
        <img src="image.jpg" alt="Sample Image"/>
    </body>
</html>
"""
assert html_tag_validator(html_valid_3) == True, "Logical error in html_tag_validator()"

# HTML with missing closing <html> tag
html_invalid_4 = """
<html>
    <head><title>Title</title></head>
    <body><h1>Content</h1></body>
"""
assert html_tag_validator(html_invalid_4) == False, "Logical error in html_tag_validator()"

# Complex HTML with multiple nested elements and attributes
html_valid_4 = """
<html>
    <head>
        <meta charset="UTF-8">
        <title>Complex HTML</title>
    </head>
    <body>
        <div>
            <h2>Heading 2</h2>
            <p>Some text with <a href="http://example.com">a link</a>.</p>
        </div>
    </body>
</html>
"""
assert html_tag_validator(html_valid_4) == True, "Logical error in html_tag_validator()"

# Edge case with empty HTML document (valid)
html_valid_5 = ""
assert html_tag_validator(html_valid_5) == True, "Logical error in html_tag_validator()"

# Completely empty body tag (valid)
html_valid_6 = "<html><body></body></html>"
assert html_tag_validator(html_valid_6) == True, "Logical error in html_tag_validator()"

# Unmatched opening and closing tags (invalid)
html_invalid_6 = "<html><head><title>Unmatched Tags</head><body></html>"
assert html_tag_validator(html_invalid_6) == False, "Logical error in html_tag_validator()"


