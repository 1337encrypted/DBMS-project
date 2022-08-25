class EMPLOYEE:
    #default constructor
    def __init__(self):
        self.name = ""
        self.age = ""
        self.phone = ""
        self.shift = ""
        self.id = ""
    
    #parameterized constructor
    def __init__(self, name, age, phone, shift, id):
        self.name = name
        self.age = age
        self.phone = phone
        self.shift = shift
        self.id = id
    
