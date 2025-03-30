prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""

active = True
while active:
    message = input(prompt)

    if message == 'quit':
#        active = False
      break
    else:
        print(message)
# The above code will repeat the user's input until they enter 'quit'
