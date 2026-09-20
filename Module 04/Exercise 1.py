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