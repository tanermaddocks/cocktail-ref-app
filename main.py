from functions.basic_functions import mainMenu

# App welcome
print ("Cocktail Reference Application")

# Load in database


# Menu
choice = ""
while choice != "E":
    choice = mainMenu()
    match choice:
        case "1": 
            # Add an item
            pass
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
