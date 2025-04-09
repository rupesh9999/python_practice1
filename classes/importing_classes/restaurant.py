"""A restaurant used to represent a different cuisines."""

class Restaurant:
    """A simple attempt to represent a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print a statement describing the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a statement that the restaurant is open."""
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, number_served):
        """Set the number of customers served."""
        self.number_served = number_served
        print(f"{self.restaurant_name} has served {self.number_served} customers.")

    def increment_number_served(self, number_served):
        """Increment the number of customers served."""
        self.number_served += number_served
        print(f"{self.restaurant_name} has served {self.number_served} customers.")

class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant, specific to ice cream stands."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Print a statement showing the ice cream flavors available."""
        print(f"{self.restaurant_name} offers the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")
    def add_flavor(self, flavor):
        """Add a new flavor to the list of flavors."""
        self.flavors.append(flavor)
        print(f"{flavor} has been added to the menu.")
    def remove_flavor(self, flavor):
        """Remove a flavor from the list of flavors."""
        self.flavors.remove(flavor)
        print(f"{flavor} has been removed from the menu.")

        