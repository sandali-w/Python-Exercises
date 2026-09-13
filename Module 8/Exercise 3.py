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