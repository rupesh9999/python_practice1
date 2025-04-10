from privileges import Admin

#create an admin instance
admin_user = Admin("Jane", "Doe", "jane.doe@example.com")

#describe the admin user
admin_user.describe_user()

#greet the admin user
admin_user.greet_user()

#increment login attempts
admin_user.privileges.show_privileges()