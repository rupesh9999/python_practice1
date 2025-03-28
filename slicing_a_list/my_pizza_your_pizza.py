my_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = my_pizzas[:]

my_pizzas.append('meat lovers')
friend_pizzas.append('margherita')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
