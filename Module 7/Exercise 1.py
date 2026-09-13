import random

def roll_dice():
    return random.randint(1, 6)

# Main program
result = 0
while result != 6:
    result = roll_dice()
    print(f"Rolled: {result}")