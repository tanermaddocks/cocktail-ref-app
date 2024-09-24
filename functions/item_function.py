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
        code = format(random.randint(0, 9999), "06d")
        if code not in existing_code: x += 1

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
    confirm = ""
    while confirm == "":
        confirm = str.lower(input("Add this item to menu? (yes/no): "))
        if confirm == ("yes" or "y"):
            bar.add_item(new_item)
            saveFile(bar)
        elif confirm == ("no" or "n"): 
            print("Add item cancelled.")
        else: 
            print ("Invalid input, try again.")
            confirm = ""
        

# Remove item
def removeItem(bar):
    identify_target = str.lower(input("Delete item by code or by name? "))
    if identify_target != ("code" or "name"): 
        return print("Invalid input, try again.")
    target = input(f"Enter the {identify_target} of the item you would like to remove: ")

    if identify_target == "code":
        target = valueErrorCheck(format(int(target)), "06d")
    elif identify_target == "name": 
        target = capitalFullString(target)
        all_items = bar.get_items()
        for item in all_items:
            if item.get_item_name != target:
                continue
            else:
                target_name = item.get_item_name
                target = item.get_item_code()
    confirm = str.lower(input(f"Delete {target_name} from menu? (yes/no): "))
    if confirm == ("yes" or "y"):
        bar.remove_item(target)
        saveFile(bar)
    elif confirm == ("no" or "n"): 
        print("Delete item cancelled.")
                

    
    complete = bar.delete_item(target)
    if complete:
        saveFile(bar)



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
        printList = f"#{item.get_item_code()} -> {item.get_item_name()} - ${item.get_item_cost()}"
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
        
    
