import random

def roll_dice(sides):
    return random.randint(1, sides)

# Main program
sides = int(input("Enter the number of sides on the dice: "))

result = 0
while result != sides:
    result = roll_dice(sides)
    print(f"Rolled: {result}")