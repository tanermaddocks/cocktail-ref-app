#Bar class is where items are stored, otherwise gives the name in an dictionary.

class Bar:
    def __init__(self, name, serve):
        self.name = name
        self.serve = serve
        self.items = []
        
    def __str__(self) -> str:
        return self.name

    def get_name(self):
        return self.name

    def get_serve(self):
        return self.serve
    
    def set_serve(self, serve):
        self.serve = serve

    def add_item(self, new_item):
        self.items.append(new_item)

    def get_items(self):
        return self.items