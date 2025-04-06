class Restaurant:
    """A Class to represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a summary of the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is open!")

# Creating three instances of the Restaurant class
restaurant1 = Restaurant("The Great Indian Curry", "Indian")
restaurant2 = Restaurant("Pasta Paradise", "Italian")
restaurant3 = Restaurant("Sushi Spot", "Japanese")

# Calling describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
