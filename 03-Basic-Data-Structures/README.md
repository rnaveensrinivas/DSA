# What are Linear Structures?

The study of data structures begins with four fundamental linear structures: stacks, queues, deques, and lists. These structures organize items in a specific order based on how they are added or removed. Items **maintain their relative positions** once added, making these collections **linear** in nature.

Linear structures have two ends, often referred to as front and rear, left and right, or top and bottom. The naming is less important than the rules governing **where items can be added or removed**. For instance, some structures allow additions at one end only, while others permit removals from both ends.

These variations make linear data structures highly versatile and essential for solving numerous problems in computer science and algorithms.

# Stacks

A stack (sometimes called a push-down stack) is an ordered collection of items where additions and removals occur only at one end, called the top. The opposite end is the base, which holds the oldest items (items that stayed in stack for long), while the top holds the most recently added item. Stacks follow the **LIFO** principle (Last In, First Out), meaning the last item added is the first to be removed.

Stacks are useful for reversing order. For instance, stacking books one by one and removing them reverses their original order. This reversal property makes stacks fundamental in various applications, such as a web browser’s Back button. As you navigate pages, URLs are added to a stack. Clicking "Back" removes them in reverse order, returning to previously visited pages.

## Stack Abstract Data Type

The stack abstract data type (ADT) is an ordered LIFO (Last In, First Out) collection of items where additions and removals occur at the top. The key operations for a stack are:

| **Method**   | **Description**                  | **Time Complexity** | **Space Complexity** |
|--------------|----------------------------------|----------------------|-----------------------|
| `Stack()`    | Creates an empty stack          | $O(1)$           | $O(1)$           |
| `push(item)` | Adds an item to the top         | $O(1)$           | $O(1)$           |
| `pop()`      | Removes and returns the top item| $O(1)$           | $O(1)$           |
| `peek()`     | Returns the top item without removing it | $O(1)$    | $O(1)$           |
| `is_empty()` | Checks if the stack is empty    | $O(1)$           | $O(1)$           |
| `size()`     | Returns the number of items in the stack | $O(1)$   | $O(1)$           |

### Notes:
- Time complexity is constant ($O(1)$) for all stack operations because these involve only the top element.
- Space complexity refers to the additional space required by each operation, excluding the space for the stack's elements.

## Implementing Stack 

When we give an abstract data type a physical implementation, we refer to the implementation as a data structure.

The stack, as an abstract data type, can have multiple physical implementations. One approach is to use a Python list with the stack's top at the end, utilizing efficient $O(1)$ operations like `append()` and `pop()`. Alternatively, the stack's top can be at the beginning of the list, requiring $O(n)$ operations like `insert(0)` and `pop(0)` due to the need to shift elements.

Check out the [implementation](./Stack/Stack.py) of stack using lists with top at end of list.

This flexibility in implementation demonstrates the power of abstraction, allowing different physical representations while maintaining the logical behavior of the stack. However, performance varies significantly, with the first implementation being more efficient for push and pop operations, especially for large stacks.

---
## Stack Applications: Reversing a String

One of the key properties of a stack is its ability to reverse the order of elements. This property can be leveraged to reverse a string efficiently using a stack. 

For an example of how to reverse a string using a stack, refer to the implementation in [reverse-string.py](./Stack/reverseString.py).

---
## Stack Applications: Simple Balanced Parentheses

In programming languages like Lisp, parentheses are used to structure expressions and functions. For instance:

```lisp
(defun square(n) (* n n))
```

Here, parentheses must appear in a balanced fashion: each opening parenthesis has a corresponding closing one, and they are properly nested. For example:

- Balanced: `(()()()())`, `(((())))`
- Unbalanced: `((((((())`, `()))`, `(()()(()`

To determine if a string of parentheses is balanced, observe that closing parentheses must match the most recent opening parenthesis, which suggests that a **stack** is the ideal data structure for this task. The stack ensures that parentheses are matched from the inside out, maintaining the correct order.

Here is the link [link](./Stack/simpleBalancedParantheses.py) to implementation.

----
## Stack Applications: Balanced Symbols

The problem of balanced parentheses is a specific case of a more general issue in programming languages, where different types of symbols (e.g., parentheses `()`, square brackets `[]`, and curly braces `{}`) need to be balanced and nested correctly. These symbols often represent different constructs in languages, such as lists, sets, dictionaries, and tuples in Python.

To solve this problem, a stack can be used: every opening symbol is pushed onto the stack, and when a closing symbol appears, it is checked against the symbol at the top of the stack to ensure they match. If they do, the opening symbol is popped from the stack. The string is balanced if all opening symbols have matching closing symbols, and the stack is empty at the end. Check out the implementation [here](./Stack/balancedSymbols.py). 

The concept of balanced symbols is essential in processing various language constructs in computer science. Stacks are useful for handling such problems, and this method extends easily to more complex cases beyond just parentheses.

---
## Stack Applications: Converting Decimal Numbers to any Base

Converting decimal numbers to any base, such as binary, octal, or hexadecimal, can be efficiently performed using a stack-based algorithm. The process involves repeatedly dividing the decimal number by the target base and storing the remainders in a stack. Each remainder corresponds to a digit in the new base, with the first remainder representing the least significant digit. After all divisions are completed, the stack contains the digits in reverse order, so the digits are popped off in sequence to form the final representation of the number in the desired base. 

This method is particularly useful for converting numbers to bases commonly used in computer science, such as binary (base 2), octal (base 8), and hexadecimal (base 16). The stack ensures that the digits are properly ordered when constructing the final result. [Here](./Stack/baseConverter.py) is an implementation of this algorithm.

Here is the division process for converting $1,000,000$ to base $16$ (hexadecimal) in table format:

| $Division$      | $Quotient$ | $Remainder (Digit)$ | $Position$ |
|----------------:|-----------:|--------------------:|--------:|
| $1000000 ÷ 16$  | $62500$    | $0$                 | $0$     |
| $62500 ÷ 16$    | $3906$     | $4$                 | $1$     |
| $3906 ÷ 16$     | $244$      | $2$                 | $2$     |
| $244 ÷ 16$      | $15$       | $4$                 | $3$     |
| $15 ÷ 16$       | $0$        | $15 (F)$            | $4$     |

Just look at remainder and the position column, think deep, you will get the intution. As you continue dividing and capturing remainders, each subsequent remainder corresponds to a higher place value, moving leftward in the number (just like in regular base-10 division).

**Final result**: $(F4240)_{16}$

---

## Stack Applications: Infix, Prefix, and Postfix Expressions

When you write an arithmetic expression like $B * C$, the form of the expression helps you interpret it correctly. In this case, the multiplication operator $*$ appears between the two operands $B$ and $C$, so you know that $B$ is multiplied by $C$. This is called an **infix expression** because the operator is placed between the operands.

Consider another example, $A + B * C$. While the operators $+$ and $*$ are still between the operands, the order in which the operations should be performed is unclear. To resolve this ambiguity, **operator precedence** is used. Multiplication has higher precedence than addition, so $B$ and $C$ are multiplied first, and then $A$ is added to the result. Parentheses can also be used to explicitly specify the order of operations, such as in $(A + (B * C))$.

To eliminate confusion and avoid relying on precedence rules, **fully parenthesized expressions** can be written. For example, $A + B * C + D$ can be rewritten as $((A + (B * C)) + D)$ to show that multiplication happens before addition. Similarly, $A + B + C + D$ can be written as $(((A + B) + C) + D)$ to follow left-to-right addition. This guarantees a clear and unambiguous interpretation of the expression.

There are two other expression formats, **prefix** (Polish Notation) and **postfix** (Reverse Polish Notation - RPN), which may seem unusual at first. In **prefix notation**, the operator precedes the operands, while in **postfix notation**, the operator follows the operands.

For example, the infix expression $A + B$ becomes:
- **Prefix**: $+ A B$
- **Postfix**: $A B +$

In **prefix notation**, operators come before their operands, and in **postfix notation**, they come after the operands. This shift ensures that the order of operations remains consistent.

Here are some examples comparing infix, prefix, and postfix notations:

| **Infix Expression** | **Prefix Expression** | **Postfix Expression** |
|----------------------|-----------------------|------------------------|
| $A + B$              | $+ A B$               | $A B +$                |
| $A + B * C$          | $+ A * B C$           | $A B C * +$            |
| $(A + B) * C$        | $* + A B C$           | $A B + C *$            |
| $A + B * C + D$      | $+ + A * B C D$       | $A B C * + D +$        |
| $(A + B) * (C + D)$  | $* + A B + C D$       | $A B + C D + *$        |
| $A * B + C * D$      | $+ * A B * C D$       | $A B * C D * +$        |
| $A + B + C + D$      | $+ + + A B C D$       | $A B + C + D +$        |

**Key Observations**:
- **Prefix and Postfix expressions** don’t require parentheses since the position of operators completely determines the order of operations.
- In contrast, **infix expressions** require parentheses to clarify precedence.
  
Prefix and postfix notations eliminate ambiguity and can be easier for computers to process within a **single pass**.

--- 

### Converting Infix Expressions to Prefix or Postfix (By Hand)
To convert an infix expression to prefix or postfix notation by hand, follow these steps:

1. **Fully Parenthesize the Infix Expression**:  
   Ensure that the infix expression is fully parenthesized, meaning each operator has its own pair of parentheses indicating the exact order of operations.

2. **Work from the Innermost Parentheses**:  
   Begin with the innermost parentheses and work your way out. This ensures that operations within parentheses are addressed first.

3. **Remove Parentheses and Add Operators**:  
   - For **Prefix**: Remove the parentheses, and **prefix** the operator to the operands. For example, $(A + B)$ becomes $+ A B$.
   - For **Postfix**: Remove the parentheses, and **postfix** the operator after the operands. For example, $(A + B)$ becomes $A B +$.

4. **Repeat Until All Parentheses are Removed**:  
   Continue applying these steps to the remaining expressions, moving outward, until all parentheses are removed and the entire expression is converted to either prefix or postfix notation.

**Example**

Let's convert the expression $(A + B) * (C + D)$ into both prefix and postfix:

- **Step 1**: Fully Parenthesize -> $((A + B) * (C + D))$
- **Step 2**: Start with the inner expressions:
  - $(A + B)$ becomes $+ A B$ (in prefix) or $A B +$ (in postfix)
  - $(C + D)$ becomes $+ C D$ (in prefix) or $C D +$ (in postfix)
- **Step 3**: Now handle the outer operator $*$:
  - Prefix: $* + A B + C D$
  - Postfix: $A B + C D + *$

This gives the final converted expressions:
- **Prefix**: $* + A B + C D$
- **Postfix**: $A B + C D + *$

---

### General Algorithm for Converting Infix to Postfix

The algorithm below describes how to convert an infix expression (e.g., `(A + B) * C`) to postfix notation (e.g., `AB+C*`) using a stack:

1. **Initialize**:
   - Create an empty list `postfix_tokens` to store the resulting postfix expression.
   - Create an empty stack `stk` to temporarily hold operators and parentheses.

2. **Process each token in the infix expression**:
   - **If the token is a left parenthesis "("**:
     - Push the left parenthesis onto the stack (`stk.push("(")`).
     
   - **If the token is a right parenthesis ")"**:
     - While the top of the stack is not a left parenthesis and the stack is not empty:
       - Pop the top element from the stack and append it to `postfix_tokens`.
     - If the stack is empty (no matching left parenthesis):
       - Raise an error: "Unmatched closing parenthesis in expression!"
     - Pop the left parenthesis from the stack (it’s no longer needed).

   - **If the token is an operator (`+`, `-`, `*`, `/`, `^`)**:
     - While the stack is not empty and the top of the stack is either:
       - An operator with higher precedence, or
       - An operator with the same precedence (except for exponentiation `^`, which is right-associative):
         - Pop operators from the stack and append them to `postfix_tokens`.
     - Push the current operator onto the stack.

   - **If the token is an operand (e.g., a number or variable)**:
     - Append the token to `postfix_tokens` as it is.

3. **After processing all tokens**:
   - While the stack is not empty:
     - If the top of the stack is a left parenthesis, raise an error: "Unmatched opening parenthesis in expression!"
     - Pop the remaining operators from the stack and append them to `postfix_tokens`.

4. **Return the final `postfix_tokens` list**.

**Example Walkthrough**:

For the infix expression: `((A + B) * C) / D`

1. `(` → push to stack.
2. `(` → push to stack.
3. `A` → append to postfix tokens.
4. `+` → push to stack.
5. `B` → append to postfix tokens.
6. `)` → pop `+` to postfix, remove `(` from stack.
7. `*` → push to stack.
8. `C` → append to postfix tokens.
9. `)` → pop `*` to postfix, remove `(` from stack.
10. `/` → push to stack.
11. `D` → append to postfix tokens.

Final postfix expression: `AB+C*D/`.

**Time Complexity**:
- **O(n)** where `n` is the number of tokens in the input infix expression. Each token is processed once, and each operation takes constant time. 

**Time Complexity**:
- **O(n)** where `n` is the number of tokens in the input infix expression. The stack holds the operator, at worst case will hold all the operators in the expression.

**Code**: The code for the above algorithm is [here](./Stack/infixToPostfix.py). 

---

### Evaluating Postfix Expressions

Here is an algorithm to to evaluate postfix expressions:

1. **Initialize Stack:**
   - Create an empty stack `operand_stk` to hold operands as they are encountered.

2. **Iterate through each token in the postfix expression:**
   - For each token in the list `postfix_tokens`, perform the following:
   
   a. **If the token is an operator** (i.e., one of `*, /, +, -, ^`):
      - Check if the stack contains at least two operands. If not, raise an error for insufficient operands.
      - Pop two operands from the stack:
        - The first pop will give the **right operand**.
        - The second pop will give the **left operand**.
      - Apply the operator (`token`) to the operands:
        - Use a match-case structure to handle different operations:
          - For `*` (multiplication), `-` (subtraction), `+` (addition), `/` (division), and `^` (exponentiation), compute the result.
          - For division (`/`), ensure that the right operand is not zero to avoid division by zero errors.
      - Push the result back onto the stack.

   b. **If the token is an operand** (a number):
      - Convert it to an integer and push it onto the stack.

3. **Final Check:**
   - After processing all tokens, the stack should contain exactly one value, which is the result of the postfix expression.
   - If the stack size is not 1, raise an error for too many operands remaining.
   
4. **Return the final result:**
   - Pop and return the last element from the stack, which will be the result of the evaluation.

**Example Walkthrough**

For the postfix expression `["3", "4", "+", "2", "*", "7", "/"]`:

- **Step 1:** Initialize the stack: `[]`
- **Step 2:** Process each token:
  - `"3"`: Push `3`. Stack: `[3]`
  - `"4"`: Push `4`. Stack: `[3, 4]`
  - `"+"`: Pop `4` and `3`, calculate `3 + 4 = 7`. Push `7`. Stack: `[7]`
  - `"2"`: Push `2`. Stack: `[7, 2]`
  - `"*"`: Pop `2` and `7`, calculate `7 * 2 = 14`. Push `14`. Stack: `[14]`
  - `"7"`: Push `7`. Stack: `[14, 7]`
  - `"/"`: Pop `7` and `14`, calculate `14 / 7 = 2`. Push `2`. Stack: `[2]`
- **Step 3:** The stack now contains one value: `[2]`. Return `2`.

**Time Complexity**:
- **O(n)** where `n` is the number of tokens in the postfix expression. Each token is processed exactly once, and each operation (push, pop, arithmetic) takes constant time.

**Space Complexity**:
- **O(n)** where `n` is the number of operands in the postfix expression. The stack will hold operands, and in the worst case, it will hold all operands at once.

**Code**: The code for the above algorithm is [here](./Stack/postfixEvaluation.py). 

---

### Why Use Polish and Reverse Polish Notation?

The primary reason for using **Polish Notation (PN)** and **Reverse Polish Notation (RPN)** is that they enable **efficient evaluation** and **problem-solving in a single pass**, avoiding the complexities of parsing, parentheses handling, and operator precedence.

**Key Benefits**:
1. **Single Pass Evaluation**: 
   - Both notations allow for **left-to-right evaluation** in one pass, simplifying computation in contexts like calculators, interpreters, and compilers.

2. **No Parentheses Needed**: 
   - The order of operations is determined by the operator's position, eliminating the need for parentheses and simplifying parsing.

3. **Efficient Memory Use**: 
   - Using a **stack** to evaluate expressions optimizes memory usage and improves computational efficiency by directly modifying the stack.

4. **Cleaner Parsing Logic**: 
   - Both notations simplify parsing, avoiding complex rules like operator precedence and associativity, making parsing faster and more efficient.

**Why "On the Go"?**
- **On-the-fly computation** allows real-time expression processing, ideal for:
  - **Real-time calculators** that evaluate as input is entered.
  - **Streaming data** that requires immediate calculations.
  - **Embedded systems** needing low-latency computation.

---

# Queue

A queue is an **ordered collection** where items are added at one end, called the **rear**, and removed from the other end, called the **front**. Items wait in the queue until it is their turn to be removed. This follows the **FIFO** (First In, First Out) principle, meaning the first item added is the first one removed. A real-life example is a line at a store or a movie theater, where people wait their turn and cannot cut in or leave early.

Queues are also used in computer systems to manage processes. For example, operating systems use queues to schedule tasks efficiently. Keystrokes typed by a user are placed in a queue-like buffer when the system is busy, and they are eventually displayed on the screen in the correct order. The key characteristics of queues are their **restricted access** (only one way in and one way out) and their fair processing order.

---

## Queue Abstract Data Type

The **queue abstract data type (ADT)** is an ordered collection of items where additions occur at the **rear** and removals occur at the **front**, maintaining the **FIFO (First In, First Out)** property. The key operations for a queue are:

**Assumption**: Queue is implemented using **doubly linked list** with **head** and **tail** pointers.  
Based on the underlying implementation data structure the complexities can vary. For example, if we use list as the underlying implementation data structure, then we would have $O(n)$ complexity in either enqueu() or dequeue() based on the choice of front and rear. 

| **Method**      | **Description**                          | **Time Complexity** | **Space Complexity** |
|-----------------|------------------------------------------|---------------------|----------------------|
| `Queue()`       | Creates an empty queue                   | $O(1)$              | $O(1)$               |
| `enqueue(item)` | Adds an item to the rear of the queue    | $O(1)$              | $O(1)$               |
| `dequeue()`     | Removes and returns the front item       | $O(1)$              | $O(1)$               |
| `is_empty()`    | Checks if the queue is empty             | $O(1)$              | $O(1)$               |
| `size()`        | Returns the number of items in the queue | $O(1)$              | $O(1)$               |

### Notes:
- **Time complexity** for all queue operations is constant **$O(1)$**, as these operations involve adding or removing elements from the front or rear.
- **Space complexity** is also **$O(1)$** for each operation, excluding the space required by the queue's internal storage (which scales with the number of elements).

---

## Implementing Queue

You can find the implementation [here](./Queue/Queue.py). In this implementation, **list** is used as the internal data structure, with the **front** of the queue at the **0th index** and the **rear** at the end of the list. As a result, the **`dequeue()`** operation has a time complexity of **$O(n)$** due to the need to shift all elements after removal.

---

## Queue Applications: Hot Potato

One classic application of a queue is simulating situations where data must be managed in a **First-In-First-Out (FIFO)** manner. A good example is the children's game **hot potato**, where children pass an item in a circle. When the music or action stops, the child holding the item is eliminated, and the game continues until only one child remains.

This game is a modern version of the famous **Josephus problem**, which is based on a historical legend involving the first-century Jewish historian **Flavius Josephus**. During the Jewish revolt against Rome, Josephus and 39 comrades were trapped in a cave. Facing imminent defeat and capture, they decided to commit suicide rather than be enslaved. They arranged themselves in a circle and began eliminating every seventh person. Josephus, a skilled mathematician, deduced where he should sit in the circle to avoid being eliminated, ultimately surviving by joining the Roman side. 

While the Josephus problem has many versions, with different numbers of people and elimination patterns, the underlying concept remains the same: a group of people arranged in a circle, with every nth person eliminated until only one person is left standing.

For an implementation of the **Hot Potato game**, refer to this [code](./Queue/hotPotato.py).

---

# Deque

A deque (**double-ended queue**), pronounced as "deck" is an ordered collection of items that allows adding and removing elements from both ends (front and rear). This flexibility makes it a hybrid structure combining the functionalities of stacks and queues, without enforcing LIFO or FIFO orderings. Proper and consistent use of addition and removal operations is required to maintain the desired behavior.

## Deque Abstract Data Type (ADT)

The **deque abstract data type (ADT)** is an ordered collection of items where elements can be added or removed from both ends (front and rear). This makes the deque a flexible data structure supporting operations of both stacks and queues.

**Assumption**: Deque is implemented using a **doubly linked list** with **head** and **tail** pointers.  
Based on the underlying implementation data structure, the complexities may vary. For example, using a list as the implementation would result in $O(n)$ complexity for operations involving either end, depending on the choice of front and rear.

| **Method**          | **Description**                                   | **Time Complexity** | **Space Complexity** |
|----------------------|---------------------------------------------------|---------------------|----------------------|
| `Deque()`           | Creates an empty deque                            | $O(1)$              | $O(1)$               |
| `add_front(item)`   | Adds an item to the front of the deque             | $O(1)$              | $O(1)$               |
| `add_rear(item)`    | Adds an item to the rear of the deque              | $O(1)$              | $O(1)$               |
| `remove_front()`    | Removes and returns the front item of the deque    | $O(1)$              | $O(1)$               |
| `remove_rear()`     | Removes and returns the rear item of the deque     | $O(1)$              | $O(1)$               |
| `is_empty()`        | Checks if the deque is empty                       | $O(1)$              | $O(1)$               |
| `size()`            | Returns the number of items in the deque           | $O(1)$              | $O(1)$               |

---

### Notes:
- **Time complexity** for all deque operations is constant **$O(1)$**, as they involve adding or removing elements at the front or rear.
- **Space complexity** for each operation is **$O(1)$**, not accounting for the storage required for the deque’s elements (which grows with the number of items).

---

## Implementing Deque

You can find the implementation [here](./Deque/Deque.py). In this implementation, **list** is used as the internal data structure, with the **front** of the queue at the **0th index** and the **rear** at the end of the list. As a result, the **`add_front()`** and **`pop_front()`** operations have a time complexity of **$O(n)$** due to the need to shift all elements after removal.

---

## Deque Applications: Palindrome Checker

A simple application would be is to check if a string is palidrome or not. [Here](./Deque/palindrome_checker.py) is the code implementation for it.

Leveraging the deque’s ability to add and remove elements from both ends in $O(1)$ time, we can compare characters from the front and rear of the string sequentially. If all pairs match, the string is a palindrome; otherwise, it is not. The code for the implementation is [here](./Deque/palindrome_checker.py).

---


# List

A **list** is a collection of items where each item has a relative position within the sequence. This structure allows operations like accessing the first, second, or last items and maintaining a flexible size. Lists are often **unordered**. In Python, lists are powerful built-in data structures, but in other languages, they may need to be implemented manually.

---

## Unordered List Abstract Data Type (ADT)

An **unordered list** is a collection where the relative position of items is maintained, but no specific order is enforced. The table below summarizes the core operations for an unordered list:

**Implementation Assumption**: A **doubly linked list** is used. If an array-based list is used, complexities may vary.

| **Method**      | **Description**                                           | **Time Complexity** | **Space Complexity** |
|------------------|----------------------------------------------------------|---------------------|----------------------|
| `List()`         | Creates a new empty list                                 | $O(1)$              | $O(1)$               |
| `add(item)`      | Adds a new item to the list                              | $O(1)$              | $O(1)$               |
| `remove(item)`   | Removes an item from the list                            | $O(n)$              | $O(1)$               |
| `search(item)`   | Searches for an item in the list                         | $O(n)$              | $O(1)$               |
| `is_empty()`     | Checks if the list is empty                              | $O(1)$              | $O(1)$               |
| `size()`         | Returns the number of items in the list                  | $O(1)$              | $O(1)$               |
| `append(item)`   | Adds a new item to the end of the list                   | $O(1)$              | $O(1)$               |
| `index(item)`    | Returns the position of an item in the list              | $O(n)$              | $O(1)$               |
| `insert(pos, item)` | Inserts an item at a specific position                | $O(n)$              | $O(1)$               |
| `pop()`          | Removes and returns the last item in the list            | $O(1)$              | $O(1)$               |
| `pop(pos)`       | Removes and returns an item at a specific position       | $O(n)$              | $O(1)$               |

---

### Notes:
1. **Time Complexity**:
   - Operations like `add`, `is_empty`, and `size` are $O(1)$.
   - Operations involving traversal, such as `remove`, `search`, and `insert`, are $O(n)$.

2. **Space Complexity**:
   - Each operation requires $O(1)$ space, excluding the storage for the list elements.
   - Doubly linked lists require extra memory for pointers (`next` and `prev`) compared to arrays.

3. **Advantages**:
   - **Dynamic Sizing**: No resizing overhead compared to arrays.
   - **Flexible Insertions**: Items can be added or removed efficiently without shifting elements.

---

## Ordered List Abstract Data Type (ADT)

An **ordered list** is a collection where each item is positioned based on a defined characteristic, such as ascending or descending order. 

| **Method**      | **Description**                                         | **Time Complexity** | **Space Complexity** |
|-----------------|--------------------------------------------------------|---------------------|----------------------|
| `OrderedList()` | Creates a new empty ordered list                       | $O(1)$              | $O(1)$               |
| `add(item)`     | Adds an item, maintaining order                        | $O(n)$              | $O(1)$               |
| `remove(item)`  | Removes the specified item                             | $O(n)$              | $O(1)$               |
| `search(item)`  | Searches for an item                                   | $O(n)$              | $O(1)$               |
| `is_empty()`    | Checks if the list is empty                            | $O(1)$              | $O(1)$               |
| `size()`        | Returns the number of items                            | $O(1)$              | $O(1)$               |
| `index(item)`   | Returns the position of an item                        | $O(n)$              | $O(1)$               |
| `pop()`         | Removes and returns the last item                      | $O(1)$              | $O(1)$               |
| `pop(pos)`      | Removes and returns an item at a specific position     | $O(n)$              | $O(1)$               |

---

### Key Differences from Unordered List:
- The `add(item)` method ensures the list remains sorted, making it more computationally expensive than in an unordered list.
- Operations like `remove` and `pop(pos)` also respect the ordering of items.

---

## Inheritance Heirarchy


```
                   ┌─────────────┐
                   │ LinkedList  │
                   └─────────────┘
                          ▲
                          │
             ┌────────────┴────────────┐
             │                         │
    ┌─────────────┐           ┌─────────────┐
    │UnorderedList│           │ OrderedList │
    └─────────────┘           └─────────────┘
```

1. **`LinkedList` (Base Class)**:
   - Represents a generic doubly linked list.
   - Provides core functionalities like `remove`, `search`, `is_empty`, `size`, `append`, `index`, `insert`, and `pop`.
   - Serves as the foundation for specific types of linked lists.

2. **`UnorderedList` (Derived Class)**:
   - Inherits from `LinkedList`.
   - Implements an **unordered linked list**, allowing elements to be added without any specific order.
   - Adds operations like `add` (to insert an element at the beginning) and retains core `LinkedList` operations.

3. **`OrderedList` (Derived Class)**:
   - Inherits from `LinkedList`.
   - Implements an **ordered linked list**, where elements are always inserted in a specific order (ascending or descending).
   - Adds the `add` operation, which ensures elements are inserted in the correct position based on the ordering.

This structure promotes **code reuse** by defining shared functionality in the base class (`LinkedList`) and extending or customizing behavior in the derived classes (`UnorderedList` and `OrderedList`).

---

## Implementing Doubly Linked List

A **doubly linked list** is a sequence of nodes, each containing:
1. **Data**: The value of the node.
2. **Next**: A pointer to the next node.
3. **Prev**: A pointer to the previous node.

This bidirectional linking enables efficient traversal and manipulation.

### Node Class:
```python
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data  # The value of the node
        self.next = next  # Pointer to the next node
        self.prev = prev  # Pointer to the previous node
```

### Advantages:
- **Bidirectional Traversal**: Navigate forward and backward efficiently.
- **Efficient Deletion**: Remove a node without traversing to find its predecessor.
- **Flexible Insertions**: Easily insert nodes before or after any given node.

---

### Code Implementation

- [**Node Class**](./List/Node.py)  
- [**Linked List**](./List/LinkedList.py)  
- [**Unordered List**](./List/UnorderedList.py)  
- [**Ordered List**](./List/OrderedList.py)  

---


# Take a look at [Exercises](./Exercises.md)

# To do
* Implement radix sort exercise question.
---
