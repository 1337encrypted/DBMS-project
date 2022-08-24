class SUPPLIER:
    # default constructor
    def __init__(self):
        self.address = ""
        self.name = ""
        self.licence = ""

    # parameteried constructor
    def __init__(self, address, name, licence):
        self.address = address
        self.name = name
        self.licence = licence
