import mysql.connector
from connectionModule import dbConnect

def update(Name, Age, Phone, Id, Shift, idName):
    conn = dbConnect()
    c = conn.cursor()
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS EMPLOYEE(NAME varchar(20), AGE int, PH_NO varchar(10), EMPLOYEE_ID int, SHIFT_TIME varchar(20))""")
        
        c.execute("UPDATE EMPLOYEE SET NAME = '" + str(Name) + "', AGE = '" + str(Age) + "', PH_NO = '" + str(Phone) + "',EMPLOYEE_ID = '" + str(Id) + "',SHIFT_TIME = '" + str(Shift) + "' WHERE EMPLOYEE_ID='"+str(Id)+"'")
        print("Record successfully updated")
        conn.commit()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("+++++++++++++++++++++++++++++++++++++++++USER DEFINED EXCEPTION+++++++++++++++++++++++++++++++++++++++++")
        #print(err)
        print("Message: ", err.msg)
        print("Error Code: ", err.errno)
        print("SQLSTATE: ", err.sqlstate)
        print("+++++++++++++++++++++++++++++++++++++++++++END OF EXCEPTION+++++++++++++++++++++++++++++++++++++++++++++")

    except IndexError:
        print('index out of range exception')
        print("+++++++++++++++++++++++++++++++++++++++++++END OF EXCEPTION+++++++++++++++++++++++++++++++++++++++++++++")

