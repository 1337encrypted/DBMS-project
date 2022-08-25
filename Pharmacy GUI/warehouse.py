#+----------+-------------+------+-----+---------+-------+
#| Field    | Type        | Null | Key | Default | Extra |
#+----------+-------------+------+-----+---------+-------+
#| ID       | int         | NO   | PRI | NULL    |       |
#| NAME     | varchar(20) | YES  |     | NULL    |       |
#| LOCATION | varchar(30) | YES  |     | NULL    |       |
#+----------+-------------+------+-----+---------+-------+

#CLASS
#warehouse

#FUNCTIONS
#please fill this list


class warehouse:
    # default constructor
    def __init__(self):
        try:
            self.con = dbConnect()
            self.cur = self.con.cursor()
        except
        self.id = 0
        self.name = ""
        self.location = ""

    # parameterized constructor
    def __init__(self, con, id, name, location):
        self.con = con
        self.cur = self.con.cursor()
        self.id = id
        self.name = name
        self.location = location

    #create table
    def createWarehouse(self):
        query = 'create table if not exists warehouse(id int primary key,name varchar(20),location varchar(30));'
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("\nSuccessfull")

    #insert
    def insertWarehouse(self, id, name, location):
        query = "insert into warehouse(id,name,location) values({},'{}','{}');"
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commmit()

    #fetch
    def fetchAll(self):
        query="select * from warehouse;"
        #cur = self.con.cursor()
        cur.execute(query);
        for row in cur:
            print(row)

    #delete
    def deleteWarehouse(self,id):
        query="delete from warehouse where id = {};".format(id)
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Delete");

    #update
    def updateWarehouse(self,id,name,location):
        query="update warehouse set location='{}', where id = ;".format(location)
        print(query)
        #cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated");
