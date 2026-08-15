# PE06 Classes
# This program creates a Restaurant class and recommends an open restaurant.

class Restaurant:

    # Constructor
    def __init__(self, restaurant_name, cuisine_type, open):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open = open

    # Display all restaurant information
    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)
        print("Open:", self.open)

    # Display whether the restaurant is open or closed
    def is_open(self):
        if self.open:
            print("Currently open")
        else:
            print("Currently closed")

    # Recommend a restaurant that is open
    @staticmethod
    def recommend(restaurant1, restaurant2, restaurant3):
        if restaurant1.open:
            return restaurant1
        elif restaurant2.open:
            return restaurant2
        elif restaurant3.open:
            return restaurant3
        else:
            return None


# Create three restaurant objects
restaurant1 = Restaurant("McDonalds", "Burgers", True)
restaurant2 = Restaurant("Pizza Hut", "Pizza", False)
restaurant3 = Restaurant("KFC", "Chicken", True)

# Describe each restaurant
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# Find an open restaurant
Opened = Restaurant.recommend(restaurant1, restaurant2, restaurant3)

# Display the recommended restaurant
if Opened:
    Opened.describe_restaurant()
    Opened.is_open()
else:
    print("All restaurants are currently closed.")