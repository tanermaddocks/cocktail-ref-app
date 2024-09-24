import json, os
from classes.bar import Bar
from classes.stock import Beer, Wine, Spirit

def saveFile(bar):
    barname = bar.get_name()

    #info save
    try: os.mkdir(f"data/{barname}")
    except FileExistsError: pass
    bar_info = {
        "barname": bar.get_name(),
        "barserve": bar.get_serve()
        }
    with open(f"data/{barname}/{barname}_info.json", "w") as json_file:
        json.dump(bar_info, json_file, indent=4)

    #menu save
    item_dict = []
    for item in bar.get_items():
        item_json = {
            "code": item.get_item_code(),
            "name": item.get_item_name(),
            "alc": item.get_item_alc(),
            "cost": item.get_item_cost(),
            "type": item.get_item_type(),
            "serve": item.get_item_serve()
        }
        item_dict.append(item_json)
    with open(f"data/{barname}/{barname}_menu.json", "w") as json_file:
        json.dump(item_dict, json_file, indent=4)
    print ("Bar menu updated.")

def loadInfo(barname):
    try:
        #info load
        with open(f"data/{barname}/{barname}_info.json", "r") as json_file:
            bar_info = json.load(json_file)
            barname = bar_info["barname"]
            barserve = bar_info["barserve"]
        return Bar(barname, barserve)
    except FileNotFoundError:
        confirm = input("\nBar not on file, do you want to add a new bar? (Enter yes to confirm): ")
        if confirm == "yes":
            print ("\nWhat does your bar use as a standard beer serve?")
            standard_beer_serve = input("Choose one of pot, schooner, pint or stein: ")
            return Bar(barname, standard_beer_serve)
        else:
            print ("\nThank for for using the cocktail reference application!")
            exit()

def loadMenu(bar):
    barname = bar.get_name()
    try:
        #menu load
        with open(f"data/{barname}/{barname}_menu.json", "r") as json_file:
            item_dict = json.load(json_file)
            for item in item_dict:
                code = item["code"]
                name = item["name"] 
                alc = item["alc"]
                cost = item["cost"]
                type = item["type"]
                serve = item["serve"]
                match type:
                    case "beer": item = Beer(code, name, alc, cost, serve)
                    case "wine": item = Wine(code, name,alc, cost)
                    case "spirit": item = Spirit(code, name, alc, cost) 
                    case "mix": pass #FOR COCKTAILS
                bar.add_item(item)
    except FileNotFoundError: print ("Failed to load menu!")
    