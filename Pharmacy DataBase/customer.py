class CUSTOMER:
    #default constructor
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.address = ""
        self.gender = ""
        self.id = ""
    
    #parameterized constructor
    def __init__(self, name, phone, address, gender, id):
        self.name = name
        self.phone = phone
        self.address = address
        self.gender = gender
        self.id = id
