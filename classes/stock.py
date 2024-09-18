class Beverage:
    #contructor
    def __init__ (self, alcohol, cost, type):
        self.alc = alcohol
        self.cost = cost
        self.type = type #vodka, tequila, lager, ale, red, white

class Spirit (Beverage):
    #constructor
    def __init__ (self, alcohol, cost, origin, type, subtype):
        super().__init__(alcohol, cost, type)
        self.origin = origin
        self.subtype = subtype #scotch, bourbon, etc.

class Beer (Beverage):
    #constructor
    def __init__(self, alcohol, cost, type, grain):
        super().__init__(alcohol, cost, type)
        self.grain = grain

class Wine (Beverage):
    #constructor
    def __init__(self, alcohol, cost, type, fruit):
        super().__init__(alcohol, cost, type)
        self.fruit = fruit