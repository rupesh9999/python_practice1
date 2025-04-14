filename = 'programming_poll.txt'

while True:
    reason = input("Why do you like programming? (or 'quit' to exit): ")
    if reason.lower() == 'quit':
        break
    
    with open(filename, 'a') as file_object:
        file_object.write(reason + "\n")
    print("Thank you for sharing your reason!")
