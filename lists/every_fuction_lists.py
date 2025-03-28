cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Original list:")
print(cars)

print("\nSorted list:")
print(sorted(cars))

print("\nReversed sorted list:")
print(sorted(cars, reverse=True))

print("\nOriginal list again:")
print(cars)

cars.reverse()
print("\nReversed list:")
print(cars)

cars.reverse()
print("\nOriginal list again:")
print(cars)

cars.sort()
print("\nSorted list:")
print(cars)

cars.sort(reverse=True)
print("\nReverse sorted list:")
print(cars)

print("\nLength of the list:")
print(len(cars))

cars.append('nissan')
print("\nList after appending 'nissan':")
print(cars)

cars.insert(0, 'mercedes')
print("\nList after inserting 'mercedes' at index 0:")
print(cars)

popped_car = cars.pop()
print(f"\nPopped car: {popped_car}")
print("List after popping:")
print(cars)

removed_car = cars.pop(2)
print(f"\nRemoved car at index 2: {removed_car}")
print("List after removing:")
print(cars)

cars.remove('mercedes')
print("\nList after removing 'mercedes':")
print(cars)

del cars[0]
print("\nList after deleting element at index 0:")
print(cars)
