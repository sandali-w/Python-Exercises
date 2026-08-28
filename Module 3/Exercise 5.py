talents = float (input("Enter talents:\n"))
pounds = float (input("Enter pounds:\n"))
lots = float (input("Enter lots:\n"))

# Conversations 
# 1 talent = 20 pounds; 1 pound =32 lots; 1 lot = 13.3 grams
total_lots = (talents * 20 * 32) + (pounds * 32) + lots
total_grams = total_lots * 13.3
kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print(f"\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams")