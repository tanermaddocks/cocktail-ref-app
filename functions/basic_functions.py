# Simple independent functions.

def mainMenu():
    print ("What would you like to do?\n")
    print ("1. Add beverage.")
    print ("2. Remove beverage.")
    print ("3. Search for a drink.")
    print ("4. View drink lists.")
    print ("5. Create cocktail.")
    print ("6. Delete a cocktail.")
    print ("E. Exit application.")
    choice = str.upper (input ("\nEnter your choice here: "))
    return choice

