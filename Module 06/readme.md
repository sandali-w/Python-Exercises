# List Structures and Iterative loops (for)

## Exercise 1.py
import random

num_dice = int(input("How many dice to roll? "))
total_sum = 0

for _ in range(num_dice):
    total_sum += random.randint(1, 6)

print(f"Total sum of dice rolls: {total_sum}")

## Exercise 2.py 
numbers = []

while True:
    user_input = input("Enter a number (press Enter to quit): ")
    if user_input == "":
        break
    numbers.append(float(user_input))

numbers.sort(reverse=True)
top_five = numbers[:5]

print("Five greatest numbers in descending order:")
for num in top_five:
    print(num)

## Exercise 3.py
number = int(input("Enter an integer: "))

if number <= 1:
    print(f"{number} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

## Exercise 4.py
cities = []

for i in range(5):
    city = input(f"Enter city name {i + 1}: ")
    cities.append(city)

print("\nCities entered:")
for city in cities:
    print(city)