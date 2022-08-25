#+--------------------+-------------+------+-----+---------+-------+
#| Field              | Type        | Null | Key | Default | Extra |
#+--------------------+-------------+------+-----+---------+-------+
#| NAME               | varchar(30) | YES  |     | NULL    |       |
#| COST               | double      | YES  |     | NULL    |       |
#| TYPE               | varchar(20) | YES  |     | NULL    |       |
#| BARCODE            | int         | NO   | PRI | NULL    |       |
#| MANUFACTURING_DATE | date        | YES  |     | NULL    |       |
#| MANUFACTURER_NAME  | varchar(20) | YES  |     | NULL    |       |
#| EXPIRY_DATE        | date        | YES  |     | NULL    |       |
#+--------------------+-------------+------+-----+---------+-------+


#CLASS
drug

#FUNCTIONS
#please fill this list


from connection import dbConnect

class drug:
    # default constructor
    def __init__(self):
        try:
            self.con = dbConnect()
            self.cur = self.con.cursor()
        except
            print("Database Error")
        self.name = ""
        self.cost = 0.0
        self.manufacturerName = ""
        self.manufactureDate = ""
        self.expiryDate = ""
        self.type = ""
        self.barcode = 0

    # parameterized constructor
    def __init__(self, con, name, cost, manufacturerName, manufactureDate, expiryDate, type, barcode):
        self.con = con
        self.cur = self.con.cursor()
        self.name = name
        self.cost = cost
        self.manufacturerName = manufacturerName
        self.manufactureDate = manufactureDate
        self.expiryDate = expiryDate
        self.type = type
        self.barcode = barcode
