#Bar class is where items are stored, otherwise gives the name in an dictionary.

class Bar:
    def __init__(self, name):
        self.name = name
        self.stock_space = []

class Beverage:
    #contructor
    def __init__ (self, alcohol, cost, subtype):
        self.alc = alcohol
        self.cost = cost
        self.subtype = subtype #vodka, tequila, lager, ale, red, white

