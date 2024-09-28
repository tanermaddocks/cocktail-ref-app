from functions.basic import serveSize, costForm

class Beverage:
    #contructor
    def __init__ (self, code, name, alc, cost) -> None:
        self.code = code
        self.name = name
        self.alc = alc
        self.cost = cost
        self.type = None
        self.serve = None

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


class Beer(Beverage):
    #constructor
    def __init__(self, code, name, alc, cost, serve):
        super().__init__(code, name, alc, cost)
        self.type = "beer"
        self.serve = serve
    
    def __str__(self) -> str:
        return f"{self.code} -> {self.name}\n\
                Type: {self.type}\nAlc/vol: {self.alc}%\n\
                Cost: ${costForm(self.cost)} for a {self.serve} glass"
    
    def get_beer_vol(self):
        return serveSize(self.serve)


class Wine(Beverage):
    #constructor
    def __init__(self, code, name, alc, cost, serve):
        super().__init__(code, name, alc, cost)
        self.type = "wine"
        self.serve = serve

    def __str__(self) -> str:
        return f"{self.code} -> {self.name}\n\
                Type: {self.type}\nAlc/vol: {self.alc}%\n\
                Cost: ${costForm(self.cost)} for a {self.serve}mL glass"


class Spirit(Beverage):
    #constructor
    def __init__ (self, code, name, alc, cost, subtype):
        super().__init__(code, name, alc, cost)
        self.subtype = subtype
        self.type = "spirit"
        self.serve = 30

    def __str__(self) -> str:
        return f"{self.code} -> {self.name}\n\
                Type: {self.subtype} {self.type}\nAlc/vol: {self.alc}%\n\
                Cost: ${costForm(self.cost)} for a {self.serve}mL nip"
    
    def get_item_subtype(self):
        return self.subtype