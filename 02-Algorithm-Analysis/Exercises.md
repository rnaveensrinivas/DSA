# Exercises

### 1. What is the Big O performance of the following code fragment?

```python
for i in range(n):
    for j in range(n):
        k = 2 + 2
```

<details>
<summary>Click to view answer</summary>

The code contains two nested loops, each running `n` times. This results in a time complexity of $O(n^2)$.

</details>

### 2. What is the Big O performance of the following code fragment?

```python
for i in range(n):
        k = 2 + 2
```

<details>
<summary>Click to view answer</summary>

The loop runs `n` times, resulting in a time complexity of $O(n)$.

</details>

### 3. What is the Big O performance of the following code fragment?

```python
i = n
while i > 0:
    k = 2 + 2
    i = i // 2
```

<details>
<summary>Click to view answer</summary>

This is a logarithmic loop, where `i` is halved on each iteration. The time complexity is $O(\log n)$.

</details>

### 4. What is the Big O performance of the following code fragment?

```python
for i in range(n):
    for j in range(n):
        for k in range(n):
            k = 2 + 2
```

<details>
<summary>Click to view answer</summary>

There are three nested loops, each running `n` times. The time complexity is $O(n^3)$.

</details>

### 5. What is the Big O performance of the following code fragment?

```python
for i in range(n):
    k = 2 + 2
for j in range(n):
    k = 2 + 2
for k in range(n):
    k = 2 + 2
```

<details>
<summary>Click to view answer</summary>

There are three consecutive loops, each running `n` times, but since they are not nested, the total complexity is $O(n)$.

</details>


### 6. Devise an experiment to verify that the list index operator is O(1).
#### [Code](./time-it-list-index.py)

### 7. Devise an experiment to verify that get item and set item are O(1) for dictionaries.
#### [Code](./time-it-dictionary-get-set.py)

### 8. Devise an experiment that compares the performance of the del operator on lists and dictionaries.
#### [Code](./time-it-del-operator.py)

### 9 & 10. Given a list of numbers in random order, write an algorithm that works in O(n log n) to find the k-th smallest number in the list. Can you improve the algorithm from the previous problem to be linear? Explain.
#### [Code](./kth-smallest-element.py)
