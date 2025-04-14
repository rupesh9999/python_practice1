def read_file(filename):
    """Read the contents of a file and print them."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"Contents of {filename}:")
        print(contents)

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    read_file(filename)
