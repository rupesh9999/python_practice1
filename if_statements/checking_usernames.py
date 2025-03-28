current_users = ['admin', 'eric', 'willie', 'alice', 'bob']
new_users = ['andrew', 'eric', 'johny', 'alice', 'peter']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")
