places = ['tokyo', 'paris', 'new york', 'sydney', 'rome']

print("Original order:")
print(places)

print("\nAlphabetical order:")
print(sorted(places))

print("\nOriginal order again:")
print(places)

print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))

print("\nOriginal order again:")
print(places)

places.reverse()
print("\nReversed order:")
print(places)

places.reverse()
print("\nOriginal order again:")
print(places)

places.sort()
print("\nAlphabetical order:")
print(places)

places.sort(reverse=True)
print("\nReverse alphabetical order:")
print(places)
