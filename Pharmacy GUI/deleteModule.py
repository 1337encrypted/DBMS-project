import mysql.connector
from connectionModule import dbConnect

def deleteRecord(data):
    conn = dbConnect()
    c = conn.cursor()
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS EMPLOYEE(NAME varchar(20), AGE int, PH_NO varchar(10), EMPLOYEE_ID int, SHIFT_TIME varchar(20))""")
        
        c.execute("DELETE FROM EMPLOYEE WHERE EMPLOYEE_ID = '" + str(data) + "'")
        print("Record successfully deleted")
        conn.commit()
        conn.close()
    except mysql.connector.Error as err:
        print("+++++++++++++++++++++++++++++++++++++++++USER DEFINED EXCEPTION+++++++++++++++++++++++++++++++++++++++++")
        #print(err)
        print("Message: ", err.msg)
        print("Error Code: ", err.errno)
        print("SQLSTATE: ", err.sqlstate)
        print("+++++++++++++++++++++++++++++++++++++++++++END OF EXCEPTION+++++++++++++++++++++++++++++++++++++++++++++")
