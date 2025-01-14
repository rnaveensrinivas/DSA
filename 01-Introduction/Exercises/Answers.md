### Q1. Construct a class hierarchy for people on a college campus. Include faculty, staff, and students. What do they have in common? What distinguishes them from one another?

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

---
