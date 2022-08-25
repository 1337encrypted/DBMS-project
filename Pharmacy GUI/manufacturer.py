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
        self.licence = ""

    # parameterized constructor
    def __init__(self, con, address, name, licence):
        self.con = con
        self.cur = self.con.cursor()
        self.address = address
        self.name = name
        self.licence = licence
