from functions.basic import mainMenu, fileForm
from functions.item_function import *
from functions.file_function import saveFile, loadInfo, loadMenu
from functions.common_print import exitMessage

# App welcome
print ("Cocktail Reference Application\n")

# Load in database
barname = fileForm(str(input("Name of your bar: ")))
bar = loadInfo(barname) #if file does not exist, new bar will be created.
loadMenu(bar)

# Menu
choice = ""
while choice != "e":
    choice = mainMenu()
    match choice:
        case "1": 
            # Add a stock item
            addStock(bar)
        case "2": 
            # Create mix
            pass           
        case "3":
            searchItem(bar)
            # Search for an item
                # Search by name
                # Search by code
            pass
        case "4": 
            # View lists
            listItem(bar)
                # See beers
                # See wines
                # See sprits
                # See mixes
                # See all
        case "e":
            # End loop to close application
            saveFile(bar)
        case _:
            print ("Invalid input, try again.")
        
exitMessage()
