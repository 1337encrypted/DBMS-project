#+-------------+-------------+------+-----+---------+-------+
#| Field       | Type        | Null | Key | Default | Extra |
#+-------------+-------------+------+-----+---------+-------+
#| NAME        | varchar(20) | YES  |     | NULL    |       |
#| PH_NO       | varchar(10) | YES  |     | NULL    |       |
#| ADDRESS     | varchar(30) | YES  |     | NULL    |       |
#| CUSTOMER_ID | int         | NO   | PRI | NULL    |       |
#| GENDER      | varchar(1)  | YES  |     | NULL    |       |
#| EMPLOYEE_ID | int         | YES  | MUL | NULL    |       |
#+-------------+-------------+------+-----+---------+-------+

#CLASS
#customer

#FUNCTIONS
#__init__(self):
#__init__(self, name, phone, address, gender, id):
#createCustomer(self):
#insertCustomer(self,name,ph_no,address,customer_id,gender,employee_id):
#fetchAll(self):
#deleteCustomer(self,customer_id):
#updateCustomer(self,customer_id,name,ph_no,address,gender,employee_id):
    
    
from connection import dbConnect

class customer:
    #default constructor
    def __init__(self):
        try:
            self.con = dbConnect()
            cur = self.con.cursor()
        except:
            print("Database Error")
            
        self.name = ""
        self.phone = ""
        self.address = ""
        self.gender = ""
        self.id = ""
    
    #parameterized constructor
    def __init__(self, con, name, phone, address, gender, id):
        self.con = con
        self.cur = self.con.cursor()
        self.name = name
        self.phone = phone
        self.address = address
        self.gender = gender
        self.id = id
    
    #create table
    def createCustomer(self):
        query = 'create table if not exists customer(name varchar(20),ph_no varchar(10),address varchar(30),customer_id int primary key,gender varchar(1),employee_id int)'
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("\nSuccessfull")
        
    #insert
    def insertCustomer(self,name,ph_no,address,customer_id,gender,employee_id):
        query = "insert into customer(name,ph_no,address,customer_id,gender,employee_id) values('{}','{}','{}',{},'{}',{})"
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commmit()
     
    #fetch
    def fetchAll(self):
        query="select * from customer"
        #cur = self.con.cursor()
        cur.execute(query);
        for row in cur:
            print(row)
      
    #delete
    def deleteCustomer(self,customer_id):
        query="delete from customer where customer_id = {} ".format(customer_id)
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Delete");
        
    #update
    def updateCustomer(self,customer_id,name,ph_no,address,gender,employee_id):
        query="update customer set ph_no='{}',address='{}',gender={},employee_id={} where customer_id = ".format(ph_no,address,gender,employee_id)
        print(query)
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated");
