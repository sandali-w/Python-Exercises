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

## Project 05

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

### instructions.txt

Plaintext
==================================================
                HOW TO PLAY
==================================================
1. Choose options 1 to 3 to move between rooms.
2. Choose option 4 to pick up items in the room.
3. Keep track of your inventory and status.
4. Option 5 allows you to save and quit the game.
==================================================

### intro.txt

Plaintext
==================================================
        WELCOME TO THE ADVENTURE GAME!
==================================================
You wake up in a pitch-black room. The air is cold,
and you can hear distant echoes. Your main goal is
to explore the mysterious rooms, collect items, and
find your way out safely!

Good luck, brave explorer!
==================================================

### main.py

import os
import json
from game.player import Player
from game.room import Room
from game.item import Item

def load_text_file(filename):
    """Reads text files using absolute paths based on main.py's location"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"[{filename} file could not be found]\n"

def get_player_room(player):
    """Safely retrieves current room from Player object"""
    if hasattr(player, 'current_room'):
        return player.current_room
    elif hasattr(player, 'location'):
        return player.location
    elif hasattr(player, 'room'):
        return player.room
    return None

def set_player_room(player, room):
    """Safely updates current room on Player object"""
    if hasattr(player, 'current_room'):
        player.current_room = room
    elif hasattr(player, 'location'):
        player.location = room
    elif hasattr(player, 'room'):
        player.room = room
    else:
        player.current_room = room

def get_player_inventory(player):
    """Safely retrieves inventory list from Player object"""
    if hasattr(player, 'inventory'):
        return player.inventory
    elif hasattr(player, 'items'):
        return player.items
    elif hasattr(player, 'bag'):
        return player.bag
    else:
        player.inventory = []
        return player.inventory

def save_game(player, rooms_dict):
    """Saves current player state to a JSON file"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(base_dir, f"{player.name.lower()}_save.json")
    
    current_room = get_player_room(player)
    room_name = current_room.name if current_room else "Hall"
    inventory_list = get_player_inventory(player)
    
    save_data = {
        "player_name": player.name,
        "current_room": room_name,
        "inventory": [item.name for item in inventory_list]
    }
    
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(save_data, file, indent=4)
        print(f"\n✅ Game saved successfully as '{player.name.lower()}_save.json'!")
    except Exception as e:
        print(f"\n❌ Error while saving game: {e}")

def load_game(player_name, rooms_dict):
    """Loads saved player state if it exists"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(base_dir, f"{player_name.lower()}_save.json")
    
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                
            start_room = rooms_dict.get(data["current_room"], list(rooms_dict.values())[0])
            player = Player(data["player_name"], start_room)
            set_player_room(player, start_room)
            
            inventory_list = get_player_inventory(player)
            for item_name in data.get("inventory", []):
                inventory_list.append(Item(item_name, "Loaded item"))
                
            print(f"\n🎮 Welcome back, {player.name}! Game loaded from your last saved state.")
            return player
        except Exception as e:
            print(f"\n❌ Error loading save file: {e}")
            return None
    return None

def main():
    # 1. Display Intro & Instructions from text files
    print(load_text_file("intro.txt"))
    print(load_text_file("instructions.txt"))
    
    # Setup Rooms and Items
    hall = Room("Hall", "A large dimly lit hall.")
    armory = Room("Armory", "A room filled with weapons and shields.")
    vault = Room("Vault", "A heavily fortified treasure room.")
    
    sword = Item("Sword", "A sharp steel blade.")
    key = Item("Key", "A rusty iron key.")
    
    hall.item = sword
    armory.item = key
    
    rooms = {
        "Hall": hall,
        "Armory": armory,
        "Vault": vault
    }

    # Set Exits
    hall.exits = {"east": armory}
    armory.exits = {"west": hall, "north": vault}
    vault.exits = {"south": armory}

    # 2. Get Player Name and check for existing save file
    hero_name = input("Enter your hero's name: ").strip()
    
    player = load_game(hero_name, rooms)
    if not player:
        player = Player(hero_name, hall)
        set_player_room(player, hall)
        print(f"\n✨ Welcome, {player.name}! A new game has started.")

    # 3. Main Game Loop
    while True:
        current_room = get_player_room(player)
        inventory_list = get_player_inventory(player)
        
        print("\n" + "="*30)
        print(f"Player: {player.name}")
        print(f"Current Location: {current_room.name if current_room else 'Unknown'}")
        
        room_item_name = current_room.item.name if current_room and getattr(current_room, 'item', None) else "None"
        print(f"Room Item: {room_item_name}")
        print(f"Inventory: {[item.name for item in inventory_list]}")
        print("="*30)
        
        print("\nActions:")
        print("1. Move")
        print("2. Collect Item")
        print("3. Save Game")
        print("4. Quit Game")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            direction = input("Enter direction to move (e.g., east, west, north, south): ").strip().lower()
            if current_room and direction in current_room.exits:
                new_room = current_room.exits[direction]
                set_player_room(player, new_room)
                print(f"You moved to the {new_room.name}.")
            else:
                print("There is no exit in that direction!")
        
        elif choice == "2":
            if current_room and getattr(current_room, 'item', None):
                item = current_room.item
                inventory_list.append(item)
                current_room.item = None
                print(f"You picked up the {item.name}!")
            else:
                print("There are no items to collect in this room.")
                
        elif choice == "3":
            save_game(player, rooms)
            
        elif choice == "4":
            save_opt = input("Do you want to save before quitting? (y/n): ").strip().lower()
            if save_opt == 'y':
                save_game(player, rooms)
            print("\nThanks for playing! Goodbye.")
            break
        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    main()