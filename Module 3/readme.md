# Variables and interactive programs 

## Exercise 1.py
name = input("Enter your name: ")
print(f"Hello, {name}!")

## Exercise 2.py
import math

radius = float(input("Enter radius: "))
area = math.pi * radius**2 
print (f"The area of the circle is {area}")

## Exercise 3.py
length = float (input("Enter the length: "))
width = float (input ("Enter width: "))

perimeter = 2 * (length + width)
area = length * width 

print (f"Permeter: {perimeter}")
print (f"Area: {area}")

## Exercise 4.py
num1 = int (input("Enter first number:"))
num2 = int (input("Enter second number:"))
num3 = int (input("Enter third number:"))

num_sum = num1 + num2 + num3
product = num1 * num2 * num3 
average = num_sum / 3

print (f"Sum: {num_sum}")
print (f"Product: {product}")
print (f"Average: {average}")

## Exercise 5.py
num1 = int (input("Enter first number:"))
num2 = int (input("Enter second number:"))
num3 = int (input("Enter third number:"))

num_sum = num1 + num2 + num3
product = num1 * num2 * num3 
average = num_sum / 3

print (f"Sum: {num_sum}")
print (f"Product: {product}")
print (f"Average: {average}")

## Exercise 6.py
import random 

# 3_digit code (numbers between 0 and 9)
code_3digit = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0,9)}"

# 4_digit code (numbers between 1 and 6)
code_4digit = f"{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}"
print(f"3-digit code: {code_3digit}")
print(f"4-digit code: {code_4digit}")

