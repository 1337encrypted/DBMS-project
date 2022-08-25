# +-------------+-------------+------+-----+---------+-------+
# | Field       | Type        | Null | Key | Default | Extra |
# +-------------+-------------+------+-----+---------+-------+
# | NAME        | varchar(20) | YES  |     | NULL    |       |
# | AGE         | int         | YES  |     | NULL    |       |
# | PH_NO       | varchar(10) | YES  |     | NULL    |       |
# | EMPLOYEE_ID | int         | NO   | PRI | NULL    |       |
# | SHIFT_TIME  | varchar(20) | YES  |     | NULL    |       |
# +-------------+-------------+------+-----+---------+-------+

# CLASS
# employee

# FUNCTIONS
# def __init__(self):
# def __init__(self, con, name, age, phone, shift, id):
# def createEmployee(self):
# def insertEmployee(self, name, age, ph_no, employee_id, shift_time):
# def deleteEmployee(self, employee_id):
# def fetchAll(self):
# def updateEmployee(self, name, age, ph_no, employee_id, shift_time):
# please fill this list
from connection import dbConnect


class employee:
    # default constructor
    def __init__(self):
        try:
            self.con = dbConnect()
            self.cur = self.con.cursor()
        except:
            print("Database Error")
        self.name = ""
        self.age = ""
        self.phone = ""
        self.shift = ""
        self.id = ""

    # parameterized constructor
    def __init__(self, con, name, age, phone, shift, id):
        self.con = con
        self.cur = self.con.cursor()
        self.name = name
        self.age = age
        self.phone = phone
        self.shift = shift
        self.id = id

    # create table
    def createEmployee(self):
        query = 'create table if not exists employee(name varchar(20),age int,ph_no int,employee_id int primary key,shift_time varchar(20))'
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("\nSuccessfull")

    # insert
    def insertEmployee(self, name, age, ph_no, employee_id, shift_time):
        query = "insert into customer(name,age,ph_no,employee_id,shift_time) values('{}','{}','{}',{},'{}',{})"
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commmit()

     # fetch
    def fetchAll(self):
        query = "select * from employee"
        #cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)

    # delete
    def deleteEmployee(self, employee_id):
        query = "delete from employee where employee_id = {} ".format(
            employee_id)
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Delete")

    # update
    def updateEmployee(self, name, age, ph_no, employee_id, shift_time):
        query = "update employee set name='{}',age='{}',ph_no={},shift_time={} where employee_id = ".format(
            name, age, ph_no, shift_time)
        print(query)
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")
