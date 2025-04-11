filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readline()

pi_string_1 = ''
for line in lines:
    pi_string_1 += line.strip()

print(f"{pi_string_1[:52]}...")
print(len(pi_string_1))

for line in lines:
    pi_string_1 += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string_1:
    print("Your birthday appears in the first million digits of pi!")

else:
    print("Your birthday does not appear in the first million digits of pi.")