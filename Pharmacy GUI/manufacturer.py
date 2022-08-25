#+---------+-------------+------+-----+---------+-------+
#| Field   | Type        | Null | Key | Default | Extra |
#+---------+-------------+------+-----+---------+-------+
#| NAME    | varchar(20) | YES  |     | NULL    |       |
#| ADDRESS | varchar(30) | YES  |     | NULL    |       |
#| LICENSE | int         | NO   | PRI | NULL    |       |
#+---------+-------------+------+-----+---------+-------+

#CLASS
manufacturer

#FUNCTIONS
#please fill this list

class manufacturer:
    # default constructor
    def __init__(self):
        try:
            self.con = dbConnect()
            self.cur = self.con.cursor()
        except:
            print("Database Error")
        self.address = ""
        self.name = ""
        self.license = 0

    # parameterized constructor
    def __init__(self, con, address, name, license):
        self.con = con
        self.cur = self.con.cursor()
        self.address = address
        self.name = name
        self.license = license

    #create table
    def createManufacturer(self):
        query = 'create table if not exists manufacturer(name varchar(20),address varchar(30),license int primary key);'
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("\nSuccessfull")
    
    #insert
    def insertManufacturer(self,name,address,license):
        query = "insert into manufacturer(name,address,license) values('{}','{}',{};)"
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commmit()
 
    #fetch
    def fetchAll(self):
        query="select * from manufacturer;"
        #cur = self.con.cursor()
        cur.execute(query);
        for row in cur:
            print(row)
  
    #delete
    def deleteManufacturer(self,license):
        query="delete from manufacturer where license = {} ;".format(license)
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Delete");
        
    #update
    def updateManufacturer(self,license,name,address):
        query="update manufacturer set address='{}' where license = ;".format(address)
        print(query)
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated");
