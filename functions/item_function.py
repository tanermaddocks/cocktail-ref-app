import random

from classes.stock import Beer, Wine, Spirit
from functions.basic import capitalFullString, wrongChoice, valueErrorCheck
from functions.file_function import saveFile


# Add item
def addStock(bar):
    #generate item code for new item
    all_items = bar.get_items()
    existing_code = []
    for item in all_items:
        existing_code.append(item.get_item_code())
    x = 0
    while x == 0:
        code = format(random.randint(0, 999999), "06d")
        if code in existing_code: continue
        else: break

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
    alc = valueErrorCheck(f"What is the alcohol percentage of {name}? ")
    print (alc)

    #item cost
    cost = valueErrorCheck(f"How much does {name} cost for a STANDARD SERVE? ")

    #insert into a class relevant to type
    match item_type:
        #for beer
        case "beer": new_item = Beer(code, name, alc, cost)
        #for wine
        case "wine": new_item = Wine(code, name, alc, cost) 
        #for spirit
        case "spirit": new_item = Spirit(code, name, alc, cost)    
    
    #add item to bar dictionary
    print(new_item)
    confirm = str.lower(input("Is all information correct? (yes/no): "))
    if confirm == "yes":
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
        
    
