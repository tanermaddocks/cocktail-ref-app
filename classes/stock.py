from functions.basic import costForm, standardCalc, beerSize

class Beverage:
    # constructor
    def __init__ (self, code, name, alc, cost) -> None:
        self.code = code
        self.name = name
        self.alc = alc
        self.cost = cost
        self.type = None
        self.serve = None
        self.mixed = False

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

    def is_mixed(self):
        return self.mixed

class Beer(Beverage):
    def __init__(self, code, name, alc, cost, serve):
        super().__init__(code, name, alc, cost)
        self.type = "beer"
        self.serve = serve
    
    def __str__(self) -> str:
        return (f"\n{self.code} -> {self.name}"
                f"\nType: {self.type.capitalize()}"
                f"\nServe: {self.serve} ({beerSize(self.serve)}mL)"
                f"\nAlc/vol: {self.alc}% "
                f"({standardCalc(self.alc, round(beerSize(self.serve), 2))} "
                f"standards)\nCost: ${costForm(self.cost)})")


class Wine(Beverage):
    def __init__(self, code, name, alc, cost, serve):
        super().__init__(code, name, alc, cost)
        self.type = "wine"
        self.serve = serve

    def __str__(self) -> str:
        return (f"\n{self.code} -> {self.name}"
                f"\nType: {self.type.capitalize()}"
                f"\nServe: {self.serve}mL glass\nAlc/vol: {self.alc}% "
                f"({round(standardCalc(self.alc, self.serve), 2)} standards)"
                f"\nCost: ${costForm(self.cost)}")


class Spirit(Beverage):
    def __init__ (self, code, name, alc, cost, subtype):
        super().__init__(code, name, alc, cost)
        self.subtype = subtype
        self.type = "spirit"
        self.serve = 30

    def __str__(self) -> str:
        return (f"\n{self.code} -> {self.name}"
                f"\nType: {self.subtype.capitalize()} {self.type}"
                f"\nServe: {self.serve}mL nip\nAlc/vol: {self.alc}% "
                f"({round(standardCalc(self.alc, self.serve), 2)} standards)"
                f"\nCost: ${costForm(self.cost)}")
    
    def get_item_subtype(self):
        return self.subtype
    
class Mix(Beverage):
    def __init__(self, code, name, alc, cost, recipe):
        super().__init__(code, name, alc, cost)
        self.type = "mix"
        self.mixed = True
        self.recipe = recipe

    def __str__(self) -> str:
        return f"{self.name}"