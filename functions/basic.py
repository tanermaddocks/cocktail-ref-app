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

def standardCalc(alcpercent, vol):
    standard = round(((alcpercent/100 * vol)/12.5), 2)
    return standard

def underscoreBar (bar_name):
    bar_name_list = str.split(str(bar_name))
    bar_name_join = "_".join(bar_name_list)
    return bar_name_join