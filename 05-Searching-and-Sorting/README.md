# Searching

Searching is the algorithmic process of finding a specific item in a collection. The result of a search is typically **True** or **False**, indicating whether the item is present. Occasionally, searches can return the item's location. In this context, the focus is on determining membership.

In Python, the **`in`** operator provides a simple way to check if an item exists in a list:

```python
15 in [3, 5, 2, 4, 1]  # False
3 in [3, 5, 2, 4, 1]   # True
```

Although the syntax is straightforward, underlying algorithms perform the actual search. There are various search methods, and understanding their operation and performance is key.

## The Sequential Search

In collections like lists, data items have a linear or sequential relationship, with each item's position determined by its index. A **sequential search** involves starting at the first item and moving through the list in order until either:

1. The desired item is found.
2. The search reaches the end of the list without finding the item.

This approach relies on the ordered nature of index values in a list.

An example: 
```plaintext
List: [3, 5, 2, 4, 1, 3, -9]
Search: 4

Start -> [3] -> [5] -> [2] -> [4] (Found!)  
```

Checkout the implementation [here](./sequentialSearch.py). 

### Analysis of Sequential Search

To analyze searching algorithms, the **number of comparisons** is used as the basic unit of computation. In sequential search, if the list is unordered and the item is not present, every element must be compared, requiring $n$ comparisons. When the item is present, the **best case** occurs if it is found in the first position, requiring just 1 comparison. The **worst case** happens if the item is found in the last position, requiring $n$ comparisons. On average, the item is found approximately halfway through the list, requiring $n/2$ comparisons. As $n$ becomes large, constants become negligible, making the time complexity $O(n)$.


**Table: Comparisons in Sequential Search of an Unordered List**

| **Case**              | **Item is Present**       | **Item is Not Present**   |
|-----------------------|--------------------------|--------------------------|
| **Best Case**         | $1$ comparison             | $n$ comparisons      |
| **Worst Case**        | $n$ comparisons      | $n$ comparisons      |
| **Average Case**      | $n/2$ comparisons    | $n$ comparisons      |

When searching an ordered list, the best-case scenario occurs if the item is found in the first position or if the first out-of-order item indicates the item is not present, requiring only 1 comparison. The **worst case** is similar to an unordered list, where $n$ comparisons are needed if the item is found at the end or confirmed absent after examining all elements. On average, when the item is present, it is found about halfway through the list, requiring $n/2$ comparisons. If the item is not present, fewer comparisons are needed compared to an unordered list since the search terminates early when encountering an out-of-range item. The time complexity remains $O(n)$, with minor improvements for absence cases.


**Table: Comparisons in Sequential Search of an Ordered List**

| **Case**              | **Item is Present**       | **Item is Not Present**   |
|-----------------------|--------------------------|--------------------------|
| **Best Case**         | $1$ comparison             | $1$ comparison             |
| **Worst Case**        | $n$ comparisons      | $n$ comparisons      |
| **Average Case**      | $n/2$ comparisons    | $n/2$ comparisons    |

---

## The Binary Search

A **binary search** is an efficient way to search an ordered list by dividing the search space in half with each comparison. Instead of sequentially checking each item, binary search begins by comparing the target with the middle item of the list. If the middle item is the target, the search is complete. If the target is smaller than the middle item, the search continues on the left half; if the target is larger, it continues on the right half. This process eliminates half of the list with each step, significantly improving search efficiency compared to sequential search.

Binary search is a classic example of the **divide and conquer** strategy. In this approach, the problem is divided into smaller subproblems, solved individually, and then combined to achieve the overall result. For binary search, the list is divided into two halves. Depending on whether the target is smaller or larger than the middle item, the search continues on the left or right half of the list, respectively, reducing the problem size with each step.

Checkout the implementation [here](./binarySearch.py). 

### Analysis of Binary Search

The binary search algorithm works by halving the search space with each comparison. After the first comparison, about half of the remaining items are eliminated. After the second comparison, half of the remaining items are further eliminated, and so on. This halving continues until only one item remains, which is either the target or not.

The number of comparisons needed to reduce the list to one item can be determined by the equation:

$$
\frac{n}{2^i} = 1
$$

Where $n$ is the number of items, and $i$ is the number of comparisons. Solving for $i$, we get:

$$
i = \log_2{n}
$$

Thus, the maximum number of comparisons required is logarithmic in relation to the size of the list, which makes the time complexity of the binary search algorithm:

$$
O(\log n)
$$

---

### Slicing and Binary Search 

The recursive solution for binary search can also use the slicing operator to divide the list into halves:

```python
binary_search_recursive(a_list[:midpoint], item)
binary_search_recursive(a_list[midpoint+1:], item)

```

However, slicing in Python takes $O(k)$ time, where $k$ is the length of the slice. This implies that the time complexity of binary search with slicing isn't strictly logarithmic. Instead of slicing, we can avoid this additional cost by passing the list along with the starting and ending indices. This allows the function to operate on sublists without creating new ones, keeping the time complexity at $O(\log n)$ for the binary search.

---

### Considerations for Small $n$
While binary search is more efficient than sequential search for large lists, for small values of $n$, the overhead of sorting may not justify its use. Sorting takes $O(n \log n)$ time, and for smaller lists, performing a sequential search may be more efficient. 

Therefore, when dealing with small datasets, the cost of sorting might outweigh the benefits of binary search. However, if the list can be sorted once and searched multiple times, the benefits of binary search become more apparent, as the initial sorting cost is amortized across many searches.

In summary:
- **For small datasets**, it might be better to avoid the overhead of sorting and use sequential search directly.
- **For large datasets**, sorting once and then performing binary search multiple times can be highly efficient.

---

# Hashing

In previous sections, we improved search algorithms by using information about item placement, such as binary search for ordered lists. In this section, we introduce hashing, a technique that builds a data structure allowing for constant time search. Hashing works by determining where items are stored in advance, making searches more efficient. However, achieving this efficiency depends on items being placed correctly, which isn't always the case.

A **hash table** is a collection of items which are stored in such a way as to make it easy to find them later. Each position of the hash table, often called a **slot**, can hold an item and is named by an integer value starting at 0. Initially, the hash table contains no items so every slot is empty. 

The mapping between an item and the slot where that item belongs in the hash table is called the **hash function**. The hash function will take any item in the collection and return an integer in the range of slot names between $0$ and $m-1$, where $m$ is the number of slots. A simple hash function, called **remainder method**, takes an item and divides it by the table size, returning the remainder as its hash value ($h(item) = item % m$). 

> **Note**
> Note that this remainder method (modulo) will typically be present in some form in all hash functions since the result must be in the range of slot names.

Once the hash values have been computed, we insert each item into the hash table at its designated position. After insertion, we can track the number of positions filled. The **load factor** represents the ratio of the number of elements to the number of available slots in the table. It indicates how full the table is, which can affect performance.

Formula:
$$
\text{Load Factor} = \frac{\text{Number of elements}}{\text{Number of slots}}
$$

When searching for an item, we compute its hash value using the hash function, then check the corresponding slot in the hash table. This search operation is **O(1)**, as the time required to compute the hash value and access the table slot is constant. If every item is correctly placed in its unique slot, we achieve constant-time search performance. This approach only works if each item is assigned to a unique slot. If multiple items are assigned to the same slot, a **collision** occurs, disrupting the hashing technique.

## Hash Functions

A **perfect hash function** maps each item in a collection to a unique slot. While it is possible to create a perfect hash function for a fixed collection, there is no systematic way to construct one for an arbitrary set of items. Although increasing the hash table size can ensure a perfect hash function, this approach is impractical for large item ranges, as it requires excessive memory. Instead, the goal is to create a hash function that minimizes collisions, is easy to compute, and distributes items evenly in the table.

### Folding Method

Sure! Here's the completed explanation:

The folding method for constructing hash functions begins by dividing the item into equal-sized pieces (the last piece may not be of equal size). These pieces are then added together to give the resulting hash value. For example, if our item was the phone number 436-555-4601, we would take the digits and divide them into groups of 2 (43, 65, 55, 46, 01). After the addition:

$$
43 + 65 + 55 + 46 + 1 = 210
$$

Next, we take the remainder when dividing by the number of slots in the hash table (in this case, 11). We compute:

$$
210 \mod 11 = 1
$$

Thus, the phone number 436-555-4601 hashes to slot 1.

Some folding methods go one step further and reverse every other piece before the addition. For the above example, reversing the second and fourth pieces (65 and 46) gives us:

$$
34 + 56 + 55 + 64 + 10 = 219
$$

Taking the remainder when dividing by 11:

$$
219 \mod 11 = 10
$$

Thus, the phone number 436-555-4601 hashes to slot 9 using this folding method.

### Mid-square Method

Another numerical technique for constructing a hash function is called the **mid-square method**. We first square the item, and then extract some portion of the resulting digits. 

For example, if the item were 44, we would first compute:

$$
44^2 = 1936
$$

Next, we extract the middle two digits from the result, which are **93**. Then, we take the remainder when dividing by the number of slots in the hash table (say, 11):

$$
93 \mod 11 = 5
$$

Thus, the item 44 hashes to slot 5 using the mid-square method.

### Hashing Characters

Hash functions can also be applied to character-based items like strings. One method involves converting each character to its ordinal value (using `ord()`), summing these values, and then applying the remainder method to map the sum to a hash table slot.

For example, the word "cat" can be hashed by converting its characters to their ordinal values:

$$
\text{ord}("c") = 99, \quad \text{ord}("a") = 97, \quad \text{ord}("t") = 116
$$

The hash value is then computed as:

$$
(99 + 97 + 116) \mod \text{table\_size}
$$

This method results in a hash value, but it has the limitation of producing the same hash for anagrams (words with the same letters in different order). To address this, one might use the position of characters as a weighting factor, giving different hash values to anagrams.

$$
(99 * 1 + 97 * 2 + 116 * 3) \mod \text{table\_size}
$$

While it's possible to come up with various hash functions, the key is that the function should be efficient, as a complex hash function could negate the advantages of hashing, making it slower than basic search methods like sequential or binary search.

## Collision Resolution

Collision resolution is the process used when two items hash to the same slot in a hash table. If the hash function is perfect, collisions will never occur. However, since this is often not possible, collision resolution becomes a very important part of hashing.

One common method for resolving collisions is **open addressing**, which involves finding an open slot in the hash table for the colliding item. **Linear probing** is a specific open addressing technique where, after a collision, the algorithm **sequentially** checks each subsequent slot until an empty one is found. This process can wrap around the table circularly to ensure all slots are checked.

When using a hash table with **open addressing** and **linear probing**, the search process follows the same logic as insertion. If the desired item is found at the hashed slot, it can be returned immediately. However, if a **collision** occurs (i.e., the slot is occupied by a different item), a **sequential search** must be performed starting from the next slot. This search continues until either the item is found or an **empty slot** is encountered, indicating the item is not in the table.

This search strategy ensures that all possible positions for a colliding item are checked, but it also means that the presence of other items with the same hash value can impact search efficiency.

A key disadvantage of **linear probing** is **clustering**, where consecutive slots in the hash table become filled due to multiple items hashing to the same value. This cluster formation occurs when many collisions happen at the same hash value, causing surrounding slots to also be filled as part of the resolution process. As a result, future insertions may be affected. Clustering increases the likelihood of further collisions and can degrade performance over time.

To reduce clustering, we can extend the linear probing technique by skipping slots when searching for the next available position. This method is referred to as **rehashing**. Specifically, the **"plus 3" probe** means that when a collision occurs, we don't look at the next slot sequentially, but instead skip ahead by three slots. This process helps distribute items more evenly and reduces clustering.

### General Rehashing Formula:
- For simple linear probing, the rehash function is given by:
  $$
  \text{new\_has} = \text{rehash}(\text{old\_hash})
  $$
  where 
  $$
  \text{rehash}(pos) = (pos + 1) \mod \text{size}
  $$

- For the "plus 3" probe, the rehash function becomes:
  $$
  \text{rehash}(pos) = (pos + 3) \mod \text{size}
  $$

- In general, the rehash function can be defined as:
  $$
  \text{rehash}(pos) = (pos + \text{skip}) \mod \text{size}
  $$

It is essential that the **skip value** is chosen so that all slots in the table will eventually be visited. If this condition is not met, some slots may remain unused, leading to inefficiency. To ensure that all slots are checked, it is commonly recommended that the size of the hash table be a **prime number**. This helps in avoiding patterns where certain slots are consistently skipped, thus improving the distribution of items across the hash table.

A variation of linear probing is called **quadratic probing**. Instead of using a constant skip value, quadratic probing increments the hash value by successive perfect squares: 1, 3, 5, 7, 9, and so on. This means that if the first hash value is $h$, the subsequent values will be $h+1$, $h+4$, $h+9$, $h+16$, and so on.

### General Rehashing Formula for Quadratic Probing:  
The rehash function in quadratic probing is defined as:
$$
\text{rehash}(pos) = (h + i^2) \mod \text{size}
$$
where:
- $h$ is the initial hash value,
- $i$ is the number of attempts (starting from 0), and
- $\text{size}$ is the size of the hash table.

In this method, the skip value is based on the square of the attempt number, meaning for each subsequent collision, the hash value will increase by the square of the attempt count. Quadratic probing helps reduce clustering by avoiding the patterns created in linear probing.

### Chaining
In chaining, each slot in the hash table contains a reference to a collection (or chain) of items. When collisions occur, the item is placed in the same slot, but within a collection, typically implemented as a linked list or another data structure. As items accumulate in a slot, the time to search for an item in that slot may increase. Here’s a simplified representation of how chaining works:

```
Index | Items (Chained)  
-----------------------
  0   | [Item1, Item7]
  1   | [Item2]
  2   | []
  3   | [Item3, Item5, Item9]
  4   | [Item4]
  5   | []
  6   | [Item6]
```

**Search Process:**
When searching for an item, the hash function determines which slot it should be in. If there are multiple items in that slot (i.e., a chain), a linear search is performed within the chain. 

**Advantages of Chaining:**
- Chaining allows us to handle collisions by placing multiple items in the same slot.
- On average, fewer items end up in each slot, which can lead to faster searches compared to open addressing, especially as the number of items grows.

## Analysis of Hashing

In hashing, the **load factor** ($\lambda$) plays a crucial role in determining the performance of the hash table. The load factor is defined as:

$$
\text{Load Factor} (\lambda) = \frac{\text{Number of elements}}{\text{Number of slots}}
$$

A smaller load factor indicates fewer collisions, which means items are more likely to be placed in their correct slots, leading to faster search times. On the other hand, a larger load factor suggests that the table is filling up, increasing the likelihood of collisions. This results in more comparisons during collision resolution and can slow down the search process.

With **chaining** as a collision resolution method, higher collisions lead to longer chains, thus requiring more comparisons to find an item. Therefore, maintaining an optimal load factor is crucial to balancing search efficiency and space utilization in a hash table.


# Work needed - need to derive mathematically the successful and unsuccessful search
refer [this](https://www.cs.oberlin.edu/~bob/cs151.spring17/Class%20Examples%20and%20Notes/April/April%205/HashMapAnalysis.pdf)

# Implementing Python's Dictionary

A dictionary is a highly useful collection in Python, commonly known as an associative data type, where key-value pairs are stored. The key is used to efficiently retrieve the corresponding data value. This idea is often referred to as a **map**.

## Map Abstract Data Type (ADT)

A map is an unordered collection of key-value pairs, where each key is unique, ensuring a one-to-one relationship between the key and its associated value. Here are the typical operations supported by a map:

| Operation        | Time Complexity   | Space Complexity |
|------------------|-------------------|------------------|
| `Map()`          | O(1)              | O(1)             |
| `put(key, val)`  | O(1) on average   | O(1)             |
| `get(key)`       | O(1) on average   | O(1)             |
| `del`            | O(1) on average   | O(1)             |
| `size()`         | O(1)              | O(1)             |
| `key in map`     | O(1) on average   | O(1)             |

- **Time Complexity:**
  - Most operations on a hash table (like `put`, `get`, `del`, `key in map`) typically take O(1) time on average because they involve direct indexing using the hash function.
  - In the case of hash collisions (e.g., chaining or open addressing), the operations may take longer in some cases, but they still tend to perform in constant time on average due to the hash table's design.

- **Space Complexity:**
  - The space complexity is O(1) for each operation because the map only stores the key-value pairs in a hash table, which requires space proportional to the number of elements in the map.
  - 
### Efficiency of Lookups

One of the key advantages of a dictionary is that it supports fast lookup. Given a key, we can quickly retrieve the associated value. This is possible because dictionaries are typically implemented using a **hash table**. In a hash table, looking up an item can approach **O(1)** time complexity, meaning constant time. This makes hash tables ideal for scenarios where efficient searching is essential, such as with large datasets, as opposed to using slower data structures like lists with sequential or binary search methods.

## Implementation

Checkout the code [here](./dictionary.py)

# Sorting

Sorting is the process of arranging elements in a specific order, such as alphabetically, by size, or by other attributes. For example, a list of words can be sorted alphabetically, and a list of cities can be sorted by population or area. Sorting is important because it optimizes many algorithms, like binary search, and allows for easier data manipulation.

There are many sorting algorithms that have been developed, each with its advantages and drawbacks. Sorting efficiency is crucial, particularly for large datasets, as it can require significant computational resources. While simpler sorting methods may work for smaller datasets, complex algorithms become more useful as the size of the collection increases.

When analyzing sorting algorithms, two primary operations are measured:
1. **Comparisons**: The number of times two values are compared to determine their relative order.
2. **Exchanges**: The number of times values need to be swapped to place them in the correct order.

These operations help evaluate the efficiency of sorting algorithms.

## Bubble Sort

Bubble sort is a simple sorting algorithm that repeatedly traverses a list, comparing adjacent items, and swapping them if they are in the wrong order. Each pass ensures that the largest unsorted element "bubbles" up to its correct position.

### Process:
1. On the first pass, the algorithm compares and possibly swaps adjacent items. After the first pass, the largest item will be placed in its correct position at the end of the list.
2. On the second pass, the largest item is already sorted, so the algorithm only needs to compare the remaining $n - 1$ items. This continues until only the smallest item remains unsorted.
3. The process repeats for $n - 1$ passes (where $n$ is the total number of items). After $n - 1$ passes, the list will be completely sorted.

### Early Stopping
A bubble sort is often considered the most inefficient sorting method since it must exchange items before the final location is known. These “wasted” exchange operations are very costly. However, because the bubble sort makes passes through the entire unsorted portion of the list, it has the capability to do something most sorting algorithms cannot. In particular, if during a pass there are no exchanges, then we know that the list must be sorted. A bubble sort can be modified to stop early if it finds that the list has become sorted. This means that for lists that require just a few passes, a bubble sort may have an advantage in that it will recognize the sorted list and stop.

### Efficiency:
- **Best Case**: If the list is already sorted, bubble sort will still go through the entire list one time, making comparisons without needing any swaps. This results in a time complexity of $O(n)$ in the best case (with an optimized version of the algorithm that checks for swaps).
- **Worst Case**: In the worst case, where the list is sorted in reverse order, bubble sort will perform $O(n^2)$ comparisons and swaps.
 
### Implementation
Check out the implementation of bubble sort [here](./bubbleSort.py).

### Unique Characteristics of Bubble Sort

1. **Simple and Intuitive**: Easy to understand and implement, often used for teaching sorting concepts.
2. **Comparison-Based**: Compares adjacent elements and swaps them if needed.
3. **Time Complexity**:  
   - Worst/Average Case: $O(n^2)$
   - Best Case (already sorted): $O(n)$ (adaptive).
4. **Stable**: Preserves the relative order of equal elements.
5. **In-Place Sorting**: Requires only $O(1)$ extra memory.
6. **Inefficient for Large Data**: Performs poorly on large datasets due to quadratic time complexity.
7. **Optimizable**: Variants like optimized bubble sort can terminate early if no swaps are needed in a pass.
8. **Partial Stop**: If the algorithm stops after the x-th pass, the largest x elements will be correctly sorted at the end of the list, providing partial sorting that can be useful in certain contexts.