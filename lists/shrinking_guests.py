# start with a list of guests
guests = ["Alice", "Bob", "Charlie", "David"]
print("Original list of guests:", guests)

# Use pop() to remove the last guest and notify them
removed_guest = guests.pop()
print(f"Sorry {removed_guest.title()}, you cant come anymore.")

# Use pop() to remove the last guest and notify them
removed_guest = guests.pop()
print(f"Sorry {removed_guest.title()}, you cant come anymore.")     

# Tell remaining guests they're still invited
print("\nGuests still invited:")
print(f"Hey {guests[0].title()}, you're still invited.")
print(f"Hey {guests[1].title()}, you're still invited.")        

# Use del to empty the list
del guests[1]  # Remove the second guest
del guests[0]  # Remove the first guest

# show the empty list
print("\nGuest list after the party:", guests)