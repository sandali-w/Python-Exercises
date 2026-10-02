# My awesome game 

Warnakulasuriya Sandali Crishenshiya Fernando

## project 1

# Ask for user input and store in variables
player_name = input("Enter your name: ")
player_age = input("Enter your age: ")

# Print the values to the console
print(f"Player Name: {player_name}")
print(f"Player Age: {player_age}")

## Project 2

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

## Project 3

def add_item(inventory):
    """Asks the user for an item and adds it to the inventory list."""
    item = input("Enter an item to add to your inventory: ")
    if item:
        inventory.append(item)
        print(f"'{item}' has been added to your inventory.")
    else:
        print("Item name cannot be empty.")

def show_inventory(inventory):
    """Prints all contents of the inventory list."""
    if not inventory:
        print("Your inventory is currently empty.")
    else:
        print("\n--- Current Inventory ---")
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")

def clear_inventory(inventory):
    """Clears all items from the inventory list."""
    if not inventory:
        print("Inventory is already empty.")
    else:
        inventory.clear()
        print("Your inventory has been cleared!")

def main():
    inventory = []
    
    while True:
        print("\n=== Main Menu ===")
        print("1. Add item to inventory")
        print("2. View inventory")
        print("3. Clear inventory")
        print("4. Exit game")
        
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            show_inventory(inventory)
        elif choice == "3":
            clear_inventory(inventory)
        elif choice == "4":
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

## Project 04

### item.py

class Item:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"

### room.py

class Room:
    def __init__(self, name: str, item=None):
        self.name = name
        self.item = item  # Can contain 0 or 1 Item

    def __str__(self):
        item_info = f" containing {self.item.name}" if self.item else " with no items"
        return f"{self.name}{item_info}"

### player.py

class Player:
    def __init__(self, name: str, location):
        self.name = name
        self.items = []       # List of items collected
        self.location = location  # Current Room object

    def move(self, destination):
        """Moves the player to a new room."""
        self.location = destination
        print(f"\n{self.name} moved to the {destination.name}.")

    def collect_item(self):
        """Collects the item from the current room if available."""
        if self.location.item:
            collected_item = self.location.item
            self.items.append(collected_item)
            self.location.item = None  # Remove item from room
            print(f"\n{self.name} picked up: {collected_item.name} ({collected_item.weight} kg)")
        else:
            print("\nThere is no item in this room to pick up.")

### main.py

from game.item import Item
from game.room import Room
from game.player import Player

def main():
    # 1. Initialize items
    sword = Item("Sword", 3.5)
    key = Item("Golden Key", 0.2)

    # 2. Initialize rooms
    hallway = Room("Hallway")
    armory = Room("Armory", item=sword)
    vault = Room("Vault", item=key)

    # 3. Create player at starting location
    player_name = input("Enter your hero's name: ")
    player = Player(name=player_name, location=hallway)

    # Available rooms map
    rooms = {
        "1": hallway,
        "2": armory,
        "3": vault
    }

    # Interactive Game Loop
    while True:
        print("\n" + "=" * 30)
        print(f"Player: {player.name}")
        print(f"Current Location: {player.location.name}")
        if player.location.item:
            print(f"Room Item: {player.location.item.name}")
        else:
            print("Room Item: None")
        
        inventory_names = [item.name for item in player.items]
        print(f"Inventory: {inventory_names if inventory_names else 'Empty'}")
        print("=" * 30)

        print("Actions:")
        print("1. Move to Hallway")
        print("2. Move to Armory")
        print("3. Move to Vault")
        print("4. Collect Item")
        print("5. Quit Game")

        choice = input("Choose an option (1-5): ").strip()

        if choice in ["1", "2", "3"]:
            destination = rooms[choice]
            player.move(destination)
        elif choice == "4":
            player.collect_item()
        elif choice == "5":
            print("\nThanks for playing! Goodbye.")
            break
        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    main()