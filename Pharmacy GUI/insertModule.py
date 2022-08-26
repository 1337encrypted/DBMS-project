import mysql.connector
from connection import dbConnect

def insert(Name, Age, Phone, Id, Shift):
    conn = dbConnect()
    c = conn.cursor()
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS EMPLOYEE(NAME varchar(20), AGE int, PH_NO varchar(10), EMPLOYEE_ID int, SHIFT_TIME varchar(20))""")

        c.execute("INSERT INTO employee VALUES ('" + str(Name) + "','" + str(Age) + "','" + str(Phone) + "','" + str(Id) + "','" + str(Shift) + "')")
        print("Successfull added record")
        conn.commit()
        conn.close()
    except mysql.connector.Error as err:
        print("+++++++++++++++++++++++++++++++++++++++++USER DEFINED EXCEPTION+++++++++++++++++++++++++++++++++++++++++")
        #print(err)
        print("Message: ", err.msg)
        print("Error Code: ", err.errno)
        print("SQLSTATE: ", err.sqlstate)
        print("+++++++++++++++++++++++++++++++++++++++++++END OF EXCEPTION+++++++++++++++++++++++++++++++++++++++++++++")
