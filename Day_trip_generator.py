destinations = ["Denver", "Golden", "Gunnison", "Colorado Springs"] # Lists of items for the day trip
restaurants = ["Pizza Shop", "BBQ Pit", "Buffet", "Bar and Grill"]
transportation = ["Car", "Bus", "Walk", "Bike"]
entertainment = ["Live Music", "Movie", "Rodeo", "Arcade"]

import random



def pick_random_item(list_of_items):
    selected_item = random.choice(list_of_items)  # Random Generator for lists above
    return selected_item

def print_day_trip(day_trip_components):    # Function to print full day trip
        print(f"Destination: {day_trip_components[0]}")
        print(f"Restaurant: {day_trip_components[1]}")
        print(f"Transportation: {day_trip_components[2]}")
        print(f"Entertainment: {day_trip_components[3]}")


def day_trip_generator():
    your_destination = pick_random_item(destinations) # Random Destination Generator
    print("Destination: ", your_destination)
    
    your_restaurant = pick_random_item(restaurants)  # Random restaurant generator
    print("Restaurant: ", your_restaurant)

    your_transportation = pick_random_item(transportation) # Random transportation generator
    print("Transportation: ", your_transportation)

    your_entertainment = pick_random_item(entertainment) # Random entertainment generator
    print("Entertainment: ", your_entertainment)

    day_trip_components = [your_destination, your_restaurant, your_transportation, your_entertainment]

    valid_response = False
    while valid_response == False:                      # While loop to determine if user is satisfied with trip
        choice = input("Are you satisfied with your day trip? Yes or No ")
   
        if choice == "No":
            altered_choice =  input("What would you like to change? Destination, Restaurant, Transportation, or Entertainment ")
            
            if altered_choice == "Destination":
                your_destination = pick_random_item(destinations)
                print_day_trip(your_destination, your_restaurant, your_transportation, your_entertainment)
                valid_response = False
            elif altered_choice == "Restaurant":
                your_restaurant = pick_random_item(restaurants)
                print_day_trip(your_destination, your_restaurant, your_transportation, your_entertainment)
                valid_response = False
            elif altered_choice == "Transportation":
                your_transportation = pick_random_item(transportation)
                print_day_trip(your_destination, your_restaurant, your_transportation, your_entertainment)
                valid_response = False
            elif altered_choice == "Entertainment":
                your_entertainment = pick_random_item(entertainment)
                print_day_trip(your_destination, your_restaurant, your_transportation, your_entertainment)
                valid_response = False
            else:
                print("Please select an item to change")     # Finishes condition and resets to line 37
        elif choice == "Yes":
            print("Enjoy your trip!")
            valid_response = True
    print(f"Here is your complete day trip!")
    print_day_trip(your_destination, your_restaurant, your_transportation, your_entertainment)
day_trip_generator()

