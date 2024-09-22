# Simple independent functions.

def mainMenu():
    print ("\nWhat would you like to do?\n")
    print ("1. Add stock.")
    print ("2. Create cocktail.")
    print ("3. Search for a drink.")
    print ("4. View drink lists.")
    print ("5. Remove item.")
    print ("E. Exit application.")
    choice = str.upper (input ("\nEnter your choice here: "))
    return choice

def capitalFullString(string):
    string_list = str.split(string)
    for word in string_list:
        str.capitalize(word)
    string = " ".join(string_list)
    return string