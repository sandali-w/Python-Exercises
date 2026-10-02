def main():
    # Prompt the user for age check
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Check age requirement
    if age < 12:
        print("You are a minor. Program shutting down.")
        return

    # Greet user if age is 12 or older 
    print("Welcome to the Game!")

    # Main menu loop
    while True:
        print("\n--- MAIN MENU ---")
        print("1. explore - Explore the mysterious forest")
        print("2. status  - Check your character status")
        print("3. inventory - View your items")
        print("4. lopeta  - Exit the game")
        
        command = input("\nEnter a command: ").lower()

        if command == "lopeta":
            print("Goodbye!")
            break
        elif command == "explore":
            print("You ventured into the dark woods and found a shiny gemstone!")
        elif command == "status":
            print("Health: 100/100 | Mana: 50/50 | Level: 1")
        elif command == "inventory":
            print("Your bag contains: 1x Wooden Sword, 3x Health Potions.")
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
    