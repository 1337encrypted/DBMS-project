class WAREHOUSE:
    # default constructor
    def __init__(self):
        self.id = ""
        self.name = ""
        self.location = ""

    # parameterized constructor
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location
