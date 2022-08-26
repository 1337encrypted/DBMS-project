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
