sandwich_orders = ["tuna", "pastrami", "chicken", "pastrami", "vegetarian", "ham and cheese", "egg salad", "pastrami"]
finished_sandwiches = []

print("Sorry, we're out of pastrami today.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print("\nSandwich orders:")
for sandwich in sandwich_orders:
    print(f"- {sandwich}")

print("\nFinished sandwiches:")
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"- {sandwich}")
    finished_sandwiches.append(sandwich)

print("\nAll finished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")