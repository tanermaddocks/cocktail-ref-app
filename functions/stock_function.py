from classes.stock import Beer, Wine, Spirit
from functions.basic import capitalFullString, standardCalc, wrongChoice


# Add item
def addStock(bar):
    #ask for item type being added
    item_type = str.lower(input("\nWhat item do you wish to add; beer, wine or spirit? "))
    match item_type:
        case "beer": pass
        case "wine": pass
        case "spirit": pass
        case _: return wrongChoice(False)
    #item name
    name = capitalFullString(input(f"What is the name of the {item_type}? "))
    #item strength in percent
    alcper =  float(input(f"What is the alcohol percentage of {name}? ")) #VALUEERROR
    match item_type:
        #for beer
        case "beer":
            #standard calc
            alc = standardCalc(alcper, 570) #Maybe make serve size an input?
            #item cost
            cost = float(input(f"How much does {name} cost for a pint (570mL)? "))
            #extra info
            pass
            new_item = Beer(name, alc, cost)
        #for wine
        case "wine":
            alc = standardCalc(alcper, 150)
            cost = float(input(f"How much does {name} cost for a glass (150mL)? "))
            #extra info
            pass
            new_item = Wine(name, alc, cost)
        #for spirit
        case "spirit":
            alc = standardCalc(alcper, 30)
            cost = float(input(f"How much does {name} cost for a nip (30mL)? "))
            #extra info
            pass
            new_item = Spirit(name, alc, cost)
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
    print ("Which items would you like to see?")
    type = str.lower(input("Choose from beer, wine, spirit, mix or all: "))
    print()
    for item in all_items: 
        match type:
            case "beer": 
                if item.get_item_type() == "beer": print(item) 
            case "wine":
                if item.get_item_type() == "wine": print(item) 
            case "spirit":
                if item.get_item_type() == "spirit": print (item)
            case "mix": 
                pass
            case "all": 
                print(item)
            case _: 
                wrongChoice(True)
        
    
