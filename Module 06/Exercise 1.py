import random

num_dice = int(input("How many dice to roll? "))
total_sum = 0

for _ in range(num_dice):
    total_sum += random.randint(1, 6)

print(f"Total sum of dice rolls: {total_sum}")
