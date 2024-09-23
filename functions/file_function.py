import json
from classes.bar import Bar
from classes.stock import Beer, Wine, Spirit
from functions.basic import underscoreBar

def saveFile(bar):
    #info save
    bar_info = {
        "barname": str(bar),
        "barserve": bar.get_serve()
        }
    with open(f"data/{underscoreBar(bar)}/{underscoreBar}_info.json", "w") as json_file:
        json.dump(bar_info, json_file, indent=4)
    #menu save
    item_dict = []
    for item in bar.get_items():
        item_json = {
            "name": item.get_item_name(),
            "alc": item.get_item_alc(),
            "cost": item.get_item_cost(),
            "type": item.get_item_type(),
            "serve": item.get_item_serve()
        }
        item_dict.append(item_json)
    with open(f"data/{underscoreBar(bar)}/{underscoreBar(bar)}_menu.json", "w") as json_file:
        json.dump(item_dict, json_file, indent=4)
    print ("Bar menu updated.")

def loadFile(bar):
    try:
        #info load
        with open(f"data/{underscoreBar(bar)}/{underscoreBar}_info.json", "r") as json_file:
            bar_info = json.load(json_file)
            barname = ["barname"]
            barserve = ["barserve"]
            bar.add_item
        #menu load
        with open(f"data/{underscoreBar}/{underscoreBar(bar)}.json_menu", "r") as json_file:
            item_dict = json.load(json_file)
            for item in item_dict:
                name = item["name"]
                alc = item["alc"]
                cost = item["cost"]
                type = item["type"]
                match type:
                    case "beer": item = Beer(name, alc, cost)
                    case "wine": item = Wine(name,alc, cost)
                    case "spirit": item = Spirit(name, alc, cost) 
                    case "mix": pass #FOR COCKTAILS
                bar.add_item(item)
    except FileNotFoundError:
        confirm = input("Bar not on file, do you want to add a new bar? (yes/no): ")
        if confirm == "yes":
            print ("What does your bar use as a standard beer serve?")
            standard_beer_serve = input("Choose one of pot, schooner, pint or stein: ")
            return bar.set_serve(standard_beer_serve)
        else:
            print ("Thank for for using the cocktail reference application!")
            return exit()
    