current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    # This will skip even numbers
    # The following line will not be executed for even numbers
    # It will only print odd numbers
    # The above code will print odd numbers from 1 to 9
    print(current_number)