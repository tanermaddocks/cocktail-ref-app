import json
from classes.stock import Beverage, Beer, Wine, Spirit
from functions.basic import underscoreBar

def saveExit(bar):
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
    with open(f"data/{underscoreBar(bar)}.json", "w") as json_file:
        json.dump(item_dict, json_file, indent=4)

def loadFile(bar):
    try:
        with open(f"data/{underscoreBar(bar)}.json", "r") as json_file:
            item_dict = json.load(json_file)
        for bev in item_dict:
            # if item.get("beer"):
            bev = Beverage(bev["name"]["alc"]["cost"]["type"]["serve"]) #FIGURE PROPER SETUP
            bar.add_item(bev)
    except FileNotFoundError:
        print ("Bar not on file, beginning new bar list.")