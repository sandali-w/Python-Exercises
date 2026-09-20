import random 

# 3_digit code (numbers between 0 and 9)
code_3digit = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0,9)}"

# 4_digit code (numbers between 1 and 6)
code_4digit = f"{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}"
print(f"3-digit code: {code_3digit}")
print(f"4-digit code: {code_4digit}")
