# Conditional structures

## Exercise 1.py
length = float(input("Enter the length of the zander in centimeters: "))
size_limit = 42

if length < size_limit:
    difference = size_limit - length
    print(
        f"The zander does not meet the size limit. Please release it back into the lake."
    )
    print(
        f"It is {difference:.1f} centimeters below the size limit of {size_limit} cm."
    )
else:
    print("The zander meets the size limit.")

    ## Exercise 2.py 
    cabin_class = input("Enter the cabin class (LUX, A, B, C): ").strip().upper()

if cabin_class == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("A: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("B: windowless cabin above the car deck.")
elif cabin_class == "C":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

    ## Exercise 3.py
    hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin value is low.")
    elif hemoglobin <= 155:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
elif gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin value is low.")
    elif hemoglobin <= 167:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
else:
    print("Invalid gender entered.")

    ## Exercise 4.py
    year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")