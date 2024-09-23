from functions.basic import mainMenu
from functions.stock_function import addStock, listItem
from functions.file_function import saveFile, loadFile
from classes.bar import Bar

# App welcome
print ("Cocktail Reference Application\n")

# Load in database
bar = Bar(str.lower(input("Name of your bar: ")))
loadFile (bar) #if file does not exist, new bar will be created.
# print (bar)

# Menu
choice = ""
while choice != "E":
    choice = mainMenu()
    match choice:
        case "1": 
            # Add a stock item
            addStock(bar)
        case "2": 
            # Create mix
            pass           

        case "3": 
            # Search for an item
                # Search by name
                # Search by reference
            pass
        case "4": 
            # View lists
            listItem(bar)
                # See beers
                # See wines
                # See sprits
                # See mixes
                # See all
            pass
        case "5":
            # Remove any item
            pass
        case "E":
            # Save then end loop to close application
            saveFile(bar)
        case _:
            print ("Invalid input, try again.\n")
        


print ("Thank for for using the cocktail reference application!")
