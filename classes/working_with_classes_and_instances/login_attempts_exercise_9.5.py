class Users:
    """A Class to represent a user."""

    def __init__(self, first_name, last_name, login_attempts):
        """Initialize the user's attributes."""
        self.first_name = first_name 
        self.last_name = last_name
        self.login_attempts = login_attempts 
        self.login_attempts = 0

    def describe_user(self):
        """Return a neatly formatted descriptive name."""
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.title()
    
    def greet_user(self):
        """Print a greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        """Increment the number of login attempts by 1."""
        self.login_attempts += 1
        print(f"Login attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        """Reset the number of login attempts to 0."""
        self.login_attempts = 0
        print(f"Login attempts reset to: {self.login_attempts}")

# Example usage:
user = Users('John', 'Doe', 0)
print(user.describe_user())
user.greet_user()
user.increment_login_attempts()
user.reset_login_attempts()
