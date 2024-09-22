class Beverage:
    #contructor
    def __init__ (self, name, alc, cost) -> None:
        self.name = name
        self.alc = alc
        self.cost = cost
        self.type = None
        self.serve = None

    def __str__(self) -> str:
        return f"{self.name}, {self.type}, {self.alc}%, ${self.cost} for {self.serve}."

    def add_stock (self, name, alc, cost, type, serve):
        self.name = name
        self.alc = alc
        self.cost = cost
        self.type = type
        self.serve = serve

class Beer (Beverage):
    #constructor
    def __init__(self, name, alc, cost):
        super().__init__(name, alc, cost)
        self.type = "beer"
        self.serve = "pint"

class Wine (Beverage):
    #constructor
    def __init__(self, name, alc, cost):
        super().__init__(name, alc, cost)
        self.type = "wine"
        self.serve = "glass"

class Spirit (Beverage):
    #constructor
    def __init__ (self, name, alc, cost):
        super().__init__(name, alc, cost)
        self.type = "spirit"
        self.serve = "nip"