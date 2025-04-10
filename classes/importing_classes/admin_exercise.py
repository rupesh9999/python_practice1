from imported_admin import Admin

# create an admin instance
admin_user = Admin("Jane", "Doe", 30, "New York")

# describe the admin user
admin_user.describe_user()

# greet the admin user
admin_user.greet_user()

# increment login attempts
admin_user.increment_login_attempts()
print(f"Login attempts: {admin_user.login_attempts}")

# show the admin's privileges
admin_user.privileges.show_privileges()