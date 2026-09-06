cities = []

for i in range(5):
    city = input(f"Enter city name {i + 1}: ")
    cities.append(city)

print("\nCities entered:")
for city in cities:
    print(city)