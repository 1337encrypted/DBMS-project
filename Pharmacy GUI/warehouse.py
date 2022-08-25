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
        self.id = ""
        self.name = ""
        self.location = ""

    # parameterized constructor
    def __init__(self, con, id, name, location):
        self.con = con
        self.cur = self.con.cursor()
        self.id = id
        self.name = name
        self.location = location
