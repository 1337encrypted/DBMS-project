# +--------------------+-------------+------+-----+---------+-------+
# | Field              | Type        | Null | Key | Default | Extra |
# +--------------------+-------------+------+-----+---------+-------+
# | NAME               | varchar(30) | YES  |     | NULL    |       |
# | COST               | double      | YES  |     | NULL    |       |
# | TYPE               | varchar(20) | YES  |     | NULL    |       |
# | BARCODE            | int         | NO   | PRI | NULL    |       |
# | MANUFACTURING_DATE | date        | YES  |     | NULL    |       |
# | MANUFACTURER_NAME  | varchar(20) | YES  |     | NULL    |       |
# | EXPIRY_DATE        | date        | YES  |     | NULL    |       |
# +--------------------+-------------+------+-----+---------+-------+


# CLASS
from connection import dbConnect
drug

# FUNCTIONS
# def __init__(self):
# def __init__(self, con, name, cost, manufacturerName, manufactureDate, expiryDate, type, barcode):
# def createDrug(self):
# def insertDrug(self, name, cost, type, barcode, manufacturing_date, manufacturer_name, expiry_date):
# def fetchAll(self):
# def deleteDrug(self, barcode):
# def updateEmployee(self, name, cost, type, barcode, manufacturing_date, manufacturer_name, expiry_date):
# please fill this list


class drug:
    # default constructor
    def __init__(self):
        try:
            self.con = dbConnect()
            self.cur = self.con.cursor()
        except
        print("Database Error")
        self.name = ""
        self.cost = 0.0
        self.manufacturerName = ""
        self.manufactureDate = ""
        self.expiryDate = ""
        self.type = ""
        self.barcode = 0

    # parameterized constructor
    def __init__(self, con, name, cost, manufacturerName, manufactureDate, expiryDate, type, barcode):
        self.con = con
        self.cur = self.con.cursor()
        self.name = name
        self.cost = cost
        self.manufacturerName = manufacturerName
        self.manufactureDate = manufactureDate
        self.expiryDate = expiryDate
        self.type = type
        self.barcode = barcode

     # create table
    def createDrug(self):
        query = 'create table if not exists drug(name varchar(30),cost int,type varchar(20),barcode int primary key,manufacturing_date date,manufacturer_name varchar(20),expiry_date date)'
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("\nSuccessfull")

     # insert
    def insertDrug(self, name, cost, type, barcode, manufacturing_date, manufacturer_name, expiry_date):
        query = "insert into drug(name,cost,type,barcode,manufacturing_date,manufacturer_name,expiry_date) values('{}','{}','{}',{},'{}',{})"
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commmit()

     # fetch
    def fetchAll(self):
        query = "select * from drug"
        #cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)

    # delete
    def deleteDrug(self, barcode):
        query = "delete from drug where barcode = {} ".format(
            barcode)
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Delete")

    # update
    def updateEmployee(self, name, cost, type, barcode, manufacturing_date, manufacturer_name, expiry_date):
        query = "update employee set name='{}',cost='{}',type={},manufacturing_date={},manufacturer_name={},expiry_date={} where barcode = ".format(
            name, cost, type, manufacturing_date, manufacturer_name, expiry_date)
        print(query)
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")
