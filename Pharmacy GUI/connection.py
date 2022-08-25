#CLASS
#dbConnect

#FUNCTIONS
#__init__

import mysql.connector as connector

class dbConnect:
    def __init__(self):
        try:
            self.con = connector.connect(host='localhost', port='3306', user='root', password='root', database='pharmacydb')
            self.cur = self.con.cursor()
            print(self.con)
        except:
            print("Dbconnect error")
