#+---------+-------------+------+-----+---------+-------+
#| Field   | Type        | Null | Key | Default | Extra |
#+---------+-------------+------+-----+---------+-------+
#| NAME    | varchar(20) | YES  |     | NULL    |       |
#| ADDRESS | varchar(30) | YES  |     | NULL    |       |
#| LICENSE | int         | NO   | PRI | NULL    |       |
#+---------+-------------+------+-----+---------+-------+

#CLASS
#supplier

#FUNCTIONS
#pleas fill this list

class supplier:
    # default constructor
    def __init__(self):
        try:
            self.con = dbConnect()
            self.cur = self.con.cursor()
        except:
            print("Database Error")
        self.address = ""
        self.name = ""
        self.licence = 0

    # parameteried constructor
    def __init__(self, con, address, name, licence):
        self.con = con
        self.cur = self.con.cursor()
        self.address = address
        self.name = name
        self.licence = licence

        # create table
        def createCustomer(self):
            query = 'create table if not exists customer(address varchar(40),name varchar(20),licence varchar(20), primary key licence)'
            # cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("\nSuccessfull")

        # insert
        def insertCustomer(self, name, ph_no, address, customer_id, gender, employee_id):
            query = "insert into customer(address ,name ,licence ) values('{}','{}','{}')"
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
            query = "delete from supplier where licence = {} ".format(licence)
            # cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("Delete");

        # update
        def updateCustomer(self, address, name,   licence):
            query = "update doctor set name='{}',age={},phone='{}',clinicAddress='{}',licence='{}' where licence = ".format(
                address,name,  licence)
            print(query)
            # cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("updated");
