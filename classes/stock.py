class Beverage:
    #contructor
    def __init__ (self, code, name, alc, cost) -> None:
        self.code = code
        self.name = name
        self.alc = alc
        self.cost = cost
        self.type = None
        self.serve = None

    def __str__(self) -> str:
        return f"#{self.code} -> {self.name} is a {self.type}, {self.alc}%, ${self.cost}0 for a {self.serve} glass."

    # def add_stock (self, code, name, alc, cost, type):
    #     self.code = code
    #     self.name = name
    #     self.alc = alc
    #     self.cost = cost
    #     self.type = type

    def get_item_code(self):
        return self.code
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
    def __init__(self, code, name, alc, cost, serve):
        super().__init__(code, name, alc, cost)
        self.type = "beer"
        self.serve = serve

class Wine (Beverage):
    #constructor
    def __init__(self, code, name, alc, cost):
        super().__init__(code, name, alc, cost)
        self.type = "wine"
        self.serve = "glass"

class Spirit (Beverage):
    #constructor
    def __init__ (self, code, name, alc, cost):
        super().__init__(code, name, alc, cost)
        self.type = "spirit"
        self.serve = "nip"