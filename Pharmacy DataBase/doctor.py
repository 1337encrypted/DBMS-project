class DOCTOR:
    # default constructor
    def __init__(self):
        self.name = ""
        self.age = ""
        self.phone = ""
        self.clinicAddress = ""
        self.licence = ""

    #changes made
    # parameterized constructor
    def __init__(self, name, age, phone, clinicAddress, licence):
        self.name = name
        self.age = age
        self.phone = phone
        self.clinicAddress = clinicAddress
        self.licence = licence
