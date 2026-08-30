# 1. Zander length check
length = float(input("Enter the length of the zander in centimeters: "))

if length < 42:
    difference = 42 - length
    print(
        f"Please release the fish back into the lake. It is {difference:.1f} cm below the size limit."
    )
else:
    print("The zander meets the size limit.")