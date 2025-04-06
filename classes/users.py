class Users:
    """A class to represent a user."""

    def __init__(self, first_name, last_name):
        """Initialize first and last name attributes."""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Print a summary of the user."""
        print(f"User's name: {self.first_name} {self.last_name}")

    def greet_user(self):
        """Print a personalized greeting."""
        print(f"Hello, {self.first_name} {self.last_name}!")

# Creating instances of the Users class
user1 = Users("John", "Doe")
user2 = Users("Jane", "Smith")

# Calling methods for each instance
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()