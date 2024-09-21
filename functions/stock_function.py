from classes.stock import Beverage, Beer, Wine, Spirit

def addItem(bar):
    #ask for item type being added
    item_entry = input("What item do you wish to add (Spirit, Beer, or Wine)? ")#SETOUT
    #add space in array for new item
    item_type = bar.add_item_space(item_entry)
    #add item info to item
    if item_entry == "beer":
        #item name
        name = input("What is the name of the item? ")
        #item subtype
        # subtype = input("What kind of beer is the item (Lager, Ale, Stout)? ")
        #item strength
        alc =  input(f"What is the alcohol percentage of {name}? ")
        #item cost
        cost = input(f"How much does {name} cost for a pint? ")
        #extra info
        new_beer = Beer(name, alc, cost)
        print (new_beer)
    elif item_entry == "wine":
        #item name
        name = input("What is the name of the item? ")
        #item subtype
        # subtype = input("What kind of wine is the item (Red, White, Bubbles)? ")
        #item strength
        alc =  input(f"What is the alcohol percentage of {name}? ")
        #item cost
        cost = input(f"How much does {name} cost for a glass? ")

        #extra info
    elif item_entry == "spirit":
        #item name
        name = input("What is the name of the item? ")
        #item subtype
        # subtype = input("What kind of spirit is the item (Light, Dark, Liqueur)? ")
        #item strength
        alc =  input(f"What is the alcohol percentage of {name}? ") 
        #item cost
        cost = input(f"How much does {name} cost for a nip? ")

        #extra info
    else:
        print ("Invalid beverage type, try again.")
    #return complete
    pass

