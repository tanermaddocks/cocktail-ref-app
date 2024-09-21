from classes.stock import Beverage, Beer, Wine, Spirit

def addItem(bar):
    #ask for item type being added
    item_type = str.lower(input("What item do you wish to add (Spirit, Beer, or Wine)? "))#SETOUT
    #add space in array for new item
    # item_type = bar.add_item_space(item_entry)
    #add item info to item
    if item_type == "beer":
        #item name
        name = str.capitalize(input(f"What is the name of the {item_type}? "))
        #item subtype
        # subtype = input("What kind of beer is the item (Lager, Ale, Stout)? ")
        #item strength
        alc =  float(input(f"What is the alcohol percentage of {name}? "))
        #item cost
        cost = float(input(f"How much does {name} cost for a pint? "))
        #extra info

        #return complete
        return print(Beer(name, alc, cost))
    
    elif item_type == "wine":
        #item name
        name = str.capitalize(input(f"What is the name of the {item_type}? "))
        #item subtype
        # subtype = input("What kind of beer is the item (Lager, Ale, Stout)? ")
        #item strength
        alc =  float(input(f"What is the alcohol percentage of {name}? "))
        #item cost
        cost = float(input(f"How much does {name} cost for a glass? "))
        #extra info

        #return complete
        return Wine(name, alc, cost)
    
    elif item_type == "spirit":
        #item name
        name = str.capitalize(input(f"What is the name of the {item_type}? "))
        #item subtype
        # subtype = input("What kind of beer is the item (Lager, Ale, Stout)? ")
        #item strength
        alc =  float(input(f"What is the alcohol percentage of {name}? "))
        #item cost
        cost = float(input(f"How much does {name} cost for a nip? "))
        #extra info

        #return complete
        return Spirit(name, alc, cost)
    
    else:
        print ("Invalid beverage type, try again.")
    #return complete
    pass

