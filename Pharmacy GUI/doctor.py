#+----------------+-------------+------+-----+---------+-------+
#| Field          | Type        | Null | Key | Default | Extra |
#+----------------+-------------+------+-----+---------+-------+
#| NAME           | varchar(20) | YES  |     | NULL    |       |
#| AGE            | int         | YES  |     | NULL    |       |
#| PH_NO          | varchar(10) | YES  |     | NULL    |       |
#| LICENSE        | int         | NO   | PRI | NULL    |       |
#| CLINIC_ADDRESS | varchar(30) | YES  |     | NULL    |       |
#+----------------+-------------+------+-----+---------+-------+

#CLASS
#doctor

#FUNCTIONS
#write functions list here


from connection import dbConnect


class doctor:
    # default constructor
    def __init__(self):
        try:
            self.con = dbConnect()
            self.cur = self.con.cursor()
        except:
            print("Database Error")
            
        self.name = ""
        self.age = 0
        self.phone = ""
        self.clinicAddress = ""
        self.licence = 0

    # parameterized constructor
    def __init__(self, con, name, age, phone, clinicAddress, licence):
        self.con = con
        self.cur = self.con.cursor()
        self.name = name
        self.age = age
        self.phone = phone
        self.clinicAddress = clinicAddress
        self.licence = licence

        # create table
        def createCustomer(self):
            query = 'create table if not exists customer(name varchar(20),age int,phone varchar(30),clinicAddress varchar(40),licence varchar(20), primary key licence)'
            # cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("\nSuccessfull")

        # insert
        def insertCustomer(self, name, ph_no, address, customer_id, gender, employee_id):
            query = "insert into customer(name ,age ,phone ,clinicAddress ,licence ) values('{}',{},'{}','{}','{}')"
            # cur = self.con.cursor()
            cur.execute(query)
            self.con.commmit()

        # fetch
        def fetchAll(self):
            query = "select * from customer"
            # cur = self.con.cursor()
            cur.execute(query);
            for row in cur:
                print(row)

        # delete
        def deleteCustomer(self, customer_id):
            query = "delete from doctor where licence = {} ".format(licence)
            # cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("Delete");

        # update
        def updateCustomer(self,  name, age,phone,clinicalAddress,licence):
            query = "update doctor set name='{}',age={},phone='{}',clinicAddress='{}',licence='{}' where licence = ".format(name ,age ,phone ,clinicAddress ,licence)
            print(query)
            # cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("updated");
