import random

class Die:
    """A class to represent a single die"""

    def __init__(self, sides=6):
        """Initialize the die with a given number of sides """
        self.sides = sides

    def roll_die(self):
        """Return a random number between 1 and the number of sides"""
        return random.randint(1, self.sides)
    
# create a 6  sided die and a 10 sided die
d6 = Die()
d10 = Die(10)

# lists to roll results
d6_rolls = []
d10_rolls = []

#roll each die 10 times
for roll in range(10):
    d6_result = d6.roll_die()
    d10_result = d10.roll_die()
    d6_rolls.append(d6_result)
    d10_rolls.append(d10_result)
    print(f"Roll {roll + 1}: d6 = {d6_result}, d10 = {d10_result}")

# calculate and print the sum of all rolls for each die
d6_total = sum(d6_rolls)
d10_total = sum(d10_rolls)
print(f"\nTotal for D6 rolls: {d6_total}")
print(f"Total for D10 rolls: {d10_total}")