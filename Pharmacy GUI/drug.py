class DRUG:
    # default constructor
    def __init__(self):
        self.name = ""
        self.cost = ""
        self.manufacturerName = ""
        self.manufactureDate = ""
        self.expiryDate = ""
        self.type = ""
        self.barcode = ""

    # parameterized constructor
    def __init__(self, name, cost, manufacturerName, manufactureDate, expiryDate, type, barcode):
        self.name = name
        self.cost = cost
        self.manufacturerName = manufacturerName
        self.manufactureDate = manufactureDate
        self.expiryDate = expiryDate
        self.type = type
        self.barcode = barcode
