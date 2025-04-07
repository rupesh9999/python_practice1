class User:
    """A simple user class"""
    def __init__(self, first_name, last_name, age, location):
        """Initialize user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User: {self.first_name} {self.last_name}, Age: {self.age}, Location: {self.location}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

    def increment_login_attempts(self):
        """Increment the number of login attempts."""
        self.login_attempts += 1
        print(f"Login attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        """Reset the number of login attempts."""
        self.login_attempts = 0
        print("Login attempts reset to 0.")

class Admin(User):
    """A specialized class for an admin user"""
    def __init__(self, first_name, last_name, age, location):
        """Initialize attributes of the parent class and Admin."""
        super().__init__(first_name, last_name, age, location)
        self.privileges = ["can add post", "can delete post", "can ban user", "can modify settings", "can view logs"]



    def show_privileges(self):
        """Print a list of admin privileges."""
        print(f"\nAdmin Priviliges for {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Example usage
admin_user = Admin("John", "Doe", 30, "New York")

# Testing the User class methods
admin_user.describe_user()
admin_user.greet_user()
admin_user.show_privileges()

# Test login attempts
print(f"\nInitial login attempts: {admin_user.login_attempts}")
admin_user.increment_login_attempts()
admin_user.increment_login_attempts()
print(f"Login attempts after incrementing: {admin_user.login_attempts}")
admin_user.reset_login_attempts()
print(f"Login attempts after reset: {admin_user.login_attempts}")