class Beverage:
    #contructor
    def __init__ (self, name, alc, cost) -> None:
        self.name = name
        self.alc = alc
        self.cost = cost
        self.type = None
        self.serve = None

    def __str__(self) -> str:
        return f"{self.name}, {self.type}, ${self.cost} for {self.serve}."

    def add_stock (self, name, alc, cost, type):
        self.name = name
        self.alc = alc
        self.cost = cost
        self.type = type

    def get_item_name(self):
        return self.name
    def get_item_alc(self):
        return self.alc
    def get_item_cost(self):
        return self.cost
    def get_item_type(self):
        return self.type
    def get_item_serve(self):
        return self.serve


class Beer (Beverage):
    #constructor
    def __init__(self, name, alc, cost):
        super().__init__(name, alc, cost)
        self.type = "beer"

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