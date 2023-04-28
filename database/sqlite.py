import sqlite3

# connecting to the database
connection = sqlite3.connect("cap23")

# cursor
cursor = connection.cursor()


sql_command = """
CREATE TABLE 
emp (
staff_number INTEGER PRIMARY KEY,
fname VARCHAR(20),
lname VARCHAR(30),
gender CHAR(1),
joining DATE
);"""
 
# execute the statement
cursor.execute(sql_command)
print('nice')
connection.close()