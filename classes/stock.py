class Beverage:
    #contructor
    def __init__ (self, name, alc, cost):
        self.name = name
        self.alc = alc
        self.cost = cost
        self.type = None

    def __str__(self) -> str:
        return f"{self.name} is a {self.type} that has an alcohol percentage of {self.alc}% and costs ${self.cost}."

    def add_stock (self, name, alc, cost, type):
        self.name = str.capitalize(name)
        self.alc = int(alc)
        self.cost = int(cost)
        self.type = str.lower(type)


class Beer (Beverage):
    #constructor
    def __init__(self, name, alc, cost):
        super().__init__(name, alc, cost)
        self.type = "beer"
    def add_stock(self, name, alc, cost, type):
        return super().add_stock(name, alc, cost, type)


class Wine (Beverage):
    #constructor
    def __init__(self, name, alc, cost):
        super().__init__(name, alc, cost)
        self.type = "wine"
    def add_stock(self, name, alc, cost, type):
        return super().add_stock(name, alc, cost, type)


class Spirit (Beverage):
    #constructor
    def __init__ (self, name, alc, cost):
        super().__init__(name, alc, cost)
        self.type = "spirit"
    def add_stock(self, name, alc, cost, type):
        return super().add_stock(name, alc, cost, type)