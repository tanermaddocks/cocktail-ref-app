# Cocktail Reference Application

This terminal application will be used to display information about beers, wines, spirits and other alcoholic beverages, that would be stocked in a bar.

A user will be able to add and remove items to the database and retrieve an item's information (alcohol percentage/standard drinks, where it's from, serving size, etc.) using a search function.

The core feature of the app will be to take user input and 'mix' items and retrieve the new combined items information, allowing users to see and create information regarding cocktails.

### Classes 

- Beverage Class: The parent class for all possible drinks. It will contain at least the alcohol percentage/standard drink in it's constructor.

    - Spirit Class: Will contain information regarding spirits.
    - Beer Class: Will contain information regarding beers.
    - Wine Class: Will contain information regarding wines.

- Mixes Class: Will save and retrieve information regarding user made mixes (cocktails). This class will also run the user input to create the mix in the first place.