#Bar class is where items are stored, otherwise gives the name in an dictionary.

class Bar:
    def __init__(self, name):
        self.name = name
        self.items = []
    def __str__(self):
        return self.name

    def add_item(self, new_item):
        self.items.append(new_item)

    def get_items(self):
        return self.items