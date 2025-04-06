class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Return a neatly formatted descriptive name."""
        return f"{self.restaurant_name} serves {self.cuisine_type}."

    def open_restaurant(self):
        """Return a message indicating that the restaurant is open."""
        return f"{self.restaurant_name} is open!"

    def set_number_served(self, number_served):
        """Set the number of customers served."""
        self.number_served = number_served

    def increment_number_served(self, customers):
        """Increment the number of customers served."""
        self.number_served += customers
# Example usage:    
my_restaurant = Restaurant("The Great Restaurant", "Italian")
print(my_restaurant.describe_restaurant())
print(my_restaurant.open_restaurant())
my_restaurant.set_number_served(5)
print(f"Number of customers served: {my_restaurant.number_served}")
my_restaurant.increment_number_served(3)
print(f"Number of customers served: {my_restaurant.number_served}")