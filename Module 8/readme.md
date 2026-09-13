# Tuple, set and dictionary

## Exercise 1.py

# Tuple storing four seasons (winter, spring, summer, autumn)
seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter month number (1-12): "))

# Dec (12), Jan (1), Feb (2) -> winter (index 0)
# Mar (3), Apr (4), May (5) -> spring (index 1)
# Jun (6), Jul (7), Aug (8) -> summer (index 2)
# Sep (9), Oct (10), Nov (11) -> autumn (index 3)
season_index = (month % 12) // 3

print(f"The season is {seasons[season_index]}.")

## Exercise 2.py

names_set = set()

while True:
    name = input("Enter a name (press Enter to stop): ").strip()
    if name == "":
        break
    
    if name in names_set:
        print("Existing name")
    else:
        print("New name")
        names_set.add(name)

print("\nList of entered names:")
for name in names_set:
    print(name)

## Exercise 3.py

airports = {}

while True:
    print("\nOptions:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    
    choice = input("Choose an option (1-3): ").strip()
    
    if choice == "1":
        icao = input("Enter ICAO code: ").strip().upper()
        name = input("Enter airport name: ").strip()
        airports[icao] = name
        print(f"Airport '{name}' saved under {icao}.")
        
    elif choice == "2":
        icao = input("Enter ICAO code to search: ").strip().upper()
        if icao in airports:
            print(f"Airport name: {airports[icao]}")
        else:
            print(f"No airport found for ICAO code '{icao}'.")
            
    elif choice == "3":
        print("Execution ended.")
        break
        
    else:
        print("Invalid option. Please enter 1, 2, or 3.")