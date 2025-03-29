favorite_numbers = {
    'john': [7, 14, 21],
    'jane': [3, 6, 9],
    'doe': [1, 2, 3],
    'alice': [4, 8, 12],
    'bob': [5, 10, 15],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")
# Output: