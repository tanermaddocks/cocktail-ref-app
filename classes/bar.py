#Bar class is where items are stored, otherwise gives the name in an dictionary.

class Bar:
    def __init__(self, name):
        self.name = name
        self.item_space = []
    def __str__(self):
        return self.name

    def add_item_space(self, item_type):
        self.item_space.append(item_type)

        