class User:
    """A simple user class."""
    def __init__(self, first_name, last_name, age, location):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Print a statement describing the user."""
        print(f"user: {self.first_name} {self.last_name}, age: {self.age}, location: {self.location}")

    def greet_user(self):
        """Print a statement greeting the user."""
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

    def increment_login_attempts(self):
        """Increment the login attempts by 1."""
        self.login_attempts += 1

class Privileges:
    """A class to manage admin privileges."""

    def __init__(self):
        """Initialize privileges attributes."""
        self.privileges = ["can add post", "cann delete post", "can ban user"]

    def show_privileges(self):
        """Display the admin's privileges."""
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """A class representing an admin user."""
    def __init__(self, first_name, last_name, age, location):
        """Initialize admin attributes."""
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()