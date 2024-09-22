import json
from classes.stock import Beverage, Beer, Wine, Spirit
from functions.basic import underscoreBar

def saveExit(bar):
    item_dict = []
    for item in bar.get_items():
        item_json = {
            "name": item.get_item_name(),
            "type": item.get_item_type(),            
            "alc": item.get_item_alc(),
            "cost": item.get_item_cost(),
            "serve": item.get_item_serve()
        }
        item_dict.append(item_json)
    with open(f"data/{underscoreBar(bar)}.json", "w") as json_file:
        json.dump(item_dict, json_file, indent=4)

def loadFile(bar):
    try:
        with open(f"data/{underscoreBar(bar)}.json", "r") as json_file:
            item_dict = json.load(json_file)
        for item in item_dict:
            if item.get_item_type == "beer":
                name = Beer(item["name"])
                type = Beer(item["type"])
                alc =  Beer(item["alc"])
                cost = Beer(item["cost"])
                serve = Beer(item["serve"])
            bar.add_item(item)
    except FileNotFoundError:
        print ("Bar not on file, beginning new bar list.")