# Functions 

## Exercise 1.py 

import random

def roll_dice():
    return random.randint(1, 6)

# Main program
result = 0
while result != 6:
    result = roll_dice()
    print(f"Rolled: {result}")

## Exercise 2.py

import random

def roll_dice(sides):
    return random.randint(1, sides)

# Main program
sides = int(input("Enter the number of sides on the dice: "))

result = 0
while result != sides:
    result = roll_dice(sides)
    print(f"Rolled: {result}")

## Exercise 3.py

def gallons_to_liters(gallons):
    return gallons * 3.78541

# Main program
while True:
    gallons = float(input("Enter volume in American gallons (negative to quit): "))
    if gallons < 0:
        break
    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallons is {liters:.2f} liters.")

## Exercise 4.py

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Main program
sample_list = [4, 7, 12, 3, 9]
result = sum_list(sample_list)

print(f"List: {sample_list}")
print(f"Sum: {result}")

## Exercise 5.py

def remove_uneven(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Main program
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = remove_uneven(original_list)

print(f"Original list: {original_list}")
print(f"Cut-down list: {filtered_list}")

## Exercise 6.py

import math

def calculate_unit_price(diameter_cm, price_eur):
    radius_m = (diameter_cm / 100) / 2
    area_m2 = math.pi * (radius_m ** 2)
    return price_eur / area_m2

# Main program
p1_diameter = float(input("Enter Pizza 1 diameter (cm): "))
p1_price = float(input("Enter Pizza 1 price (€): "))

p2_diameter = float(input("Enter Pizza 2 diameter (cm): "))
p2_price = float(input("Enter Pizza 2 price (€): "))

p1_unit_price = calculate_unit_price(p1_diameter, p1_price)
p2_unit_price = calculate_unit_price(p2_diameter, p2_price)

print(f"\nPizza 1 unit price: €{p1_unit_price:.2f} per m²")
print(f"Pizza 2 unit price: €{p2_unit_price:.2f} per m²")

if p1_unit_price < p2_unit_price:
    print("Pizza 1 offers better value for money.")
elif p2_unit_price < p1_unit_price:
    print("Pizza 2 offers better value for money.")
else:
    print("Both pizzas offer equal value for money.")
