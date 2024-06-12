# Normalization

## Introduction

a technique of organizing a data in multiply table to minimize data redundancy
data redundancy lead to lots of problem including increase the size of database, insertion, deletion, updation

suppose we have a table of the student_id, student detail and department_id and department detail
### insertion anomaly:
- if we have to add a new data we should add the same data again for it
- if we add a new student we should write a same department detail for it

### deletion anomaly: 
- if we delete all student we also delete the data about department

### updation anomaly: 
- if we update the detail of the department we should update for all the student in the same department

### how the normalization solve the problem ? 
- normalization break the table into the two table one for a student and one for a department

### Type of the Normalization:
1. 1st Normal Form
2. 2nd Normal Form
3. 3rd Normal Form
4. BCNF

---
## 1st Normal Form:
Scalable Table design which can be easily extended <br />
**Functional Dependency:** Here, we don't even need fancy terms. 
A functional dependency in 1NF simply means each record (book) in a table must have a unique identifier 
(like an ISBN number) that determines all the other information in that record (title, author, etc.). 
Imagine a book without a unique ISBN - complete chaos! there are 4 basic rules that a table should follow to be 
in 1st normal form

**There are 4 rules two follow in 1NF :**

1. each column should not contain multiply value
```
| rollno | name     | Subject |
|--------|----------|---------|
| 1      | Michale  | C, C++  |
| 2      | Travis   | Python  |
| 3      | Franklin | JS      |
```
you should convert this table to this:
```
| rollno | name     | Subject |
|--------|----------|---------|
| 1      | Michale  | C       |
| 2      | Travis   | Python  |
| 3      | Franklin | JS      |
| 1      | Michale  | C++     |
```

2. each column should contain a value of same type
3. each column should have a unique name
4. oder of saving data is not matter
---

## 2nd Normal Form:
- first of all A table in 2NF must also adhere to all the rules of 1NF
- **Elimination of partial dependencies:** <br />
This is the key concept of 2NF. A partial dependency occurs when a non-key attribute 
(attribute not part of the primary key) relies on only a part of the primary key, rather than the entire key,
to uniquely identify a record.

#### Example:
Imagine a table storing student information:
```
| student_id | student_name | major_id | major_name |
|------------|--------------|----------|------------| as you can see the primary key is student_id + major_id
| 1          | Michale      | 1        | C          | but something like major name only depends on major_id
| 1          | Michale      | 2        | C++        | this called partial dependencies
| 2          | Travis       | 3        | Python     |
| 3          | Franklin     | 4        | JS         |
```
To achieve 2NF, you would separate the table into two:
```
A: 

| student_id | name     |
|------------|----------|
| 1          | Michale  |
| 2          | Travis   |
| 3          | Franklin |
| 4          | Jim      |

B: 

| major_id     | name     |
|--------------|----------|
| 1            | C        |
| 2            | C++      |
| 3            | Python   |
| 4            | Js       |

C: 

| Professor_id | Major  _id |
|--------------|------------|
| 1            | 3          |
| 2            | 3          |
| 3            | 2          |
| 3            | 1          |
```

---

## 3rd Normal Form:
- again table in 3NF must also adhere to all the rules of 2NF
- **No Transitive Dependencies**: <br />
There should be no indirect dependencies between non-key attributes (attributes not part of any candidate key) 
and the primary key. In simpler terms, imagine attribute A determines attribute B, and B determines attribute C. 
In 3NF, C must directly depend on the primary key, not just through B.

#### Example:
lets assume that our C table from previous example also have some detail on it
```
| student_id   | Major_id | exam_name | total_marks |
|--------------|----------|-----------|-------------|
| 1            | 3        | Midterms  | 25          | the total marks relies on non-key attr (exam_name)
| 2            | 3        | Final     | 50          | that means we have transitive dependecies
| 3            | 2        | Midterms  | 25          |
| 3            | 1        | Midterms  | 25          |
```
the exam_name is related to the the student and major but the total_marks depends on the exam so we have to convert 
exam into the new table
```
A: 
| student_id   | Major_id | exam_name |
|--------------|----------|-----------|
| 1            | 3        | Midterms  |
| 2            | 3        | Final     |
| 3            | 2        | Midterms  |
| 3            | 1        | Midterms  |

B: 
| exam_name | toatl_marks |
|-----------|-------------|
| Midterm   | 25          |
| Final     | 50          |
```
---

## Boyce-Codd Normal Form (BCNF):
- again table in BCNF must also adhere to all the rules of 3NF
- **BCNF (goes beyond 3NF)**: Requires that every determinant (part of the key that influences another attribute) 
must be a candidate key (a minimal set of attributes that uniquely identifies a row) itself

```
| student_id   | Major_id | exam_name |
|--------------|----------|-----------|
| 1            | 3        | Midterms  | as we can see student have a same Major with different exam
| 2            | 3        | Final     | we break the table in two table again and avoid this repeatation
| 3            | 2        | Midterms  |
| 3            | 1        | Midterms  |

A: 
| student_id | major_exam_id |
|------------|---------------|
| 1          | 1             |
| 2          | 2             |
| 3          | 3             |
| 3          | 4             |

B: 
| major_exam_id | major | exam     |
|---------------|-------|----------|
| 1             | 3     | Midterms |
| 2             | 3     | Final    |
| 3             | 2     | midterms |
| 4             | 2     | Final    |
| 5             | 1     | midterms |
| 5             | 1     | Final    |
```
---

## 4th Normal Form (4NF):
- again table in 4NF must also adhere to all the rules of BCNF
- table have at least 3 column
- it should not have Multi-Valued dependencies, An MVD exists when there's a single attribute (or set of attributes) 
in a table that determines multiple values for another attribute (or set of attributes).

### Example:
getting back to the student table suppose we have something like this:
```
| student_id | name     | Hobby      | Phone_number |
|------------|----------|------------|--------------|
| 1          | Michale  | Volleyball | 090          | as you can see we have a repeat of the student 
| 1          | Michale  | Football   | 090          | becuse one student can have multiply hobby and phone
| 2          | Travis   | Football   | 080          | 
| 2          | Travis   | Football   | 070          | 
| 3          | Franklin | Volleyball | 040          |
| 4          | Jim      | Football   | 010          |


in this case we can use the 4NF and devide the table in to the few table

A:
| student_id | name     |
|------------|----------|
| 1          | Michale  |
| 2          | Travis   |
| 3          | Franklin |
| 4          | Jim      |

B: 
| student_id | Hobby      |
|------------|------------|
| 1          | Volleyball |
| 1          | Football   |
| 2          | Football   |
| 3          | Volleyball |
| 4          | Football   |

C: 
| student_id | Phone_number |
|------------|--------------|
| 1          | 090          |
| 2          | 080          |
| 2          | 070          |
| 3          | 040          |
| 4          | 010          |
```


## Full Example from 1NF to 4NF:

### Initial Unnormalized Table:
We'll start with a table that contains student, course, instructor, and department information, but it's not normalized.
```
| student_id | student_name | course_id | course_name | instructor_name | instructor_office |    dept_name   | dept_head |
|------------|--------------|-----------|-------------|-----------------|-------------------|----------------|-----------|
| 1          | John Doe     | C101      | Math        | Dr. Smith       | Office 101        | Math Dept      | Dr. Brown |
| 1          | John Doe     | C102      | Physics     | Dr. Johnson     | Office 102        | Physics Dept   | Dr. Green |
| 2          | Jane Smith   | C101      | Math        | Dr. Smith       | Office 101        | Math Dept      | Dr. Brown |
| 2          | Jane Smith   | C103      | Chemistry   | Dr. Williams    | Office 103        | Chemistry Dept | Dr. White |
```

### First Normal Form (1NF):
1NF requires that the table have no repeating groups or arrays. Each column must contain only atomic (indivisible) values.
```
| student_id | student_name | course_id | course_name | instructor_name | instructor_office |    dept_name   | dept_head |
|------------|--------------|-----------|-------------|-----------------|-------------------|----------------|-----------|
| 1          | John Doe     | C101      | Math        | Dr. Smith       | Office 101        | Math Dept      | Dr. Brown |
| 1          | John Doe     | C102      | Physics     | Dr. Johnson     | Office 102        | Physics Dept   | Dr. Green |
| 2          | Jane Smith   | C101      | Math        | Dr. Smith       | Office 101        | Math Dept      | Dr. Brown |
| 2          | Jane Smith   | C103      | Chemistry   | Dr. Williams    | Office 103        | Chemistry Dept | Dr. White |
```

### Second Normal Form (2NF):
2NF requires that the table be in 1NF and that all non-key attributes are fully functionally dependent on the primary key.
Here, student_name, course_name, instructor_name, instructor_office, dept_name, and dept_head are not fully dependent 
on student_id and course_id.
```
A:
| student_id | student_name |
|------------|--------------|
| 1          | John Doe     |
| 2          | Jane Smith   |

B:
| course_id | course_name | instructor_name | instructor_office |
|-----------|-------------|-----------------|-------------------|
| C101      | Math        | Dr. Smith       | Office 101        |
| C102      | Physics     | Dr. Johnson     | Office 102        |
| C103      | Chemistry   | Dr. Williams    | Office 103        |

C: 
| dept_name      | dept_head |
|----------------|-----------|
| Math Dept      | Dr. Brown |
| Physics Dept   | Dr. Green |
| Chemistry Dept | Dr. White |

D: 
| student_id | course_id |
|------------|-----------|
| 1          | C101      |
| 1          | C102      |
| 2          | C101      |
| 2          | C103      |
```

### Third Normal Form (3NF):
3NF requires that the table be in 2NF and that all the attributes must be functionally dependent on the primary key 
and not on any other non-prime attribute.
```
| course_id | course_name | instructor_name |
|-----------|-------------|-----------------|
| C101      | Math        | Dr. Smith       |
| C102      | Physics     | Dr. Johnson     |
| C103      | Chemistry   | Dr. Williams    |

| instructor_name | instructor_office |
|-----------------|-------------------|
| Dr. Smith       | Office 101        |
| Dr. Johnson     | Office 102        |
| Dr. Williams    | Office 103        |

```