import json

def get_stored_username():
    """Get stored username4 if available."""
    filename = 'username4.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"welcome back, {username}!")
    else:
        username = input("what is your name?")
        filename = 'username4.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"we'll remember you when you come back, {username}!")
            
greet_user()