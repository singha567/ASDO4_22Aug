
import pyodbc
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
conn = pyodbc.connect(connectionString)
cur = conn.cursor()
#result = cur.execute('SELECT * FROM company').fetchall()
#conn.close()
#for row in result:
#    print(row)


### mini lab 2
## Use between, like, <, in =

# between
print('******* between  *****')
result = cur.execute('SELECT first_name, dept_no FROM salesperson where dept_no between 2 and 3').fetchall()
for row in result:
    print(row)
result = cur.execute('SELECT first_name, salary FROM salesperson where salary between 12.00 and 14.00').fetchall()
for row in result:
    print(row)

print('***** like ****')
result = cur.execute('SELECT first_name, dept_no FROM salesperson where first_name like \'F%\'').fetchall()
for row in result:
    print(row)


print('****** < *****')
result = cur.execute('SELECT first_name, salary FROM salesperson where salary < 12.00').fetchall()
for row in result:
    print(row)

print('****** in ****')
result = cur.execute('SELECT first_name, salary FROM salesperson where dept_no in (1,3)').fetchall()
for row in result:
    print(row)

print('****** not in NULL ****')
result = cur.execute('SELECT first_name, post_code FROM salesperson where post_code not in (\'\')').fetchall()
for row in result:
    print(row)

print('****** = ****')
result = cur.execute('SELECT first_name, salary FROM salesperson where dept_no = 2').fetchall()
for row in result:
    print(row)

conn.close()

