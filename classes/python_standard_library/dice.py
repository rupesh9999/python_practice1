class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        import random
        return random.randint(1, self.sides)
    
    def __str__(self):
        return f"Dice with {self.sides} sides"
    
    def __repr__(self):
        return f"Dice({self.sides})"
    
# Example usage
if __name__ == "__main__":
    dice = Dice()
    print(dice)  # Output: Dice with 6 sides
    print(dice.roll())  # Output: Random number between 1 and 6
    dice_10 = Dice(10)
    print(dice_10)  # Output: Dice with 10 sides
    print(dice_10.roll())  # Output: Random number between 1 and 10
    dice_20 = Dice(20)
    print(dice_20)  # Output: Dice with 20 sides
    print(dice_20.roll())  # Output: Random number between 1 and 20
    dice_100 = Dice(100)
    print(dice_100)  # Output: Dice with 100 sides  
    print(dice_100.roll())  # Output: Random number between 1 and 100