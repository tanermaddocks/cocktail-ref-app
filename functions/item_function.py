from classes.stock import Beer, Wine, Spirit
from functions.basic import capitalFullString, wrongChoice
from functions.file_function import saveFile


# Add item
def addStock(bar):
    #ask for item type being added
    item_type = str.lower(input("What item do you wish to add; beer, wine or spirit? "))
    match item_type:
        case "beer": pass
        case "wine": pass
        case "spirit": pass
        case _: return wrongChoice(False)
    #item name
    name = capitalFullString(input(f"What is the name of the {item_type}? "))
    #item strength in percent
    alc =  float(input(f"What is the alcohol percentage of {name}? ")) #VALUEERROR
    match item_type:
        #for beer
        case "beer":
            #item cost
            cost = float(input(f"How much does {name} cost for a pint (570mL)? "))
            #extra info
            pass
            new_item = Beer(name, alc, cost)
        #for wine
        case "wine":
            cost = float(input(f"How much does {name} cost for a glass (150mL)? "))
            #extra info
            pass
            new_item = Wine(name, alc, cost)
        #for spirit
        case "spirit":
            cost = float(input(f"How much does {name} cost for a nip (30mL)? "))
            #extra info
            pass
            new_item = Spirit(name, alc, cost)
    #add item to bar dictionary
    print(new_item)
    confirm = str.lower(input("Is all information correct? (yes/no): "))
    if confirm == "y" or "yes":
        bar.add_item(new_item)
        saveFile(bar)
    else:
        print("Add item cancelled, try again.")

# Remove item
def removeItem(bar):
    target = input("Enter the name of the item you would like to remove: ")
    

# Search item
pass

# List items
def listItem(bar):
    all_items = bar.get_items()
    if not all_items: return print ("No items in bar.")
    print ("Which items would you like to see?")
    type = str.lower(input("Choose from beer, wine, spirit, mix or all: "))
    print()
    for item in all_items: 
        printList = f"-> {item.get_item_name()} - ${item.get_item_cost()}"
        match type:
            case "beer": 
                #see beer
                if item.get_item_type() == "beer": print(printList)
            case "wine":
                #see wine
                if item.get_item_type() == "wine": print(printList)
            case "spirit":
                #see spirit
                if item.get_item_type() == "spirit": print(printList)
            case "mix": 
                #see mix
                pass
            case "all":
                #see all
                print(printList)
            case _:
                #wrong input
                wrongChoice(True)
        
    
