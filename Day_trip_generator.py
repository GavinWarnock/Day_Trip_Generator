destinations = ["Denver", "Golden", "Gunnison", "Colorado Springs"]
restaurants = ["Pizza Shop", "BBQ Pit", "Buffet", "Bar and Grill"]
transportation = ["Car", "Bus", "Walk", "Bike"]
entertainment = ["Live Music", "Movie", "Rodeo", "Arcade"]

import random

def pick_random_item(list_of_items):
    selected_item = random.choice(list_of_items)  # Random Generator for lists above
    return selected_item

your_destination = pick_random_item(destinations) # Random Destination Generator
print("Destination: ", your_destination)

you_restaurant = pick_random_item(restaurants)  # Random restaurant generator
print("Restaurant: ", you_restaurant)

your_transportation = pick_random_item(transportation)
print("Transportation: ", your_transportation)

your_entertainment = pick_random_item(entertainment)
print("Entertainment: ", your_entertainment)