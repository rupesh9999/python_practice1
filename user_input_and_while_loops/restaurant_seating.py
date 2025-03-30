restaurant_seating = input("Enter the restaurant seating arrangement: ")
restaurant_seating = int(restaurant_seating)

if restaurant_seating > 8:
    print(f"\nYou'll have to wait for a table.")
else:
    print(f"\nYour table is ready.")