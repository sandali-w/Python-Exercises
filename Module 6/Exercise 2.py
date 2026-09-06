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