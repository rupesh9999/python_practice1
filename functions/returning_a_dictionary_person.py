def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
# Example usage:    

musician = build_person('jimi', 'hendrix')
print(musician)