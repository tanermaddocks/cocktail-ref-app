from classes.stock import Beer, Wine, Spirit
from functions.basic import capitalFullString

# Add item
def addStock(bar):
    #ask for item type being added
    item_type = str.lower(input("\nWhat item do you wish to add (Spirit, Beer, or Wine)? "))
    if item_type == "beer" or "wine" or "spirit":
        #item name
        name = capitalFullString(input(f"What is the name of the {item_type}? "))
        #item strength
        alc =  float(input(f"What is the alcohol percentage of {name}? "))
        match item_type:
            #for beer
            case "beer":
                #item cost
                cost = float(input(f"How much does {name} cost for a pint? "))
                #extra info
                pass
                #return complete
                new_item = Beer(name, alc, cost)
            #for wine
            case "wine":
                #item cost
                cost = float(input(f"How much does {name} cost for a glass? "))
                #extra info
                pass
                #return complete
                new_item = Wine(name, alc, cost)
            #for spirit
            case "spirit":
                #item cost
                cost = float(input(f"How much does {name} cost for a nip? "))
                #extra info
                pass
                #return complete
                new_item = Spirit(name, alc, cost)
    else:
        return print("Invalid item type, try again.")
    #add item to bar dictionary
    return bar.add_item(new_item)

# Remove item
pass

# Search item
pass

# List items
def listItem(bar):
    all_items = bar.get_items()
    if not all_items: print ("No items in bar.") 
    for item in all_items: print (item)
