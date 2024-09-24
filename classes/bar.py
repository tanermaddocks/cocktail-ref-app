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

    def get_serve(self) -> str:
        return self.serve
    
    def set_serve(self, serve):
        self.serve = serve

    def add_item(self, new_item):
        self.items.append(new_item)

    def delete_item(self, item_code):
        new_menu = []
        deleted = False
        for item in self.items:
            if item.get_item_code != item_code:
                new_menu.append(item)  
            else: deleted = True
        self.items = new_menu
        return deleted

    def get_items(self):
        return self.items