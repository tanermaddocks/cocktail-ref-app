def exitMessage():
    print ("Thank for for using the cocktail reference application!")

def invalidEntry():
    print ("Invalid entry, try again.")

def wrongChoice(includeMix):
    if includeMix:
        print ("Invalid item type, choose from beer, wine spirit or cocktail.")
    else:
        print ("Invalid item type, choose from beer, wine or spirit.")