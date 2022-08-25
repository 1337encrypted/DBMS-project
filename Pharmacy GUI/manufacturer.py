class MANUFACTURER:
    # default constructor
    def __init__(self):
        self.address = ""
        self.name = ""
        self.licence = ""

    # parameterized constructor
    def __init__(self, address, name, licence):
        self.address = address
        self.name = name
        self.licence = licence
