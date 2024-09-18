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
        self.subtype = subtype #scotch, fruit, dry

class Beer (Beverage):
    #constructor
    def __init__(self, alcohol, cost, type):
        super().__init__(alcohol, cost, type)

class Wine (Beverage):
    #constructor
    def __init__(self, alcohol, cost, type):
        super().__init__(alcohol, cost, type)