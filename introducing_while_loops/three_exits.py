prompt = "\nTell me something, which pizza toppings you would like to add:"
prompt += "\n(Enter 'quit' when you are finished.)"

# Using a conditional test in the while statement
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(f"I' ve added {message} to your pizza!")

# Using an active variable
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(f"I' ve added {message} to your pizza!")

# Using a break statement
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(f"I' ve added {message} to your pizza!")
