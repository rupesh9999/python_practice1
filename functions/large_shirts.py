def make_shirt(size='large', message='I love Python!'):
    """Prints the size and message of the shirt."""
    print(f"\nMaking a {size} t-shirt with the message: '{message}'.")

# call the function with default values
make_shirt()

# call the function with a different size but default message
make_shirt(size='medium')

# call the function with both custom size and message
make_shirt(size='small', message='Python is awesome!')