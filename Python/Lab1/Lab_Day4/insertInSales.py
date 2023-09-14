# function for inserting a record in salesperson table

import pyodbc

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


# INSERT statement 
#  
sqlqueryvar = "INSERT INTO salesperson (emp_no,first_name,last_name,dept_no,salary,sales_target,county,post_code,tel,notes) VALUES (80, 'Arti','Singh',1,10000,12,'Kent','KT19 5YY','012345','Learning DevOps')"

insertresult = run_sql(sqlqueryvar)
print(insertresult)

## 