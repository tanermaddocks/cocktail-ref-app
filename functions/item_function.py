import random

from classes.stock import Beer, Wine, Spirit
from functions.basic import capitalFullString, valueErrorCheck, confirm
from functions.common_print import wrongChoice, invalidEntry
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

    #insert into a class relevant to type
    match item_type:
        #for beer
        case "beer": 
            beer_serve = bar.get_beer_serve()
            #item cost
            cost = valueErrorCheck(f"How much does {name} cost for a {beer_serve} glass? ")
            new_item = Beer(code, name, alc, cost, beer_serve)
        #for wine
        case "wine": 
            wine_serve = bar.get_wine_serve()
            #item cost
            cost = valueErrorCheck(f"How much does {name} cost for a {wine_serve}mL glass? ")
            new_item = Wine(code, name, alc, cost) 
        #for spirit
        case "spirit": 
            new_item = Spirit(code, name, alc, cost)    
    
    #add item to bar dictionary
    print(f"\n{new_item}")
    print(f"\nAdd {name} to {bar}'s menu?")
    approve = confirm()
    if approve:
        bar.add_item(new_item)
        saveFile(bar)
    else:
        print("Add item cancelled.")

        

# Remove item
def removeItem(bar):
    identify_target = str.lower(input("Delete item by code or by name? "))
    # if identify_target != ("code" or "name"):
    #     return print("Invalid input, try again.")
    if identify_target == "code": pass
    elif identify_target == "name": pass
    else: return invalidEntry
    prompt = f"Enter {identify_target} of item to be removed: "

    #find item code and name
    if identify_target == "code": target = format(int(valueErrorCheck(prompt)), "06d")
    elif identify_target == "name": target = capitalFullString(input(prompt))
    all_items = bar.get_items()
    for item in all_items:
        if identify_target == "code":
            if item.get_item_code() == target:
                target_name = item.get_item_name()
                break
        elif identify_target == "name": 
            if item.get_item_name() == target:
                target = item.get_item_code()
                target_name = item.get_item_name()
                break
    #if none found
    else: return print(f"No item in {bar}'s menu with that {identify_target}.")

    #confirm delete
    print(f"Delete {target_name} from {bar}'s menu?")
    approve = confirm()
    if approve:
        bar.delete_item(target)
        saveFile(bar)
    else: print("Delete item cancelled.")



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
        printList = f"#{item.get_item_code()} -> {item.get_item_name()} - ${format(item.get_item_cost(), ".2f")}"
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
        
    
