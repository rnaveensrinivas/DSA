# Exercises

### 1. Convert the following values to binary using the Divide by 2 algorithm. Show the stack of remainders.

- 17
- 45
- 96

<details>
<summary>Click to view answer</summary>

#### 1. Convert 17 to binary:

| Division ($\div 2$) | Quotient ($\text{Quotient}$) | Remainder (Digit) | Position ($\text{Position}$) |
|--------------------:|----------------------------:|------------------:|----------------------------:|
| $17 \div 2$         | $8$                        | $1$               | $0$                         |
| $8 \div 2$          | $4$                        | $0$               | $1$                         |
| $4 \div 2$          | $2$                        | $0$               | $2$                         |
| $2 \div 2$          | $1$                        | $0$               | $3$                         |
| $1 \div 2$          | $0$                        | $1$               | $4$                         |

Binary: $(10001)_2$

---

#### 2. Convert 45 to binary:

| Division ($\div 2$) | Quotient ($\text{Quotient}$) | Remainder (Digit) | Position ($\text{Position}$) |
|--------------------:|----------------------------:|------------------:|----------------------------:|
| $45 \div 2$         | $22$                       | $1$               | $0$                         |
| $22 \div 2$         | $11$                       | $0$               | $1$                         |
| $11 \div 2$         | $5$                        | $1$               | $2$                         |
| $5 \div 2$          | $2$                        | $1$               | $3$                         |
| $2 \div 2$          | $1$                        | $0$               | $4$                         |
| $1 \div 2$          | $0$                        | $1$               | $5$                         |

Binary: $(101101)_2$

---

#### 3. Convert 96 to binary:

| Division ($\div 2$) | Quotient ($\text{Quotient}$) | Remainder (Digit) | Position ($\text{Position}$) |
|--------------------:|----------------------------:|------------------:|----------------------------:|
| $96 \div 2$         | $48$                       | $0$               | $0$                         |
| $48 \div 2$         | $24$                       | $0$               | $1$                         |
| $24 \div 2$         | $12$                       | $0$               | $2$                         |
| $12 \div 2$         | $6$                        | $0$               | $3$                         |
| $6 \div 2$          | $3$                        | $0$               | $4$                         |
| $3 \div 2$          | $1$                        | $1$               | $5$                         |
| $1 \div 2$          | $0$                        | $1$               | $6$                         |

Binary: $(1100000)_2$



</details>

### 2. Convert the following infix expressions to prefix (use full parentheses):

- $(A + B) * ( C + D) * (E + F)$
- $A + ((B + C) * (D + E))$
- $A * B * C * D + E + F$

<details>
<summary>Click to view answer</summary>

- $(A + B) * ( C + D) * (E + F)$  
  - Prefix Conversion:  
    - $(((A + B) * (C + D)) * (E + F))$  
    - $* * + A B + C D + E F$  

- $A + ((B + C) * (D + E))$  
  - Prefix Conversion:  
    - $(A + ((B + C) * (D + E)))$  
    - $+ A * + B C + D E$  

- $A * B * C * D + E + F$  
  - Prefix Conversion:  
    - $(((((A * B) * C) * D) + E) + F)$  
    - $+ + * * * A B C D E F$

</details>

### 3. Convert the above infix expressions to postfix (use full parentheses).

<details>
<summary>Click to view answer</summary>

- $(A + B) * (C + D) * (E + F)$  
  - Postfix Conversion:  
    - $(((A + B) * (C + D)) * (E + F))$  
    - $((A B +) (C D +) *) (E F +) *$  
    - $A B + C D + * E F + *$  

- $A + ((B + C) * (D + E))$  
  - Postfix Conversion:  
    - $(A + ((B + C) * (D + E)))$  
    - $A (B C +) (D E +) * +$  
    - $A B C + D E + * +$  

- $A * B * C * D + E + F$  
  - Postfix Conversion:  
    - $((((A * B) * C) * D) + E) + F$  
    - $A B * C * D * E + F +$  

</details>

### 4. Convert the above infix expressions to postfix using the direct conversion algorithm. Show the stack as the conversion takes place.
<details>
<summary>Click to view answer</summary>
### 4. Convert the above infix expressions to postfix using the direct conversion algorithm. Show the stack as the conversion takes place.

#### Expression 1: $(A + B) * (C + D) * (E + F)$  

| Step | Symbol  | Stack  | Postfix                |
|------|---------|--------|------------------------|
| 1    | `(`     | `(`    |                        |
| 2    | `A`     | `(`    | `A`                    |
| 3    | `+`     | `(+`   | `A`                    |
| 4    | `B`     | `(+`   | `A B`                  |
| 5    | `)`     |        | `A B +`                |
| 6    | `*`     | `*`    | `A B +`                |
| 7    | `(`     | `*(`   | `A B +`                |
| 8    | `C`     | `*(`   | `A B + C`              |
| 9    | `+`     | `*(+`  | `A B + C`              |
| 10   | `D`     | `*(+`  | `A B + C D`            |
| 11   | `)`     | `*`    | `A B + C D +`          |
| 12   | `*`     | `*`    | `A B + C D + *`        |
| 13   | `(`     | `*(`   | `A B + C D +`          |
| 14   | `E`     | `*(`   | `A B + C D + E`        |
| 15   | `+`     | `*(+`  | `A B + C D + E`        |
| 16   | `F`     | `*(+`  | `A B + C D + E F`      |
| 17   | `)`     | `*`    | `A B + C D + E F +`    |
| 18   | End     |        | `A B + C D + * E F + *`|

**Postfix**: $A B + C D + * E F + *$  

---

#### Expression 2: $A + ((B + C) * (D + E))$  

| Step | Symbol | Stack   | Postfix            |
|------|--------|-------- |--------------------|
| 1    | `A`    |         | `A`                |
| 2    | `+`    | `+`     | `A`                |
| 3    | `(`    | `+(`    | `A`                |
| 4    | `(`    | `+((`   | `A`                |
| 5    | `B`    | `+((`   | `A B`              |
| 6    | `+`    | `+((+`  | `A B`              |
| 7    | `C`    | `+((+`  | `A B C`            |
| 8    | `)`    | `+(`    | `A B C +`          |
| 9    | `*`    | `+(*`   | `A B C +`          |
| 10   | `(`    | `+(*(`  | `A B C +`          |
| 11   | `D`    | `+(*(`  | `A B C + D`        |
| 12   | `+`    | `+(*(+` | `A B C + D`        |
| 13   | `E`    | `+(*(+` | `A B C + D E`      |
| 14   | `)`    | `+(*`   | `A B C + D E +`    |
| 15   | `)`    | `+`     | `A B C + D E + *`  |
| 16   | End    |         | `A B C + D E + * +`|

**Postfix**: $A B C + D E + * +$  

---

#### Expression 3: $A * B * C * D + E + F$  

| Step | Symbol | Stack | Postfix                |
|------|--------|-------|------------------------|
| 1    | `A`    |       | `A`                    |
| 2    | `*`    | `*`   | `A`                    |
| 3    | `B`    | `*`   | `A B`                  |
| 4    | `*`    | `*`   | `A B *`                |
| 5    | `C`    | `*`   | `A B * C`              |
| 6    | `*`    | `*`   | `A B * C *`            |
| 7    | `D`    | `*`   | `A B * C * D`          |
| 8    | `+`    | `+`   | `A B * C * D *`        |
| 9    | `E`    | `+`   | `A B * C * D * E`      |
| 10   | `+`    | `+`   | `A B * C * D * E +`    |
| 11   | `F`    | `+`   | `A B * C * D * E + F`  |
| 12   | End    |       | `A B * C * D * E + F +`|

**Postfix**: $A B * C * D * E + F +$  

</details>

### 5. Evaluate the following postfix expressions. Show the stack as each operand and operator is processed.

- 2 3 · 4 +
- 1 2 + 3 + 4 + 5 +
- 1 2 3 4 5 · + · +

<details>
<summary>Click to view answer</summary>

### 1. Expression: **2 3 · 4 +**

| Step | Action              | Stack  |
|------|---------------------|--------|
| 1    | Push 2              | [2]    |
| 2    | Push 3              | [2, 3] |
| 3    | Process `·` (2 · 3) | [6]    |
| 4    | Push 4              | [6, 4] |
| 5    | Process `+` (6 + 4) | [10]   |

**Final Result**: **10**

---

### 2. Expression: **1 2 + 3 + 4 + 5 +**

| Step | Action               | Stack   |
|------|----------------------|---------|
| 1    | Push 1               | [1]     |
| 2    | Push 2               | [1, 2]  |
| 3    | Process `+` (1 + 2)  | [3]     |
| 4    | Push 3               | [3, 3]  |
| 5    | Process `+` (3 + 3)  | [6]     |
| 6    | Push 4               | [6, 4]  |
| 7    | Process `+` (6 + 4)  | [10]    |
| 8    | Push 5               | [10, 5] |
| 9    | Process `+` (10 + 5) | [15]    |

**Final Result**: **15**

---

### 3. Expression: **1 2 3 4 5 · + · +**

| Step | Action                 | Stack           |
|------|------------------------|-----------------|
| 1    | Push 1                 | [1]             |
| 2    | Push 2                 | [1, 2]          |
| 3    | Push 3                 | [1, 2, 3]       |
| 4    | Push 4                 | [1, 2, 3, 4]    |
| 5    | Push 5                 | [1, 2, 3, 4, 5] |
| 6    | Process `·` (4 · 5)    | [1, 2, 3, 20]   |
| 7    | Process `+` (3 + 20)   | [1, 2, 23]      |
| 8    | Process `·` (2 · 23)   | [1, 46]         |
| 9    | Process `+` (1 + 46)   | [47]            |

**Final Result**: **47**

---
</details>

### 6. The alternative implementation of the queue ADT is to use a list such that the rear of the queue is at the end of the list. What would this mean for Big-O performance?

### 7. What is the result of carrying out both steps of the linked list add method in reverse order? What kind of reference results? What types of problems may result?

### 8. Explain how the linked list remove method works when the item to be removed is in the last node.

### 9. Explain how the remove method works when the item is in the only node in the linked list.

### 10. Modify the infix-to-postfix algorithm so that it can handle errors.
#### [Code](./Stack/infixToPostfix.py)

### 11. Modify the postfix evaluation algorithm so that it can handle errors.
#### [Code](./Stack/postfixEvaluation.py)

### 12. Implement a direct infix evaluator that combines the functionality of infix-to-postfix conversion and the postfix evaluation algorithm. Your evaluator should process infix tokens from left to right and use two stacks, one for operators and one for operands, to perform the evaluation.
#### [Code](./Stack/infixEvaluation.py)

### 13. Turn your direct infix evaluator from the previous problem into a calculator.
#### [Code](./Stack/calculator.py)

### 14. Implement the queue ADT, using a list such that the rear of the queue is at the end of the list.

### 15. Design and implement an experiment to do benchmark comparisons of the two queue implementations. What can you learn from such an experiment?

### 16. Modify the hot potato simulation to allow for a randomly chosen counting value so that each pass is not predictable from the previous one.

### 17. Consider a real life situation. Formulate a question and then design a simulation that can help to answer it. Possible situations include:

- Cars lined up at a car wash
- Customers at a grocery store check-out
- Airplanes taking off and landing on a runway
- A bank teller

Be sure to state any assumptions that you make and provide any probabilistic data that must be considered as part of the scenario.

### 18. Implement a radix sorting machine. A radix sort for base 10 integers is a mechanical sorting technique that utilizes a collection of bins, one main bin and 10 digit bins. Each bin acts like a queue and maintains its values in the order that they arrive. The algorithm begins by placing each number in the main bin. Then it considers each value digit by digit. The first value is removed and placed in a digit bin corresponding to the digit being considered. For example, if the ones digit is being considered, 534 is placed in digit bin 4 and 667 is placed in digit bin 7. Once all the values are placed in the corresponding digit bins, the values are collected from bin 0 to bin 9 and placed back in the main bin. The process continues with the tens digit, the hundreds, and so on. After the last digit is processed, the main bin contains the values in order.

### 19. Another example of the parentheses matching problem comes from Hypertext Markup Language (HTML). In HTML, tags exist in both opening and closing forms and must be balanced to properly describe a web document. This very simple HTML document is intended only to show the matching and nesting structure for tags in the language. Write a program that can check an HTML document for proper opening and closing tags.:

```html
<html>
   <head>
      <title>
         Example
      </title>
   </head>

   <body>
      <h1>Hello, world</h1>
   </body>
</html>
```

#### [Code](./Stack/html_tag_validator.py)

### 20. Extend the program from Listing 3.15 to handle palindromes with spaces. For example, I PREFER PI is a palindrome that reads the same forward and backward if you ignore the blank characters.

### 21. To implement the size method, we counted the number of nodes in the list. An alternative strategy would be to store the number of nodes in the list as an additional piece of data in the head of the list. Modify the UnorderedList class to include this information and rewrite the size method.

### 22. Implement the remove method so that it works correctly in the case where the item is not in the list.

### 23. Modify the list classes to allow duplicates. Which methods will be impacted by this change?

### 24. Implement the __str__ method in the UnorderedList class. What would be a good string representation for a list?

### 25. Implement the __str__ method so that lists are displayed the Python way (with square brackets).

### 26. Implement the remaining operations defined in the unordered list ADT (append, index, pop, insert).

### 27. Implement a slice method for the UnorderedList class. It should take two parameters, start and stop, and return a copy of the list starting at the start position and going up to but not including the stop position.

### 28. Implement the remaining operations defined in the ordered list ADT.

### 29. Consider the relationship between unordered and ordered lists. Is it possible that inheritance could be used to build a more efficient implementation? Implement this inheritance hierarchy.

### 30. Implement a stack using linked lists.

### 31. Implement a queue using linked lists.

### 32. Implement a deque using linked lists.

### 33. Design and implement an experiment that will compare the performance of a Python list with a list implemented as a linked list.

### 34. Design and implement an experiment that will compare the performance of the Python list-based stack and queue with the linked list implementation.

### 35. The linked list implementation given above is called a singly linked list because each node has a single reference to the next node in the sequence. An alternative implementation is known as a doubly linked list. In this implementation, each node has a reference to the next node (commonly called next) as well as a reference to the preceding node (commonly called back). The head reference also contains two references, one to the first node in the linked list and one to the last. Code this implementation in Python.

### 36. Create an implementation of a queue that would have an average performance of  for enqueue and dequeue operations.
