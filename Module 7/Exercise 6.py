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
