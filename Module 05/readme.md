# While Loops (While)

## Exercise 1.py
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1
    
## Exercise 2.py
INCH_TO_CM = 2.54

while True:
    inches = float(input("Enter length in inches(negative number to quit):"))
    if inches < 0:
        print("Program ended.")
        break
    cm = inches * INCH_TO_CM
    print(f"{inches} inches = {cm:.2f} cm")

## Exercise 3.py
numbers = []

while True:
    user_input = input("Enter a number (press Enter to quit): ")
    if user_input == "":
        break 
    numbers . append (float(user_input))

    if numbers:
        print (f"Smallest number:{min(numbers)}")
        print (f"Largest number:{max(numbers)}")
    else: 
        print("No numbers were entered.")

## Exercise 4.py
import random 

target_number = random.randint (1, 10)

while True: 
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < target_number:
        print ("Too low")
    elif guess > target_number:
        print ("Too high")
    else : 
        print ("Correct")
        break

## Exercise 5.py
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter username:")
    password = input("Enter password:")

    if username == "Python" and password == "rules":
        print("Welcome")
        break 
    else:
        attempts += 1 

    if attempts == max_attempts :
        print ("Access denied")
        
## Exercise 6.py
import random

total_points = int(input("How many random points to generate? "))
points_inside_circle = 0

for _ in range(total_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        points_inside_circle += 1

pi_approximation = 4 * (points_inside_circle / total_points)
print(f"Approximated value of pi: {pi_approximation}")