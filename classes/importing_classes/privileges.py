from user import User

class Privileges:
    """A class to manage admin privileges."""

    def __init__(self):
        """Initialize privileges."""
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Display the admin's privileges."""
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """A class representing an admin user."""

    def __init__(self, first_name, last_name, email):
        """Initialize admin attributes."""
        super().__init__(first_name, last_name, email)
        self.privileges = Privileges()