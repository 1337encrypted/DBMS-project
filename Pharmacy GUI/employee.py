#+-------------+-------------+------+-----+---------+-------+
#| Field       | Type        | Null | Key | Default | Extra |
#+-------------+-------------+------+-----+---------+-------+
#| NAME        | varchar(20) | YES  |     | NULL    |       |
#| AGE         | int         | YES  |     | NULL    |       |
#| PH_NO       | varchar(10) | YES  |     | NULL    |       |
#| EMPLOYEE_ID | int         | NO   | PRI | NULL    |       |
#| SHIFT_TIME  | varchar(20) | YES  |     | NULL    |       |
#+-------------+-------------+------+-----+---------+-------+

#CLASS
#employee

#FUNCTIONS
#please fill this list

class employee:
    #default constructor
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
    
    #parameterized constructor
    def __init__(self, con, name, age, phone, shift, id):
        self.con = con
        self.cur = self.con.cursor()
        self.name = name
        self.age = age
        self.phone = phone
        self.shift = shift
        self.id = id
    
