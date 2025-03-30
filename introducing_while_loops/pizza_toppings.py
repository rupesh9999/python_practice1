prompt = "\nTell me something, which pizza toppings you would like to add:"
prompt += "\n(Enter 'quit' when you are finished.)"

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(f"I' ve added {message} to your pizza!")
# The above code will repeat the user's input until they enter 'quit'
# The code will print the message with the added toppings