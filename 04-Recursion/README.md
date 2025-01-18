# What is Recursion?

Recursion is a problem-solving technique where a problem is broken down into smaller subproblems, with each subproblem being a smaller instance of the original problem. The process continues until a "base case" is reached, which is small enough to solve trivially. Typically, recursion involves a function calling itself. Although it may seem simple, recursion provides elegant solutions to problems that would otherwise be complex or difficult to implement.

# Example: Calculating the Sum of a List of Numbers

Let’s assume you don’t have access to `while` or `for` loops. How would you compute the sum of a list of numbers?

If you were a mathematician, you might recall that addition is a function defined for two parameters: a pair of numbers. So, to turn the problem of summing a list into a simpler problem, we could represent the list as a series of nested addition operations.

For example, summing the numbers $1 + 3 + 5 + 7 + 9$ can be rewritten as:

$$
((((1 + 3) + 5) + 7) + 9)
$$
or equivalently:

$$
(1 + (3 + (5 + (7 + 9))))
$$

Notice that the innermost addition, $(7 + 9)$, is a simple problem that can be solved directly without the need for loops or complex constructs. The problem is gradually simplified as we move outward:

$$
\begin{aligned}
\text{total} &= (1 + (3 + (5 + (7 + 9)))) \\
\text{total} &= (1 + (3 + (5 + 16))) \\
\text{total} &= (1 + (3 + 21)) \\
\text{total} &= (1 + 24) \\
\text{total} &= 25
\end{aligned}
$$

## Python Implementation

Now, let's translate this idea into Python code. We can define the sum of a list as the sum of the first element of the list (`num_list[0]`) and the sum of the rest of the list (`num_list[1:]`). This gives us the following functional definition:

$$
\text{list\_sum(num\_list)} = \text{first(num\_list)} + \text{list\_sum(rest(num\_list))}
$$

Here’s the Python implementation:

```python
def list_sum(num_list): 
    if len(num_list) == 1:  
        # Base case: the sum of a list of size 1 is just the first element
        return num_list[0]
    else: 
        return num_list[0] + list_sum(num_list[1:])
```

This function works by recursively summing the elements of the list. The base case occurs when the list has only one element, which is trivially the sum. Otherwise, it adds the first element of the list to the sum of the rest of the list, which is computed recursively.

--- 

## Recursion Trace Tree

Here’s an ASCII representation of the recursion trace tree for the `list_sum` function, using the example of the list `[1, 3, 5, 7, 9]`:

```
list_sum([1, 3, 5, 7, 9])
├── 1 + list_sum([3, 5, 7, 9])
│   ├── 3 + list_sum([5, 7, 9])
│   │   ├── 5 + list_sum([7, 9])
│   │   │   ├── 7 + list_sum([9])
│   │   │   │   ├── 9 ── Base case
│   │   │   │   └── Returns 9
│   │   │   └── Returns 7 + 9 = 16
│   │   └── Returns 5 + 16 = 21
│   └── Returns 3 + 21 = 24
└── Returns 1 + 24 = 25
```

**Explanation of the Trace**:
1. The first call is `list_sum([1, 3, 5, 7, 9])`. It calls `list_sum([3, 5, 7, 9])` recursively.
2. This process continues until the base case is reached with a list `[9]`, at which point the function returns `9`.
3. As the recursive calls return, the sums are calculated and propagated back up the tree:
   - `list_sum([9])` returns `9` (base case).
   - `list_sum([7, 9])` returns `7 + 9 = 16`.
   - `list_sum([5, 7, 9])` returns `5 + 16 = 21`.
   - `list_sum([3, 5, 7, 9])` returns `3 + 21 = 24`.
   - Finally, `list_sum([1, 3, 5, 7, 9])` returns `1 + 24 = 25`.

---

# Three Laws of Recursion

Recursive algorithms must follow three essential laws:

1. **Base Case**: A recursive algorithm must have a base case, which is a condition that stops the recursion. It represents the simplest version of the problem that can be solved directly. In the `list_sum` algorithm, the base case is when the list has only one element.

2. **State Change**: The algorithm must **move toward the base case** by changing its state. This usually involves modifying the data that represents the problem, typically making the problem smaller. In `list_sum`, the list becomes shorter with each recursive call by removing the first element (`num_list[1:]`), progressively working toward the base case.

3. **Recursive Call**: The algorithm must call itself recursively to solve the problem. This is the essence of recursion—each recursive step solves a smaller instance of the problem until the base case is reached. In `list_sum`, the function calls itself with a shorter list (`num_list[1:]`), repeating the process until the base case is met.

These laws ensure that recursion is not just a cycle, but an effective method of solving problems by breaking them down into smaller, manageable subproblems.

# Simple Programs: 

## Converting an Integer to a String in Any Base

To convert an integer to a string in any base between binary and hexadecimal, a recursive approach works elegantly. The process involves three steps: reducing the integer into numbers smaller than base by using division with remainders, looking up each digit in a sequence of characters (e.g., "0123456789" for base 10), and concatenating the results. Using integer division, the remainder provides the next digit, and the quotient reduces the number toward the base case, where the number is smaller than the base. This recursive approach simplifies the conversion of numbers like `769` into their string representation by breaking down the problem into progressively smaller chunks. [Here](./integerToString.py) is the implementation. 

## Reversing a String

[Here](./reverseString.py) is the implementation. 

## Palindrome Checker

[Here](./palindromeChecker.py) is the implementation. 

# Stack Frames

In an alternative approach to converting an integer to a string in a given base, the [code](./integerToStringUsingStack.py) uses a stack to store the intermediate results instead of relying on recursion. During each iteration of the `int_to_str` function, the remainder of the integer divided by the base is pushed onto a stack. After the integer has been reduced to zero, the characters are popped from the stack and concatenated to form the final string. This method mirrors the behavior of Python’s call stack, where each recursive call generates a new **stack frame** for local variables. The explicit stack used here is similar to how Python’s internal stack frames work during recursion, where each function call’s return value is left on top of the stack. The stack frames in recursion also maintain the scope of local variables, ensuring each recursive call has its own set of variables independent of others.

## Example: Recursive Sum 

### Function Definition
```python
def sum_recursive(n):
    """Calculate the sum of numbers from n down to 1."""
    if n <= 0:
        return 0
    return n + sum_recursive(n - 1)
```

### Example Call: `sum_recursive(4)`

#### Stack Frame Representation

Each stack frame includes:
- **Current Value of `n`**
- **Return Expression**

```plaintext
Call Stack (from top to bottom)

+----------------------------------------+
| sum_recursive(0)                       |  # Base case
| n = 0                                  |
| return 0                               |
+----------------------------------------+
| sum_recursive(1)                       |  
| n = 1                                  |
| return 1 + sum_recursive(0)            |
+----------------------------------------+
| sum_recursive(2)                       |
| n = 2                                  |
| return 2 + sum_recursive(1)            |
+----------------------------------------+
| sum_recursive(3)                       |
| n = 3                                  |
| return 3 + sum_recursive(2)            |
+----------------------------------------+
| sum_recursive(4)                       |  # Initial call
| n = 4                                  |
| return 4 + sum_recursive(3)            |
+----------------------------------------+

Final Result: 10
```

---

### Unwinding the Stack (Execution Flow)
1. **Base Case (`n=0`)**:
   - The function returns `0` directly without making further recursive calls.
   - The `sum_recursive(0)` frame is popped.

2. **`sum_recursive(1)`**:
   - Calculates `1 + sum_recursive(0)` using the returned value from `sum_recursive(0)`.
   - Returns `1`.

3. **`sum_recursive(2)`**:
   - Calculates `2 + sum_recursive(1)` using the returned value from `sum_recursive(1)`.
   - Returns `3`.

4. **`sum_recursive(3)`**:
   - Calculates `3 + sum_recursive(2)` using the returned value from `sum_recursive(2)`.
   - Returns `6`.

5. **`sum_recursive(4)`**:
   - Calculates `4 + sum_recursive(3)` using the returned value from `sum_recursive(3)`.
   - Returns `10`.

---


# Visualizing Recursions

This section explores recursion through artistic examples using Python's **turtle graphics** module. Turtle graphics provide a simple way to create visual patterns by controlling a "turtle" that can move, turn, and draw lines. By adjusting the turtle's movement, line width, and color, we can create intricate designs.

## Quick Introduction to Turtle Module

The **turtle** module in Python is a beginner-friendly graphics library used to create simple drawings and animations. It introduces programming concepts visually, making it an excellent tool for learning programming and exploring recursion, geometry, and patterns.

### Key Features:
- **Turtle as a Cursor**: A "turtle" represents a cursor that moves on the screen to draw lines or shapes.
- **Drawing Commands**: Control the turtle to move forward, backward, turn, or lift its pen for movement without drawing.
- **Customization**: You can change the pen color, width, and speed of the turtle.
- **Shapes and Patterns**: Draw geometric shapes like circles, squares, and polygons or create complex patterns using loops and recursion.

### Basic Commands:
1. **Setup**: 
   - `import turtle`: Import the module.
   - `turtle.Turtle()`: Create a turtle object.

2. **Movement**:
   - `forward(distance)`: Move forward by a specified distance.
   - `backward(distance)`: Move backward.
   - `right(angle)` / `left(angle)`: Turn the turtle right or left by a given angle.

3. **Drawing**:
   - `penup()` / `pendown()`: Lift or place the pen to stop or start drawing.
   - `color(color_name)`: Set the pen color.
   - `width(width)`: Set the pen's thickness.

4. **Control**:
   - `speed(speed)`: Adjust drawing speed.
   - `exitonclick()`: Wait for a click to close the turtle window.

### Example:
```python
import turtle

# Create a turtle object
t = turtle.Turtle()

# Set turtle properties
t.color("blue")
t.width(2)

# Draw a square
for _ in range(4):
    t.forward(100)  # Move forward 100 units
    t.right(90)     # Turn right by 90 degrees

# Finish and close the window
turtle.done()
```

### Applications:
- Visualizing recursion (fractals, spirals)
- Drawing geometric shapes
- Animation and simple games

---

One example demonstrates drawing a **spiral recursively**. The base case stops the recursion when the line length (`len`) reaches zero or less. Otherwise, the turtle moves forward by `len` units, turns right by 90 degrees, and recursively calls the function with a reduced length. The window remains open until the user clicks on it, ensuring the design is visible before the program exits. Check out the code for drawing spiral recursively [here](./turtleSpiral.py).

Here's an improved version of your text, with better flow and use of links:

---

## Fractals

Fractals are mathematical structures that exhibit **self-similarity**, meaning they look the same at various levels of magnification. Found extensively in nature—such as in coastlines, snowflakes, mountains, trees, and shrubs—fractals are often used in computer graphics to generate realistic landscapes. One such example is a **fractal tree**, where even a small twig mirrors the entire structure of the tree. By recursively describing a tree as a trunk with smaller branches extending to the left and right, each retaining the same fractal properties, we can simulate tree-like growth in a computationally efficient manner. For an implementation of a fractal tree, check out this [Python code](./fractalTree.py).

To enhance the realism of the fractal tree, several modifications can be made to the recursive algorithm:

1. **Varying Branch Thickness**: As the branches get smaller, reduce their thickness to simulate the natural tapering of tree branches.
2. **Branch Color Changes**: Transition the color of branches to green as their length decreases, mimicking leaves.
3. **Randomized Branch Angles**: Introduce variation in the angle of branching, choosing a random angle between 15 and 45 degrees for each recursive step, creating a more organic look.
4. **Randomized Decay in Branch Length**: Instead of subtracting a fixed amount from the branch length, subtract a random amount to introduce irregularity and variation in the tree's shape.

These adjustments can lead to a much more lifelike representation of a tree's growth pattern. For an example of this modified fractal tree, see the [code here](./fractalTreeModified.py).

--- 

## Sierpinski triangle
The **Sierpinski triangle** is another fractal that demonstrates self-similarity. It can be drawn using a three-way recursive algorithm. Start with a large triangle, then divide it into four smaller triangles by connecting the midpoints of each side. Remove the middle triangle, and apply the same process to the remaining three corner triangles. This recursive process can be repeated indefinitely to create smaller triangles within each iteration. [Here](./SierpinskiTriangle.py) is an implementation.

---

# Complex Recursive Problems

We will now explore problems that are challenging to solve iteratively but can be elegantly addressed with recursion. We'll also examine a seemingly simple problem that appears to have a recursive solution, but doesn't.

## Tower of Hanoi

The **Tower of Hanoi** puzzle, created by French mathematician Edouard Lucas in 1883, is inspired by a legend involving Hindu priests in a temple. The priests were tasked with moving 64 gold disks from one pole to another, following two strict rules: only one disk can be moved at a time, and a larger disk cannot be placed on top of a smaller one. Although the story is intriguing, solving the puzzle is no easy feat. In fact, completing the task requires $2^{64} - 1 = 18,446,744,073,709,551,615$ moves, which would take $584,942,417,355$ years at the rate of one move per second! This underscores the puzzle's complexity.

Here is a simple **ASCII art** representation of the Tower of Hanoi with three poles and a few disks:

```plaintext
          |          |          |     
         -|-         |          |     
        --|--        |          |     
       ---|---       |          |     
      ----|----      |          |     
     -----|-----     |          |     
        Pole A     Pole B     Pole C
```

In this example, each pole holds a stack of 5 disks, with the smallest disk at the top and the largest at the bottom. To solve the Tower of Hanoi puzzle, the disks are moved between the poles while adhering to the rules.

### Recursive Solution

How do we solve this problem recursively? Here's how:

#### Base Case:
The base case occurs when we have only one disk. At this point, the puzzle is trivial — simply move the disk from Pole A to Pole C.

#### Recursive Steps:
- **For two disks**, we move the smaller disk to Pole B (using Pole C as an intermediary), then move the larger disk to Pole C. Finally, we move the smaller disk from Pole B to Pole C.
  
- **For three disks**, we move the smallest disk to Pole C, then the middle disk to Pole B, and finally move the smallest disk from Pole C to Pole B (using Pole C as an intermediary). Then, move the largest disk to Pole C, and using Pole A as an intermediary, move the disks from Pole B to Pole C.

This approach generalizes as we add more disks, and each step involves recursively solving smaller sub-problems.

Let's check out the [code](./towerOfHanoi.py). 

Here are some results: 
```plaintext
Solving Tower of Hanoi Problem for 1 disks
Move disk 1 from Pole A to Pole C

Solving Tower of Hanoi Problem for 2 disks
Move disk 1 from Pole A to Pole B
Move disk 2 from Pole A to Pole C
Move disk 1 from Pole B to Pole C

Solving Tower of Hanoi Problem for 3 disks
Move disk 1 from Pole A to Pole C
Move disk 2 from Pole A to Pole B
Move disk 1 from Pole C to Pole B
Move disk 3 from Pole A to Pole C
Move disk 1 from Pole B to Pole A
Move disk 2 from Pole B to Pole C
Move disk 1 from Pole A to Pole C

Solving Tower of Hanoi Problem for 4 disks
Move disk 1 from Pole A to Pole B
Move disk 2 from Pole A to Pole C
Move disk 1 from Pole B to Pole C
Move disk 3 from Pole A to Pole B
Move disk 1 from Pole C to Pole A
Move disk 2 from Pole C to Pole B
Move disk 1 from Pole A to Pole B
Move disk 4 from Pole A to Pole C
Move disk 1 from Pole B to Pole C
Move disk 2 from Pole B to Pole A
Move disk 1 from Pole C to Pole A
Move disk 3 from Pole B to Pole C
Move disk 1 from Pole A to Pole B
Move disk 2 from Pole A to Pole C
Move disk 1 from Pole B to Pole C
```
---

# Dynamic Programming

Many computer science problems involve optimizing values, such as finding the shortest path or minimizing the number of objects that satisfy certain criteria. One such optimization technique is **dynamic programming**. A classic example of an optimization problem is making change using the fewest coins. 

In a simple case with U.S. coins, a greedy approach works well: start with the largest coin (a quarter) and use as many as possible before moving to smaller coins. For example, for 63 cents, the greedy method gives six coins (two quarters, one dime, and three pennies). However, when a 21-cent coin is added to the mix, the greedy method fails, as it would still use six coins. The optimal solution, in this case, is three 21-cent coins. This shows that while the greedy approach can work in many situations, it doesn't always yield the best solution.

To ensure an optimal solution to the change-making problem, we can use recursion. The base case is when the amount to be changed exactly matches the value of a coin—this requires just one coin. For other amounts, we consider multiple options: we can subtract the value of a coin (such as a penny, nickel, or dime) and recursively determine the minimum number of coins needed for the remaining amount. 

The recursive solution involves selecting the smallest number of coins required for each possible coin, and the number of coins required for the original amount is the minimum among these options. This can be expressed as:

$$
\text{num\_coins}(original\_amount) = \min \left\{
\begin{array}{l}
1 + \text{num\_coins}(original\_amount - 1) \\
1 + \text{num\_coins}(original\_amount - 5) \\
1 + \text{num\_coins}(original\_amount - 10) \\
1 + \text{num\_coins}(original\_amount - 25) \\
\end{array}
\right\}
$$

Let's look at the recursive [code](./coinChange.py) on solving this problem. 

Now the recursive code is extremely inefficient, for a change of 63, it takes $67,716,925$ recursive calls to find the optimal solution of 4 coins. 

### Why is the Recursive Code Inefficient?

The recursive implementation of the `num_coins` function is inefficient due to **repeated calculations** of subproblems. Let’s break this down:

#### Example: Change for 63
When computing the minimum coins required for a change of 63 using coin denominations `[1, 5, 10, 25]`, the recursive function explores all possible combinations of coins. For each amount, it recursively calculates the minimum coins for smaller amounts, but the same subproblems are computed repeatedly.

#### Exponential Growth of Recursive Calls
Each recursive call spawns additional recursive calls for smaller amounts. This branching leads to an exponential growth in the number of calls as the `change` value increases.

For a change of 63:
- The function makes **67,716,925 recursive calls**.
- Most of these calls are redundant, recalculating solutions for the same subproblems (e.g., `num_coins(62)`, `num_coins(61)`, etc.).

#### The Core Issue: Overlapping Subproblems
The algorithm recomputes the solution for the same `change` multiple times. For example:
- When solving for `num_coins(63)`, the function may compute `num_coins(62)` multiple times as part of different branches.
- Similarly, `num_coins(61)` will also be recomputed many times within those branches.

This results in a **time complexity of O(c^n)**, where:
- `c` is the number of coin types.
- `n` is the target `change`.

### Solution: 

The key to reducing the workload in recursive solutions lies in **storing past results** to avoid redundant computations. This approach, known as **memoization** (also called **caching**), involves maintaining a table to store results of previously solved subproblems. Here's how it works:

1. **Store Results in a Table**: As soon as the minimum number of coins for a specific amount is calculated, store the result in a table (e.g., a dictionary or array).
   
2. **Check Before Computing**: Before attempting to calculate the minimum coins for a given amount, check the table to see if the result is already available.
   
3. **Reuse Stored Values**: If the result exists in the table, reuse it directly instead of recomputing the value. This eliminates redundant work and saves significant computation time.

This strategy transforms the inefficient recursive solution into a much faster and scalable approach, avoiding the repeated exploration of overlapping subproblems.

Take a look at method `num_coins_memo` in [code](./coinChange.py) on solving this problem. 

---

