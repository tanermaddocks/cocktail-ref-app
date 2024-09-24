# Simple independent functions.

def mainMenu():
    print ("\nWhat would you like to do?\n")
    print ("1. Add stock.")
    print ("2. Create cocktail.")
    print ("3. Search for a drink.")
    print ("4. View drink lists.")
    print ("5. Remove item.")
    print ("E. Exit application.")
    choice = str.upper(input ("\nEnter your choice here: "))
    print()
    return choice

def capitalFullString(string):
    string_list = string.lower().split()
    string_list_cap = []
    for word in string_list:
        string_list_cap.append(word.capitalize())
    string_cap = " ".join(string_list_cap)
    return string_cap

def standardCalc(alcpercent, vol): #unused as of now
    standard = round(((alcpercent/100 * vol)/(10/0.78)), 2)
    return standard

def fileForm(bar_name):
    bar_no_special = []
    for character in bar_name:
        if character not in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"':
            bar_no_special.append(character.lower())
    bar_name_file = "_".join(("".join(bar_no_special)).split())
    return bar_name_file

def valueErrorCheck(prompt):
    value = 1
    while value != 0:
        try: 
            value = float(input(prompt))
            break
        except ValueError: 
            print ("Must be a number, please try again.\n")
            continue
    return value
 
def wrongChoice(includeMix):
    if includeMix:
        print ("Invalid item type, choose from beer, wine spirit or cocktail.")
    else:
        print ("Invalid item type, choose from beer, wine or spirit.")

def serveSize(serve): #unused as of now
    match serve:
        case "pot": serve_mL = 285
        case "schooner": serve_mL = 425
        case "pint": serve_mL = 570
        case "stein": serve_mL = 1000
    return serve_mL