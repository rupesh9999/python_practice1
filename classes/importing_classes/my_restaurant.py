from restaurant import Restaurant, IceCreamStand
# Create an instance of Restaurant

my_restaurant = Restaurant("The Gourmet Kitchen", "French")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(20)
my_restaurant.increment_number_served(5)

# Create an instance of IceCreamStand
my_ice_cream_stand = IceCreamStand("Sweet Treats", "Dessert")
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.open_restaurant()
my_ice_cream_stand.add_flavor("Vanilla")
my_ice_cream_stand.add_flavor("Chocolate")
my_ice_cream_stand.add_flavor("Strawberry")
my_ice_cream_stand.show_flavors()
my_ice_cream_stand.remove_flavor("Vanilla") 
my_ice_cream_stand.show_flavors()   
my_ice_cream_stand.set_number_served(50)
my_ice_cream_stand.increment_number_served(10)
my_ice_cream_stand.show_flavors()
