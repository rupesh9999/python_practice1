class User:
    """A class to represent a user profile."""

    def __init__(self, first_name, last_name, email):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Login attempts: {self.login_attempts}")


    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}!")
