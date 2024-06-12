```python
import sqlite3

# This line creates a connection to an SQLite database file named sp.sqlite
conn = sqlite3.connect('sp.sqlite')
# If the database file doesn't exist, SQLite will create a new one
# The conn variable now holds a connection object that you'll use to interact with the database.

# This line creates a cursor object (c) using the cursor() method of the connection object (conn).
c = conn.cursor()
# A cursor acts like a pointer within the database, allowing you to execute SQL statements and fetch results.


r1 = c.execute('select * from "s";')
print(r1)
for m1 in r1:
    print(m1)
c.close()
conn.close()
```