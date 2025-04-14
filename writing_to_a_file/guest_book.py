filename = 'guest_book.txt'

while True:
    name = input("Please enter your name (or 'quit' to exit): ")
    if name.lower() == 'quit':
        break
    
    with open(filename, 'a') as file_object:
        file_object.write(name + "\n")
    print(f"Hello {name}, you've been added to the guest book.")
    print("Your name has been recorded.")