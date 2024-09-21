class Beverage:
    #contructor
    def __init__ (self, name, alc, cost):
        self.name = name
        self.alc = alc
        self.cost = cost
        self.type = None
        self.serve = None

    def __str__(self) -> str:
        return f"{self.name} is a {self.type} that has an alcohol percentage of {self.alc}% and costs ${self.cost} for a {self.serve}."

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
    def add_stock(self, name, alc, cost, type, serve):
        return super().add_stock(name, alc, cost, type, serve)


class Wine (Beverage):
    #constructor
    def __init__(self, name, alc, cost):
        super().__init__(name, alc, cost)
        self.type = "wine"
        self.serve = "glass"
    def add_stock(self, name, alc, cost, type, serve):
        return super().add_stock(name, alc, cost, type, serve)


class Spirit (Beverage):
    #constructor
    def __init__ (self, name, alc, cost):
        super().__init__(name, alc, cost)
        self.type = "spirit"
        self.serve = "nip"
    def add_stock(self, name, alc, cost, type, serve):
        return super().add_stock(name, alc, cost, type, serve)