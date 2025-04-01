def make_shirt(size, message):
    """Prints the size and message of the shirt."""
    print(f"The shirt size is {size} and the message is {message}.")

# call the function with positional arguments
make_shirt('large', 'I love Python!')

# call the function with keyword arguments
make_shirt(message='I love Python!', size='large')