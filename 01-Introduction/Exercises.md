# Exercises

### 1. Construct a class hierarchy for people on a college campus. Include faculty, staff, and students. What do they have in common? What distinguishes them from one another?

<details>
<summary>Click to view Answer</summary>

```                        
             Person
               |
       ----------------
       |              |
    Employee        Student
       |                     
--------------
|            |          
Faculty    Staff    
```

#### Person
* **Attributes**
  - Name
  - Age
  - Gender
  - Contact Information
  - Address
* **Actions**
  - Update contact information
  - Request leave (if applicable)
  - Get full name
  - Change address

#### Employee (inherits from Person)
* **Attributes**
  - Employee ID
  - Department
  - Designation
  - Salary
  - Hiring Date
* **Actions**
  - Clock in/out
  - Submit leave request
  - Get salary details
  - Attend training sessions
  - Update employment status

#### Faculty (inherits from Employee)
* **Attributes**
  - Teaching Subjects
  - Research Interests
  - Courses Taught
  - Publications
* **Actions**
  - Create syllabus
  - Grade assignments
  - Conduct research
  - Hold office hours
  - Attend faculty meetings

#### Staff (inherits from Employee)
* **Attributes**
  - Job Role
  - Work Hours
  - Department
  - Shift
  - Supervisor
* **Actions**
  - Maintain records
  - Coordinate logistics
  - Support faculty and students
  - Manage supplies  

#### Student (inherits from Person)
* **Atrributes**
  - Student ID
  - Enrollment Date
  - Course/Program
  - Grade Point Average (GPA)
  - Major
* **Actions**
   - Register for courses
   - Submit assignments
   - Check grades
   - Request transcript
   - Enroll for exams
  
</details>

---

### 2. Construct a class hierarchy for bank accounts.

<details>
<summary>Click to view Answer</summary>

```                         
              BankAccount
                  |
       -----------------------
       |                     |
    SavingsAccount       CheckingAccount
       |                     |
CertificateOfDeposit    BusinessAccount
```

#### BankAccount
* **Attributes**
  - Account Number
  - Account Holder Name
  - Balance
  - Date Opened
  - Bank Name
* **Actions**
  - Deposit money
  - Withdraw money
  - View account details
  - Check balance
  - Close account

#### SavingsAccount (inherits from BankAccount)
* **Attributes**
  - Interest Rate
  - Minimum Balance
* **Actions**
  - Calculate interest
  - Enforce minimum balance

#### CertificateOfDeposit (inherits from SavingsAccount)
* **Attributes**
  - Maturity Date
  - Penalty for Early Withdrawal
* **Actions**
  - Calculate maturity value
  - Apply penalty for early withdrawal

#### CheckingAccount (inherits from BankAccount)
* **Attributes**
  - Overdraft Limit
  - Monthly Fee
* **Actions**
  - Write checks
  - Overdraft protection

#### BusinessAccount (inherits from CheckingAccount)
* **Attributes**
  - Business Name
  - Tax Identification Number
  - Transaction Limit
* **Actions**
  - Process payroll
  - Handle large transactions
  - Generate business statements

</details>

---

### 3. Construct a class hierarchy for different types of computers.

<details>
<summary>Click to view Answer</summary>

```                         
               Computer
                  |
       -----------------------
       |                     |
PersonalComputer           Server
       |                     |
DesktopComputer       MainframeComputer
       |
     Laptop
```

#### Computer
* **Attributes**
  - Processor
  - RAM
  - Storage
  - Operating System
  - Manufacturer
* **Actions**
  - Power on/off
  - Execute programs
  - Install software
  - Connect to a network

#### PersonalComputer (inherits from Computer)
* **Attributes**
  - Graphics Card
  - Peripheral Devices
* **Actions**
  - Customize hardware
  - Install personal software

#### DesktopComputer (inherits from PersonalComputer)
* **Attributes**
  - Tower Size
  - External Monitor Support
* **Actions**
  - Connect external devices
  - Upgrade components

#### Laptop (inherits from PersonalComputer)
* **Attributes**
  - Battery Life
  - Weight
  - Screen Size
* **Actions**
  - Operate on battery
  - Portable usage

#### Server (inherits from Computer)
* **Attributes**
  - Rack Size
  - Number of Processors
  - Uptime
* **Actions**
  - Manage network resources
  - Host applications
  - Handle concurrent users

#### MainframeComputer (inherits from Server)
* **Attributes**
  - Processing Power
  - Scalability
  - Redundancy Features
* **Actions**
  - Handle bulk data processing
  - Support thousands of users
  - Ensure high availability

</details>

---

### 4. Using the classes provided in the chapter, interactively construct a circuit and test it.
#### [Code](./LogicGate.py)

---

### 5. Implement the simple methods get_num and get_den that will return the numerator and denominator of a fraction.
#### [Code](./Fraction.py)
---

### 6. In many ways it would be better if all fractions were maintained in lowest terms right from the start. Modify the constructor for the Fraction class so that GCD is used to reduce fractions immediately. Notice that this means the __add__ function no longer needs to reduce. Make the necessary modifications.
#### [Code](./Fraction.py)
---

### 7. Implement the remaining simple arithmetic operators (__sub__, __mul__, and __truediv__).
#### [Code](./Fraction.py)
---

### 8. Implement the remaining relational operators (__gt__, __ge__, __lt__, __le__, and __ne__).
#### [Code](./Fraction.py)
---

### 9. Modify the constructor for the fraction class so that it checks to make sure that the numerator and denominator are both integers. If either is not an integer, the constructor should raise an exception.
#### [Code](./Fraction.py)
---

### 10. In the definition of fractions we assumed that negative fractions have a negative numerator and a positive denominator. Using a negative denominator would cause some of the relational operators to give incorrect results. In general, this is an unnecessary constraint. Modify the constructor to allow the user to pass a negative denominator so that all of the operators continue to work properly.
#### [Code](./Fraction.py)
---

### 11. Research the __radd__ method. How does it differ from __add__? When is it used? Implement __radd__.
#### [Code](./Fraction.py)
---

### 12. Repeat the last question but this time consider the __iadd__ method.
#### [Code](./Fraction.py)
---

### 13. Research the __repr__ method. How does it differ from __str__? When is it used? Implement __repr__.
#### [Code](./Fraction.py)

---

### 14. Research other types of gates that exist (such as NAND, NOR, and XOR). Add them to the circuit hierarchy. How much additional coding did you need to do?
#### [Code](./LogicGate.py)
---

### 15. The most simple arithmetic circuit is known as the half adder. Research the simple half-adder circuit. Implement this circuit.
#### [Code](./halfAdder.py)
---

### 16. Now extend that circuit and implement an 8-bit full adder.
#### [Code](./eightBitFullAdder.py)


---

### 17. The circuit simulation shown in this chapter works in a backward direction. In other words, given a circuit, the output is produced by working back through the input values, which in turn cause other outputs to be queried. This continues until external input lines are found, at which point the user is asked for values. Modify the implementation so that the action is in the forward direction; upon receiving inputs the circuit produces an output.
#### Low priority, hence skipped.
---

### 18. Design a class to represent a playing card and another one to represent a deck of cards. Using these two classes, implement your favorite card game.
#### [Code](./cardGame.py)
---

### 19. Find a Sudoku puzzle online or in the local newspaper. Write a program to solve the puzzle.

---

