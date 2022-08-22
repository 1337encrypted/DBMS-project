#pip install mysql-connector for connecting to the database
import mysql.connector

def dbConnect():
    
    try:
        conn = mysql.connector.connect(host='localhost',user='root',password='root',database='pharmacydb')
        return conn
    except:
        print("Dbconnect error")

#def function(conn):
#    c = conn = dbConnect()

def main():
    conn = dbConnect()
    #function(conn)

if __name__ == '__main__':
    main()
