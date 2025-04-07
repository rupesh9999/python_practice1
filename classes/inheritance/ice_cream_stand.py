class Restaurant:
    """A simple restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print a statement describing the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a statement indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_server(self, number_served):
        """Set the number of customers served."""
        self.number_served = number_served
        print(f"Number of customers served: {self.number_served}")

    def increment_number_served(self, number_served):
        """Increment the number of customers served by a given amount."""
        self.number_served += number_served
        print(f"Number of customers served: {self.number_served}")

class IceCreamStand(Restaurant):
    """A specialised class for an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        """Initialize attributes of the  parent class and IceCreamStand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        
    def display_flavors(self):
        """Display the available ice cream flavors."""
        print(f"\n{self.restaurant_name} has the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Example usage
my_ice_cream_stand = IceCreamStand("Sweet Treats")
my_ice_cream_stand.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint"]
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavors()
my_ice_cream_stand.open_restaurant()

my_ice_cream_stand.set_number_server(50)
my_ice_cream_stand.increment_number_served(20)