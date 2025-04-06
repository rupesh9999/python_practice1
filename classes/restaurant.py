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

# Creating an instance of the Restaurant class
my_restaurant = Restaurant("The Great Indian Curry", "Indian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()