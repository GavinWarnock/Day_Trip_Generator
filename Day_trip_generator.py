destinations = ["Denver", "Golden", "Gunnison", "Colorado Springs"]
restaurants = ["Pizza Shop", "BBQ Pit", "Buffet", "Bar and Grill"]
transportation = ["Car", "Bus", "Walk", "Bike"]
entertainment = ["Live Music", "Movie", "Rodeo", "Arcade"]

import random



def pick_random_item(list_of_items):
    selected_item = random.choice(list_of_items)  # Random Generator for lists above
    return selected_item

def day_trip_generator():
    your_destination = pick_random_item(destinations) # Random Destination Generator
    print("Destination: ", your_destination)

    your_restaurant = pick_random_item(restaurants)  # Random restaurant generator
    print("Restaurant: ", your_restaurant)

    your_transportation = pick_random_item(transportation) # Random restaurant generator
    print("Transportation: ", your_transportation)

    your_entertainment = pick_random_item(entertainment) # Random entertainment generator
    print("Entertainment: ", your_entertainment)

    def print_day_trip():
        print(f"Destination: {your_destination}")
        print(f"Restaurant: {your_restaurant}")
        print(f"Transportation: {your_transportation}")
        print(f"Entertainment: {your_entertainment}")
 
    valid_response = False
    while valid_response == False:
        choice = input("Are you satisfied with your day trip? Yes or No ")
   
        if choice == "No":
            altered_choice =  input("What would you like to change? Destination, Restaurant, Transportation, or Entertainment ")
            
            if altered_choice == "Destination":
                your_destination = pick_random_item(destinations)
                print_day_trip()
                valid_response = False
            elif altered_choice == "Restaurant":
                your_restaurant = pick_random_item(restaurants)
                print_day_trip()
                valid_response = False
            elif altered_choice == "Transportation":
                your_transportation = pick_random_item(transportation)
                print_day_trip()
                valid_response = False
            elif altered_choice == "Entertainment":
                your_entertainment = pick_random_item(entertainment)
                print_day_trip()
                valid_response = False
            else:
                print("Please select an item to change")
        elif choice == "Yes":
            print("Enjoy your trip!")
            valid_response = True
    print(f"Here is your complete day trip!")
    print_day_trip()
day_trip_generator()

