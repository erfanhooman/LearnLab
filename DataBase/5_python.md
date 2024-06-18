```python
import sqlite3

# This line creates a connection to an SQLite database file named sp.sqlite
conn = sqlite3.connect('sp.sqlite')
# If the database file doesn't exist, SQLite will create a new one
# The conn variable now holds a connection object that you'll use to interact with the database.

# This line creates a cursor object (c) using the cursor() method of the connection object (conn).
c = conn.cursor()
# A cursor acts like a pointer within the database, allowing you to execute SQL statements and fetch results.

# this line executes an SQL query using the execute() method of the cursor object (c).
r1 = c.execute('select * from "s";')
# The execute() method returns a cursor object (r1), which in this case holds the results of the query.

print(r1)

for m1 in r1:
# In each iteration, the current row of data from the results is assigned to the variable m1.
    print(m1)
    # Since m1 is a tuple containing the values from each column in the row, you'll see the data formatted as a tuple (e.g., (value1, value2, value3)) for each row. 

# This line closes the cursor object (c).
c.close()

# This line closes the connection to the database (conn).
conn.close()
```
---
#### This code showcases how you can leverage multiple cursors to execute queries on different tables within the same database connection
```python
import sqlite3
conn = sqlite3.connect('sp.sqlite')
c1 = conn.cursor()
c2 = conn.cursor()

r1 = c1.execute('select * from s;')
r2 = c2.execute('select * from p;') 
print('S')

for m1 in r1:
    print(m1)

print('P')
for m1 in r2:
    print(m1)
 
c1.close()
c2.close()
conn.close()
```

---
```python
import sqlite3
conn = sqlite3.connect('sp.sqlite')
c2 = conn.cursor()

r2 = c2.execute('select * from p;')

print(c2.fetchone())
print(c2.fetchone())
# These lines demonstrate the fetchone() method. Each time you call c2.fetchone(),
# it retrieves and prints the next row of data from the results for table "p" held by the c2 cursor.


print(r2.fetchone())
# r2 is just a reference to the result set produced by c2.execute('select * from p;')
# so they are effectively the same operation


c2.close()
conn.close()
```