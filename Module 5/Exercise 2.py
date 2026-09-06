INCH_TO_CM = 2.54

while True:
    inches = float(input("Enter length in inches(negative number to quit):"))
    if inches < 0:
        print("Program ended.")
        break
    cm = inches * INCH_TO_CM
    print(f"{inches} inches = {cm:.2f} cm")
    