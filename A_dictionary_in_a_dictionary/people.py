people = []

person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 46,
    'city': 'sitka',
}
people.append(person)

person = {
    'first_name': 'willie',
    'last_name': 'matthes',
    'age': 11,
    'city': 'sitka',
}
people.append(person)

person = {
    'first_name': 'erin',
    'last_name': 'matthes',
    'age': 43,
    'city': 'vienna',
}
people.append(person)

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"Hi I am {name}, of {city}, is {age} years old.")
