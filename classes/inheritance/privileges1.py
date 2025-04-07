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
        """Display user information"""
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
    
    def greet_user(self):
        """Greet the user"""
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")
    
    def increment_login_attempts(self):
        """Increment the login attempts counter"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset login attempts to 0"""
        self.login_attempts = 0

class Privileges:
    """A class to manage admin privileges"""
    def __init__(self):
        """Initialize privileges attribute"""
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can modify settings",
            "can view logs"
        ]
    
    def show_privileges(self):
        """Display admin privileges"""
        print(f"\nAdmin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """A specialized class for an admin user"""
    def __init__(self, first_name, last_name, age, location):
        """Initialize attributes of parent class and Admin"""
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()

# Create an admin instance
admin_user = Admin("Jane", "Doe", 28, "Chicago")

# Test the methods
admin_user.describe_user()
admin_user.greet_user()
admin_user.privileges.show_privileges()

# Test login attempts
print(f"\nInitial login attempts: {admin_user.login_attempts}")
admin_user.increment_login_attempts()
admin_user.increment_login_attempts()
admin_user.increment_login_attempts()
print(f"Login attempts after increments: {admin_user.login_attempts}")
admin_user.reset_login_attempts()
print(f"Login attempts after reset: {admin_user.login_attempts}")