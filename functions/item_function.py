import random
from classes.stock import Beer, Wine, Spirit
from functions.basic import capitalFullString, valueErrorCheck,\
                            confirm, wrongChoice, costForm, codeMaker
from functions.file_function import saveFile


# Add item
def addStock(bar):
    #generate item code for new item
    code = codeMaker(bar)

    #ask for item type being added
    item_type = str.lower(input(
        "What item do you wish to add; beer, wine or spirit? "))
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
            cost = valueErrorCheck(f"How much does {name} cost "
                                   f"for a {beer_serve}? ")
            new_item = Beer(code, name, alc, cost, beer_serve)
        #for wine
        case "wine": 
            wine_serve = bar.get_wine_serve()
            #item cost
            cost = valueErrorCheck(f"How much does {name} cost for "
                                   f"a {wine_serve}mL glass? ")
            new_item = Wine(code, name, alc, cost, wine_serve) 
        #for spirit
        case "spirit": 
            subtype = str.lower(input(f"What kind of spirit is {name}?"
                                      "\n - Vokda\n - Tequila\n - Rum\n - Gin"
                                      "\n - Whiskey\n - Brandy\n - Liqueur"
                                      "\nEnter one of the above options: "))
            cost = valueErrorCheck(f"How much does {name} "
                                   f"cost for a 30ml nip? ")
            new_item = Spirit(code, name, alc, cost, subtype)    
    
    #add item to bar dictionary
    print(f"\n{new_item}")
    print(f"\nAdd {name} to {bar}'s menu?")
    approve = confirm()
    if approve:
        bar.add_item(new_item)
        saveFile(bar)
    else:
        print("Add item cancelled.")


def addMix(bar):
    pass


# Search for an item
def searchItem(bar):
    (target, target_name) = bar.search_item(bar)
    if target_name == False: return print(target)
    choice = ""
    while choice != "e":
        choice = str.lower(input(f"\nEnter E to return to menu or "
                                 f"enter D to delete {target_name} "
                                 f"from {bar}'s menu: "))
        if choice == "d":
            #confirm delete
            print(f"Delete {target} -> {target_name} from {bar}'s menu?")
            approve = confirm()
            if approve:
                bar.delete_item(target)
                saveFile(bar)
            else: 
                print("Delete item cancelled.")
            break


# List items
def listItem(bar):
    all_items = bar.get_items()
    if not all_items: 
        return print("No items in bar.")
    print("Which items would you like to see?")
    type = str.lower(input("Choose from beer, wine, spirit, mix or all: "))
    print()
    for item in all_items: 
        printList = (f" #{item.get_item_code()} -> {item.get_item_name()}"
                     f" - ${costForm(item.get_item_cost())}")
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
        
    
