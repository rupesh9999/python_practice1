prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""

active = True
while active:
    meassage = input(prompt)

    if message == 'quit':
#        active = False
      break
    else:
        print(f"I'd love to go to {prompt.title}")
# The above code will repeat the user's input until they enter 'quit'