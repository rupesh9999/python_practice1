# List of sandwich orders
sandwich_orders = ["tuna", "chicken", "vegetarian", "ham and cheese", "egg salad"]

# Empty list to store finished sandwiches
finished_sandwiches = []

# Process each sandwich order
while sandwich_orders:
    # Take the first sandwich from the orders list
    sandwich = sandwich_orders.pop(0)
    # Print a message indicating the sandwich is made
    print(f"I made your {sandwich} sandwich.")
    # Add the sandwich to the finished list
    finished_sandwiches.append(sandwich)

# Display all finished sandwiches
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")