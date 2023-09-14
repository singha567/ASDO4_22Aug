# Labs for Automating Database Tasks Using Python Programming Language 
# Part 1 – Create Table
# Part 2 – Practice Executing Insert Commands
# Part 3 – Practice Executing an Update Command
# select data

import pyodbc

# Function for select query to use fetchall
def run_select(sqlvar):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    try:
       result = cur.execute(sqlvar).fetchall()
    except Exception as e:
        print(e)
        result = None
    conn.commit()
    cur.close()
    return result


#Function for DDL, DML queries
def run_sql(sqlvar):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    try:
       result = cur.execute(sqlvar)
    except Exception as e:
        print(e)
        result = None
    conn.commit()
    cur.close()
    return result

# Drop table
sqlqueryvar = 'DROP TABLE Student'
create_qry = run_sql(sqlqueryvar)
print(create_qry)

# CREATE statement
sqlqueryvar = "CREATE TABLE Student ( StudentID int NOT NULL, FirstName nvarchar(40) NOT NULL, Surname nvarchar(30) NULL, Course nvarchar(30) NULL, City nvarchar(15) NULL )"
create_qry = run_sql(sqlqueryvar)
print(create_qry)

# INSERT statement   
insertRows = ["INSERT INTO Student VALUES (1,'Arti','Singh','DevOps','Kent')",
              "INSERT INTO Student VALUES (2,'Tom','Hardy','Acting','Paphos')",
              "INSERT INTO Student VALUES (3,'ABC','','DevOps','London')",
              "INSERT INTO Student VALUES (4,'XYZ','','','')",
              "INSERT INTO Student VALUES (5,'Sam','Strange','Developer','Basingstoke')"]

for i in insertRows:
    run_sql(i)

#SELECT statement
sqlqueryvar = 'SELECT * FROM Student'
create_qry = run_select(sqlqueryvar)
print(create_qry)

#UPDATE statement
sqlqueryvar = "UPDATE Student set firstname = 'Dummy' WHERE studentid =4"
create_qry = run_sql(sqlqueryvar)
print(create_qry)

#SELECT statement
sqlqueryvar = 'SELECT * FROM Student'
create_qry = run_select(sqlqueryvar)
print(create_qry)
## 