import mysql.connector as mysql

def dbConnect():
    try:
        con = mysql.connect(host='localhost', port='3306', user='root', password='root', database='pharmacydb')
        #print(con)
    except mysql.connector.Error as err:
        print("+++++++++++++++++++++++++++++++++++++++++USER DEFINED EXCEPTION+++++++++++++++++++++++++++++++++++++++++")
        #print(err)
        print("Error Code: ", err.errno)
        print("SQLSTATE: ", err.sqlstate)
        print("Message: ", err.msg)
        print("+++++++++++++++++++++++++++++++++++++++++++END OF EXCEPTION+++++++++++++++++++++++++++++++++++++++++++++")
    return con
