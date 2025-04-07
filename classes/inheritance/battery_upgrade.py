class Car:
    """A simple car class"""
    def __init__(self, make, model, year):
        """Initialize car attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """Set the odometer reading"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add miles to the odometer"""
        self.odometer_reading += miles

class Battery:
    """A simple battery class for electric vehicles"""
    def __init__(self, battery_size=75):
        """Initialize battery attributes"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print the range based on battery size"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        """Upgrade battery to 100 kWh if it's not already"""
        if self.battery_size != 100:
            self.battery_size = 100
            print("Battery has been upgraded to 100 kWh!")
        else:
            print("Battery is already at maximum capacity (100 kWh).")

class ElectricCar(Car):
    """A class for electric vehicles"""
    def __init__(self, make, model, year):
        """Initialize attributes of parent class and electric car"""
        super().__init__(make, model, year)
        self.battery = Battery()

# Create an electric car instance
my_tesla = ElectricCar("tesla", "model s", 2023)

# Test the initial setup
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Upgrade the battery and test again
print("\nUpgrading battery...")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Try upgrading again
print("\nAttempting to upgrade again...")
my_tesla.battery.upgrade_battery()