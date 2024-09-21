from functions.basic import mainMenu
from functions.stock_function import addItem
from classes.bar import Bar

# App welcome
print ("Cocktail Reference Application")

# Load in database

bar = Bar(str.lower(input("Name of your bar: ")))
# print (bar)

# Menu
choice = ""
while choice != "E":
    choice = mainMenu()
    match choice:
        case "1": 
            print(addItem(bar))
        case "2": 
            # Remove an item
            pass
        case "3": 
            # Search for an item
                # Search by name
                # Search by reference
            pass
        case "4": 
            # View lists
                # See beers
                # See wines
                # See sprits
                # See mixes
                # See all
            pass
        case "5":
            # Create mix
            pass
        case "6": 
            # Remove mix
            pass
        case "E":
            # Close application
            pass
        case _:
            print ("Invalid input, try again.\n")
        


print ("\nThank for for using the cocktail reference application!")
