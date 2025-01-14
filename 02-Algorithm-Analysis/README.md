# What is Algorithm Analysis?

Algorithms are general step-by-step methods to solve problems, programs are specific implementations of these algorithms in a programming language. There can be many implementations of the same algorithm based on language, readability, style, and data structures available. AAlgorithm analysis focuses on evaluating the efficiency and effectiveness of the underlying algorithm, independent of its implementation. Readability is important, but understanding and analyzing algorithms is crucial in computer science.

Algorithm analysis aims to compare algorithms based on their efficiency in utilizing computing resources. This helps determine which algorithm is better in terms of **resource usage or overall efficiency**.  

### **Types of Resources Considered**:  
- **Space (Memory)**:  
    Algorithms can be analyzed based on the memory required to solve a problem. While this often depends on the problem instance, some algorithms have specific space requirements that warrant detailed examination.  
- **Time (Execution or Running Time)**:  
    Time efficiency is another key factor, referring to the duration an algorithm takes to execute.  

  - **Benchmark Analysis**:  
     One way to measure execution time is through benchmarking. In Python, the `time` module allows capturing the system clock time before and after execution to calculate the time taken. While this provides exact runtime values, these measurements are dependent on hardware, programming language, compiler, and other environmental factors.  

  - **Limitations of Benchmarking**:  
     Benchmarks are machine-dependent, making results inconsistent across different systems. As such, benchmarking is not a reliable method for universally comparing algorithms.  

### **Need for a Machine-Independent Measure**:  
   To compare algorithms fairly, a characterization of execution time that is independent of specific machines or environments is required. Such a measure focuses solely on the algorithm’s performance, enabling meaningful comparisons across implementations.  

---

# Big O Notation

To analyze an algorithm's efficiency independent of specific systems, we measure the **number of operations or steps** required to solve a problem. These steps are treated as basic units of computation, with the execution time expressed as a function $T(n)$, where $n$ represents the size of the problem.  

### **Defining $T(n)$:**  

$T(n)$ represents the **time complexity** of an algorithm, expressed as a function of $n$, where $n$ is the size of the input or problem instance. It quantifies the total number of basic operations or steps the algorithm requires to complete as a function of $n$.  

This function provides insight into how the algorithm's execution time scales with increasing input size, enabling comparisons between different algorithms based on their efficiency.

**Example**: For a summation algorithm, $T(n) = 1 + n$, where $n$ is the number of terms.  

### **Order of Magnitude and Dominant Term:**  
Exact counts of operations are less critical than identifying the **dominant part** of $T(n)$, which grows the fastest as $n$ increases. The dominant term provides a simplified approximation of $T(n)$, called the **order of magnitude**, represented using **Big O notation**, $O(f(n))$.  

* **Simplification Using Big O:**  
  - Example 1: For $T(n) = 1 + n$, as $n$ becomes large, the constant $1$ is insignificant, so $T(n) \approx O(n)$.  
  - Example 2: For $T(n) = 5n^2 + 27n + 1005$, the $n^2$ term dominates when $n$ is large. Coefficients and smaller terms are ignored, so $T(n) \approx O(n^2)$.  

* **Significance of Big O Notation:**  
  - Big O provides a universal way to describe an algorithm's growth rate as the input size increases.  
  - It enables comparisons between algorithms by focusing on their dominant behavior for large $n$.
  
### What we have done so far? 

We began by measuring the **actual execution time** of programs. However, this method proved unreliable as it depends on specific hardware, programming environments, and other external factors. To address this, we shifted our focus to the **inherent properties of the algorithm** itself by defining $T(n)$, a function that expresses the number of steps the algorithm requires as a function of the input size $n$.  

Next, we realized that we don’t need to determine the **exact number of steps** for most practical purposes. Instead, we focus on the **order of magnitude of the dominant term** in $T(n)$, as this term dictates the algorithm’s behavior for large inputs. This led us to the concept of **Big O notation**, which provides a simplified, machine-independent way to compare the efficiency of algorithms based on how their resource usage scales with input size.

### Characterizing Algorithm Performance  

For some algorithms, performance depends not only on the **size of the input** but also on the **specific values of the data**. In such cases, performance is characterized in three scenarios:  

1. **Worst-Case Performance**:  
   The scenario where the algorithm performs **poorly** due to specific data inputs that maximize computational effort.  

2. **Best-Case Performance**:  
   The scenario where the algorithm performs **exceptionally well**, requiring minimal computational effort due to favorable data inputs.  

3. **Average-Case Performance**:  
   The scenario representing the algorithm’s **typical performance**, accounting for the average behavior over all possible inputs.  

Understanding these distinctions is critical to avoid being misled by one specific case and ensures a balanced evaluation of an algorithm’s efficiency.

### Common Functions for Big O

A number of very common order of magnitude functions will come up over and over as you study algorithms. In order to decide which of these functions is the dominant part of any $T(n)$ function, we must see how they compare with one another as n gets large.

Here’s a table listing common **Big O functions** in increasing order of growth, along with descriptions and examples:  

| **Big O Notation** | **Name**               | **Description**                                                                                        | **Example**                                            |
|---------------------|------------------------|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| $O(1)$          | Constant              | Performance does not depend on the input size; always takes the same time.                             | Accessing an element in an array by index.           |
| $O(\log n)$     | Logarithmic           | Grows slowly; often associated with algorithms that halve the input size at each step.                 | Binary search.                                        |
| $O(n)$          | Linear                | Grows proportionally to the input size; processes every input element once.                            | Iterating through a list.                            |
| $O(n \log n)$   | Linearithmic          | Combines linear and logarithmic growth; common in efficient sorting algorithms.                        | Merge sort, heap sort.                               |
| $O(n^2)$        | Quadratic             | Grows proportionally to the square of the input size; often seen in nested loops.                      | Bubble sort, selection sort.                         |
| $O(n^3)$        | Cubic                 | Grows proportionally to the cube of the input size; common in complex nested loops.                    | Matrix multiplication (naive approach).             |
| $O(2^n)$        | Exponential           | Grows very rapidly; typically represents algorithms that explore all subsets or combinations.          | Solving the traveling salesperson problem (brute force). |
| $O(n!)$         | Factorial             | Grows extremely fast; often arises in problems involving permutations.                                 | Solving the traveling salesperson problem (exhaustive). |  

Here, is a simple visualization of above functions:  

![Visualizing Big O Functions](https://iq.opengenus.org/content/images/2021/08/time-complexity.jpg "Big O Functions")

Now, let's try an experiment, we will see the different between and $O(n^2)$ and $O(n)$ using list. Check it out [here](./self-check-min-element.py). 

# Performance of Python Data Structures

We’ll explore the Big O performance of Python lists and dictionaries through timing experiments. Understanding their efficiency is crucial for implementing other data structures.

## `timeit` Module

The `timeit` module in Python is used to measure the execution time of code snippets. It ensures consistent timing across different platforms by running the code in a controlled environment. This makes it ideal for benchmarking functions, especially when you want to compare their performance accurately.

### How to Use `timeit`:
1. **Create a `Timer` object**: The `Timer` object takes two arguments:
   - The first argument is the Python code you want to measure.
   - The second argument is the setup code, which runs once before the timed statement. This setup is often used to import necessary modules or initialize variables. The `timeit` module includes this step to ensure the timing tests are performed in a clean environment, free from any lingering variables or state that might unintentionally affect the function's performance.

2. **Running the Timer**: By default, `timeit` runs the statement one million times and returns the total time. The `number` parameter allows you to specify the number of repetitions. Since other processes on the computer may cause variations in time, running the test multiple times helps gather enough data for reliable measurements.

### Example:

Suppose we want to measure how long it takes to execute a simple function that sums a list of numbers.

```python
import timeit

# Setup code (initializes the list)
setup_code = "numbers = [i for i in range(100)]"

# Code to time (summing the list)
test_code = "sum(numbers)"

# Create Timer object
timer = timeit.Timer(test_code, setup_code)

# Run the Timer and measure execution time for 1000 repetitions
execution_time = timer.timeit(number=1000)

# Print the result
print(f"Execution time for 1000 repetitions: {execution_time} seconds")
```

### Output:
The output might look like this:

```plaintext
Execution time for 1000 repetitions: 0.020356000000000036 seconds
```

This means it took approximately 0.02 seconds to execute the summing operation 1000 times.

By using `timeit`, you can accurately measure how long a specific piece of code takes to run, which is particularly useful when comparing different approaches to solving the same problem.

---

## List's Algorithmic Complexity

Python's list implementation is optimized based on how people typically use lists. The developers prioritized fast performance for common operations like indexing and assignment, which are both $O(1)$ regardless of list size. For growing a list, `append` is O(1), while `extend` and concatenation `+` are $O(k)$, where $k$ is the size of the list being added. These choices reflect a trade-off, where less common operations may be slower to optimize the most frequent ones. 

List creation is a common task, and the most efficient methods for creating large lists are **range** and **repetition**, followed by **list comprehension**. **Appending** and **concatenation** are much slower, with **concatenation** being the least efficient. For optimal performance in large list creation, **range** or **repetition** should be preferred. To view an experiment with `timeit` that supports the above statements, click [here](./time-it-list-creation.py).


------


### **1. `index []`**
- **Description:** Access an element by its index.
- **Complexity:**
  - **Time**: $O(1)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  arr = [10, 20, 30]
  print(arr[1])  # Output: 20
  ```

---

### **2. `index assignment`**
- **Description:** Assign a value to a specific index.
- **Complexity:**
  - **Time**: $O(1)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  arr = [10, 20, 30]
  arr[1] = 50
  print(arr)  # Output: [10, 50, 30]
  ```

---

### **3. `append`**
- **Description:** Add an element to the end of the list.
- **Complexity:**
  - **Time**: $O(1)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  arr = [10, 20, 30]
  arr.append(40)
  print(arr)  # Output: [10, 20, 30, 40]
  ```

---

### **4. `pop()`**
- **Description:** Remove and return the last element.
- **Complexity:**
  - **Time**: $O(1)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  arr = [10, 20, 30]
  print(arr.pop())  # Output: 30
  print(arr)  # Output: [10, 20]
  ```

---

### **5. `pop(i)`**
- **Description:** Remove and return the element at index `i`.
- **Complexity:**
  - **Time**: $O(n)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  arr = [10, 20, 30]
  print(arr.pop(1))  # Output: 20
  print(arr)  # Output: [10, 30]
  ```

---

### **6. `insert(i, item)`**
- **Description:** Insert an item at index `i`.
- **Complexity:**
  - **Time**: $O(n)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  arr = [10, 30]
  arr.insert(1, 20)
  print(arr)  # Output: [10, 20, 30]
  ```

---

### **7. `del` operator**
- **Description:** Remove an element or slice using its index.
- **Complexity:**
  - **Time**: $O(n)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  arr = [10, 20, 30]
  del arr[1]
  print(arr)  # Output: [10, 30]
  ```

---

### **8. `iteration`**
- **Description:** Loop through elements in a list.
- **Complexity:**
  - **Time**: $O(n)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  arr = [10, 20, 30]
  for num in arr:
      print(num)  # Output: 10, 20, 30
  ```

---

### **9. `contains (in)`**
- **Description:** Check if an element exists in the list.
- **Complexity:**
  - **Time**: $O(n)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  arr = [10, 20, 30]
  print(20 in arr)  # Output: True
  ```

---

### **10. `get slice [x:y]`**
- **Description:** Extract a sublist from index `x` to `y` (exclusive).
- **Complexity:**
  - **Time**: $O(k)$, where $k$ is the required length
  - **Space**: $O(k)$, where $k$ is the required length
- **Example:**
  ```python
  arr = [10, 20, 30, 40]
  print(arr[1:3])  # Output: [20, 30]
  ```

---

### **11. `del slice`**
- **Description:** Remove a range of elements.
- **Complexity:**
  - **Time**: $O(n)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  arr = [10, 20, 30, 40]
  del arr[1:3]
  print(arr)  # Output: [10, 40]
  ```

---

### **12. `set slice`**
- **Description:** Replace a range of elements with another sequence.
- **Complexity:**
  - **Time**: $O(n+k)$, where $k$ is the required length
  - **Space**: $O(k)$, where $k$ is the required length
- **Example:**
  ```python
  arr = [10, 20, 30, 40]
  arr[1:3] = [50, 60]
  print(arr)  # Output: [10, 50, 60, 40]
  ```

---

### **13. `reverse`**
- **Description:** Reverse the elements of the list in place.
- **Complexity:**
  - **Time**: $O(n)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  arr = [10, 20, 30]
  arr.reverse()
  print(arr)  # Output: [30, 20, 10]
  ```

---

### **14. `concatenate`**
- **Description:** Combine two lists into a new list.
- **Complexity:**
  - **Time**: $O(k)$, where $k$ is the size of joining list
  - **Space**: $O(k)$, where $k$ is the size of joining list
- **Example:**
  ```python
  arr1 = [10, 20]
  arr2 = [30, 40]
  print(arr1 + arr2)  # Output: [10, 20, 30, 40]
  ```

---

### **15. `extend`**
- **Description:** Add all elements from another iterable to the end of the list.
- **Complexity:**
  - **Time**: $O(k)$, where $k$ is the size of joining list
  - **Space**: $O(k)$, where $k$ is the size of joining list
- **Example:**
  ```python
  arr = [10, 20]
  arr.extend([30, 40])
  print(arr)  # Output: [10, 20, 30, 40]
  ```

---

### **16. `sort`**
- **Description:** Sort the list in ascending order (in place).
- **Complexity:**
  - **Time**: $O(n.\log(n))$
  - **Space**: $O(1)$, using *Timsort*
- **Example:**
  ```python
  arr = [30, 10, 20]
  arr.sort()
  print(arr)  # Output: [10, 20, 30]
  ```

---

### **17. `multiply`**
- **Description:** Repeat the list `k` times.
- **Complexity:**
  - **Time**: $O(nk)$, where $k$ is the number of times multiplied. 
  - **Space**: $O(nk)$, where $k$ is the number of times multiplied.
- **Example:**
  ```python
  arr = [10, 20]
  print(arr * 3)  # Output: [10, 20, 10, 20, 10, 20]
  ```

### Summary

| **Operation**      | **Time Complexity**  | **Space Complexity** |
|--------------------|----------------------|----------------------|
| `index []`         | $O(1)$               | $O(1)$               |
| `index assignment` | $O(1)$               | $O(1)$               |
| `append`           | $O(1)$               | $O(1)$               |
| `pop()`            | $O(1)$               | $O(1)$               |
| `pop(i)`           | $O(n)$               | $O(1)$               |
| `insert(i, item)`  | $O(n)$               | $O(1)$               |
| `del` operator     | $O(n)$               | $O(1)$               |
| iteration          | $O(n)$               | $O(1)$               |
| `contains (in)`    | $O(n)$               | $O(1)$               |
| `get slice [x:y]`  | $O(k)$               | $O(k)$               |
| `del slice`        | $O(n)$               | $O(1)$               |
| `set slice`        | $O(n+k)$             | $O(n+k)$             |
| `reverse`          | $O(n)$               | $O(1)$               |
| `concatenate`      | $O(k)$               | $O(k)$               |
| `extend`           | $O(k)$               | $O(k)$               |
| `sort`             | $O(n \log(n))$       | $O(1)$ (Timsort)     |
| `multiply`         | $O(nk)$              | $O(nk)$              |


The two different times for `pop` occur because popping from the end of the list takes **O(1)**, while popping from the front (or any other position) takes **O(n)**. This is due to Python's list implementation, where removing an item from the front shifts all remaining elements. While this may seem inefficient, it allows for fast **O(1)** indexing, which Python designers considered a worthwhile tradeoff. Consider [this](./time-it-list-pop.py) experiment that demonstrates the performance difference. 

---

## Dictionary's Algorithmic Complexity

Dictionaries differ from lists in that they allow access by key instead of position. The key operations—getting an item, setting an item, and checking if a key exists—are all **O(1)** on average. However, in rare cases, these operations can degrade to **O(n)**. Let's look at the **average case** complexities for dictionaries. 

---

### **1. `get(key, value=None)`**
- **Description:** Returns the value for `key`. If `key` is not found, returns `value` (default is `None`).
- **Complexity:**
  - **Time**: $O(1)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  d = {'a': 1, 'b': 2}
  print(d.get('a'))  # Output: 1
  print(d.get('c', 0))  # Output: 0
  ```

---

### **2. `[]`**
- **Description:** Access the value associated with a `key`.
- **Complexity:**
  - **Time**: $O(1)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  d = {'a': 1, 'b': 2}
  print(d['a'])  # Output: 1
  ```

---

### **3. `d[key] = value`**
- **Description:** Assign a value to a specific key, adding it if it doesn’t exist.
- **Complexity:**
  - **Time**: $O(1)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  d = {'a': 1}
  d['b'] = 2
  print(d)  # Output: {'a': 1, 'b': 2}
  ```

---

### **4. `del` operator**
- **Description:** Delete a key-value pair.
- **Complexity:**
  - **Time**: $O(1)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  d = {'a': 1, 'b': 2}
  del d['a']
  print(d)  # Output: {'b': 2}
  ```

---

### **5. `pop(key)`**
- **Description:** Remove and return the value associated with `key`. Raises `KeyError` if `key` is missing.
- **Complexity:**
  - **Time**: $O(1)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  d = {'a': 1, 'b': 2}
  print(d.pop('a'))  # Output: 1
  print(d)  # Output: {'b': 2}
  ```

---

### **6. `popitem()`**
- **Description:** Removes and returns the **last inserted** key-value pair as a tuple.
- **Complexity:**
  - **Time**: $O(1)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  d = {'a': 1, 'b': 2}
  print(d.popitem())  # Output: ('b', 2)
  print(d)  # Output: {'a': 1}
  ```

---

### **7. `clear()`**
- **Description:** Remove all key-value pairs.
- **Complexity:**
  - **Time**: $O(n)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  d = {'a': 1, 'b': 2}
  d.clear()
  print(d)  # Output: {}
  ```

---

### **8. `update()`**
- **Description:** Updates the dictionary with key-value pairs from another dictionary or iterable.
- **Complexity:**
  - **Time**: $O(k)$, where $k$ is the number of updates. 
  - **Space**: $O(k)$, where $k$ is the number of updates. 
- **Example:**
  ```python
  d = {'a': 1}
  d.update({'b': 2, 'c': 3})
  print(d)  # Output: {'a': 1, 'b': 2, 'c': 3}
  ```

---

### **9. `keys()`**
- **Description:** Returns a view of the dictionary’s keys.
- **Complexity:**
  - **Time**: $O(n)$
  - **Space**: $O(n)$
- **Example:**
  ```python
  d = {'a': 1, 'b': 2}
  print(list(d.keys()))  # Output: ['a', 'b']
  ```

---

### **10. `values()`**
- **Description:** Returns a view of the dictionary’s values.
- **Complexity:**
  - **Time**: $O(n)$
  - **Space**: $O(n)$
- **Example:**
  ```python
  d = {'a': 1, 'b': 2}
  print(list(d.values()))  # Output: [1, 2]
  ```

---

### **11. `items()`**
- **Description:** Returns a view of the dictionary’s key-value pairs as tuples.
- **Complexity:**
  - **Time**: $O(n)$
  - **Space**: $O(n)$
- **Example:**
  ```python
  d = {'a': 1, 'b': 2}
  print(list(d.items()))  # Output: [('a', 1), ('b', 2)]
  ```

---

### **12. `contains (in)`**
- **Description:** Check if a key exists in the dictionary.
- **Complexity:**
  - **Time**: $O(1)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  d = {'a': 1, 'b': 2}
  print('a' in d)  # Output: True
  ```

---

### **13. `len(d)`**
- **Description:** Returns the number of key-value pairs.
  - **Complexity:**
  - **Time**: $O(1)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  d = {'a': 1, 'b': 2}
  print(len(d))  # Output: 2
  ```

---

### **14. `copy()`**
- **Description:** Returns a shallow copy of the dictionary.
- **Complexity:**
  - **Time**: $O(n)$
  - **Space**: $O(n)$
- **Example:**
  ```python
  d = {'a': 1, 'b': 2}
  new_d = d.copy()
  print(new_d)  # Output: {'a': 1, 'b': 2}
  ```

---

### **15. `getdefault(key)`**
- **Description:** Similar to `get()`, returns the value for `key`, or `None` if the key is not found.
- **Complexity:**
  - **Time**: $O(1)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  d = {'a': 1}
  print(d.get('b'))  # Output: None
  ```

---

### **16. `setdefault(key, value)`**
- **Description:** Returns the value for `key`. If `key` doesn’t exist, adds it with the specified value.
- **Complexity:**
  - **Time**: $O(1)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  d = {'a': 1}
  d.setdefault('b', 2)
  print(d)  # Output: {'a': 1, 'b': 2}
  ```

---

### **17. `fromkeys()`**
- **Description:** Creates a new dictionary with specified keys and a default value.
- **Complexity:**
  - **Time**: $O(n)$
  - **Space**: $O(n)$
- **Example:**
  ```python
  keys = ['a', 'b', 'c']
  d = dict.fromkeys(keys, 0)
  print(d)  # Output: {'a': 0, 'b': 0, 'c': 0}
  ```

---

### **18. `iteration`**
- **Description:** Iterate over keys, values, or key-value pairs.
- **Complexity:**
  - **Time**: $O(n)$
  - **Space**: $O(1)$
- **Example:**
  ```python
  d = {'a': 1, 'b': 2}
  for key, value in d.items():
      print(key, value)  # Output: a 1, b 2
  ```

### Summary
The efficiency of dictionary operations is summarized in below Table, based on **average performance**.

| **Operation**            | **Time Complexity** | **Space Complexity** |
|--------------------------|---------------------|----------------------|
| `get(key, value=None)`   | $O(1)$              | $O(1)$               |
| `[]`                     | $O(1)$              | $O(1)$               |
| `d[key] = value`         | $O(1)$              | $O(1)$               |
| `del` operator           | $O(1)$              | $O(1)$               |
| `pop(key)`               | $O(1)$              | $O(1)$               |
| `popitem()`              | $O(1)$              | $O(1)$               |
| `clear()`                | $O(n)$              | $O(1)$               |
| `update()`               | $O(k)$              | $O(k)$               |
| `keys()`                 | $O(n)$              | $O(n)$               |
| `values()`               | $O(n)$              | $O(n)$               |
| `items()`                | $O(n)$              | $O(n)$               |
| `contains (in)`          | $O(1)$              | $O(1)$               |
| `len(d)`                 | $O(1)$              | $O(1)$               |
| `copy()`                 | $O(n)$              | $O(n)$               |
| `getdefault(key)`        | $O(1)$              | $O(1)$               |
| `setdefault(key, value)` | $O(1)$              | $O(1)$               |
| `fromkeys()`             | $O(n)$              | $O(n)$               |
| `iteration`              | $O(n)$              | $O(1)$               |

Getting a value from a dictionary is **$O(1)$**, while that for list is **$O(n)$**. [This](./time-it-contains.py) time-it experiment demonstrates the behavior. 

---

## Set's Algorithmic Complexity

| **Operation**              | **Time Complexity** | **Space Complexity** |
|----------------------------|---------------------|----------------------|
| `add(element)`             | $O(1)$              | $O(1)$               |
| `remove(element)`          | $O(1)$              | $O(1)$               |
| `discard(element)`         | $O(1)$              | $O(1)$               |
| `pop()`                    | $O(1)$              | $O(1)$               |
| `clear()`                  | $O(1)$              | $O(1)$               |
| `copy()`                   | $O(n)$              | $O(n)$               |
| `update(iterable)`         | $O(len(iterable))$  | $O(len(iterable))$   |
| `union(set)`               | $O(len(set))$       | $O(len(set))$        |
| `intersection(set)`        | $O(min(len(self), len(set)))$ | $O(min(len(self), len(set)))$ |
| `difference(set)`          | $O(len(self))$      | $O(len(self))$       |
| `symmetric_difference(set)`| $O(len(self) + len(set))$ | $O(len(self) + len(set))$ |
| `issubset(set)`            | $O(len(self))$      | $O(1)$               |
| `issuperset(set)`          | $O(len(set))$       | $O(1)$               |
| `isdisjoint(set)`          | $O(min(len(self), len(set)))$ | $O(1)$               |
| `len(set)`                 | $O(1)$              | $O(1)$               |
| `in (element)`             | $O(1)$              | $O(1)$               |
| `iteration`                | $O(n)$              | $O(1)$               |

### Notes:
1. **Set Operations:** Operations like `intersection`, `union`, `difference`, etc., depend on the size of the input sets.
2. **Hash Table:** Sets in Python are implemented as hash tables, making most operations like `add`, `remove`, and membership tests (`in`) run in constant time $O(1)$.
3. **Space Complexity:** Space depends on the number of elements stored in the set. The memory usage is proportional to the size of the hash table used internally.

---

# Take a look at [Exercises](./Exercises.md)

