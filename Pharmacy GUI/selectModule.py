import mysql.connector
from connection import dbConnect

def read():
    conn = dbConnect()
    c = conn.cursor()
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS EMPLOYEE(NAME varchar(20), AGE int, PH_NO varchar(10), EMPLOYEE_ID int, SHIFT_TIME varchar(20))""")
        c.execute("SELECT * FROM EMPLOYEE")
        results = c.fetchall()
        print("Records selected")
        conn.close()
        return results
    except mysql.connector.Error as err:
        print("+++++++++++++++++++++++++++++++++++++++++USER DEFINED EXCEPTION+++++++++++++++++++++++++++++++++++++++++")
        #print(err)
        print("Message: ", err.msg)
        print("Error Code: ", err.errno)
        print("SQLSTATE: ", err.sqlstate)
        print("+++++++++++++++++++++++++++++++++++++++++++END OF EXCEPTION+++++++++++++++++++++++++++++++++++++++++++++")

