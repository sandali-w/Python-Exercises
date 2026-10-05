# My awesome game: The Lost Artifact

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
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} (Weight: {self.weight} kg)"

### room.py

class Room:
    def __init__(self, name, description, number, item=None):
        self.name = name
        self.description = description
        self.number = number
        self.item = item

    def __str__(self):
        return f"{self.name}: {self.description}"

### player.py

class Player:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        self.coins = 0
        self.items = []
        self.has_map = False

    def move(self, room):
        self.location = room
        print(f"\nYou moved to: {room.name}")
        print(room.description)

    def collect_item(self):
        if self.location.item is None:
            print("\nThere is no item to collect here.")
            return

        item = self.location.item

        if any(existing.name == item.name for existing in self.items):
            print(f"\nYou already have the {item.name}.")
            return

        self.items.append(item)
        print(f"\nYou collected: {item.name}")

    def show_inventory(self):
        print("\n--- INVENTORY ---")

        if not self.items:
            print("Your inventory is empty.")
            return

        for item in self.items:
            print(f"- {item.name} ({item.weight} kg)")

    def show_status(self):
        print("\n--- PLAYER STATUS ---")
        print(f"Name     : {self.name}")
        print(f"Age      : {self.age}")
        print(f"Location : {self.location.name}")
        print(f"Coins    : {self.coins}")
        print(f"Map      : {'Yes' if self.has_map else 'No'}")
        print(f"Items    : {len(self.items)}")

### main.py

import os
from game.item import Item
from game.room import Room
from game.player import Player


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FILE = os.path.join(BASE_DIR, "savegame.txt")


def show_map(current_room_name, has_map):
    if not has_map:
        print("\nYou do not have the map yet.")
        print("Explore Door 1 first.")
        return

    print("\n========== WORLD MAP ==========")
    print("Door 1 - The Forest Gate")
    print("   |")
    print("Door 2 - The Dark Cave")
    print("   |")
    print("Door 3 - The Sunken Ruins")
    print("   |")
    print("Door 4 - The Ancient Shop")
    print("   |")
    print("Door 5 - The Sacred Vault")
    print("===============================")
    print("Current location:", current_room_name)


def read_file(filepath):
    file_path = os.path.join(BASE_DIR, filepath)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"File not found: {filepath}"


def has_item(player, item_name):
    return any(item.name == item_name for item in player.items)


def save_game(player):
    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        file.write(f"{player.name}\n")
        file.write(f"{player.age}\n")
        file.write(f"{player.location.number}\n")
        file.write(f"{player.coins}\n")
        file.write(f"{int(player.has_map)}\n")
        file.write(",".join(item.name for item in player.items))

    print("\nGame saved successfully!")


def load_game(player, rooms, items):
    if not os.path.exists(SAVE_FILE):
        print("\nNo saved game found.")
        return player

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            lines = file.read().splitlines()

        name = lines[0]
        age = int(lines[1])
        room_number = int(lines[2])
        coins = int(lines[3])
        has_map = bool(int(lines[4]))

        saved_items = []

        if len(lines) > 5 and lines[5]:
            saved_items = lines[5].split(",")

        new_player = Player(
            name,
            age,
            rooms[room_number - 1]
        )

        new_player.coins = coins
        new_player.has_map = has_map

        for item_name in saved_items:
            if item_name in items:
                new_player.items.append(items[item_name])

        print("\nGame loaded successfully!")

        return new_player

    except (IndexError, ValueError, KeyError):
        print("\nSave file is damaged or invalid.")
        return player


def create_rooms():

    green_key = Item("Green Key", 1)
    silver_key = Item("Silver Key", 1)
    blue_key = Item("Blue Key", 1)
    gold_key = Item("Gold Key", 1)
    crystal = Item("Crystal of Light", 2)

    rooms = [

        Room(
            "Door 1: The Forest Gate",
            "A mysterious forest gate stands before you.",
            1,
            green_key
        ),

        Room(
            "Door 2: The Dark Cave",
            "A dark cave filled with strange sounds.",
            2,
            silver_key
        ),

        Room(
            "Door 3: The Sunken Ruins",
            "Ancient ruins lie beneath the water.",
            3,
            blue_key
        ),

        Room(
            "Door 4: The Ancient Shop",
            "An ancient shop offers special items for coins.",
            4
        ),

        Room(
            "Door 5: The Sacred Vault",
            "A huge golden door protects the final chamber.",
            5
        )
    ]

    item_dict = {
        "Green Key": green_key,
        "Silver Key": silver_key,
        "Blue Key": blue_key,
        "Gold Key": gold_key,
        "Crystal of Light": crystal
    }

    return rooms, item_dict


def explore_room(player):

    room = player.location

    print(f"\nYou explore {room.name}...")
    print(room.description)

    # Door 1
    if room.number == 1:

        if not player.has_map:
            player.has_map = True
            print("\nYou found the World Map!")

        else:
            print("\nYou already found the map.")

    # Door 2
    elif room.number == 2:

        if not has_item(player, "Silver Key"):
            player.coins += 10

            print("\nYou found 10 coins!")
            print("Total coins:", player.coins)

        else:
            print("\nYou already explored this area.")

    # Door 3
    elif room.number == 3:

        if not has_item(player, "Blue Key"):
            player.coins += 10

            print("\nYou found 10 coins!")
            print("Total coins:", player.coins)

        else:
            print("\nYou already explored this area.")

    # Door 4
    elif room.number == 4:

        print("\nYou are at the Ancient Shop.")
        print("Use the 'shop' command to buy items.")

    # Door 5
    elif room.number == 5:

        if (
            has_item(player, "Gold Key")
            and has_item(player, "Crystal of Light")
        ):

            print("\n")
            print("****************************************")
            print("          SACRED VAULT OPENED!")
            print("****************************************")

            print("The golden door slowly opens...")
            print("You enter the final chamber.")

            print("")
            print("        LOST ARTIFACT FOUND!")
            print("")

            print("        ★ FINAL WIN ★")
            print("")

            print("You completed the adventure!")

            print("****************************************")

            return True

        else:

            print("\nThe Sacred Vault is locked.")

            if not has_item(player, "Gold Key"):
                print("You need the Gold Key.")

            if not has_item(player, "Crystal of Light"):
                print("You need the Crystal of Light.")

    return False


def move_player(player, rooms):

    try:
        destination = int(
            input("Enter door number (1-5): ")
        )

    except ValueError:

        print("\nPlease enter a valid number.")
        return

    if destination < 1 or destination > 5:

        print("\nInvalid door number.")
        return

    current = player.location.number

    if destination != current + 1:

        if destination <= current:
            print("\nYou cannot go backwards.")

        else:
            print("\nYou must complete the doors in order.")

        return

    required_keys = {
        2: "Green Key",
        3: "Silver Key",
        4: "Blue Key",
        5: "Gold Key"
    }

    if destination in required_keys:

        required_key = required_keys[destination]

        if not has_item(player, required_key):

            print(
                f"\nYou need the {required_key} "
                f"to enter Door {destination}."
            )

            return

    player.move(rooms[destination - 1])


def shop(player, gold_key, crystal):

    if player.location.number != 4:

        print("\nThe shop is only available at Door 4.")
        return False

    while True:

        print("\n")
        print("================================")
        print("         ANCIENT SHOP")
        print("================================")
        print("1. Gold Key          - 5 coins")
        print("2. Crystal of Light  - 15 coins")
        print("3. Exit")
        print("================================")

        choice = input("Choose an item: ")

        # Buy Gold Key
        if choice == "1":

            if has_item(player, "Gold Key"):

                print("\nYou already have the Gold Key.")

            elif player.coins >= 5:

                player.coins -= 5
                player.items.append(gold_key)

                print("\nYou bought the Gold Key!")
                print("5 coins were used.")
                print("Remaining coins:", player.coins)

            else:

                print("\nYou need 5 coins to buy the Gold Key.")
                print("Your coins:", player.coins)

        # Buy Crystal of Light
        elif choice == "2":

            if not has_item(player, "Gold Key"):

                print("\nYou need the Gold Key first!")

            elif has_item(player, "Crystal of Light"):

                print("\nYou already have the Crystal of Light.")

            elif player.coins >= 15:

                player.coins -= 15
                player.items.append(crystal)

                print("\nYou bought the Crystal of Light!")
                print("15 coins were used.")
                print("Remaining coins:", player.coins)

                print("\nNow go to Door 5.")
                print("Open the Sacred Vault to find the Lost Artifact.")

                # Shop closes automatically
                return False

            else:

                print("\nYou need 15 coins to buy the Crystal.")
                print("Your coins:", player.coins)

        # Exit shop
        elif choice == "3":

            print("\nYou left the shop.")
            return False

        else:

            print("\nInvalid choice.")
            print("Please choose 1, 2, or 3.")


def main():

    print("\n")
    print("===================================================")
    print("          THE LOST ARTIFACT ADVENTURE")
    print("===================================================")

    print(read_file("intro.txt"))

    name = input("\nEnter your name: ")

    if not name:
        name = "Hero"

    while True:

        try:
            age = int(
                input("Enter your age: ")
            )

            break

        except ValueError:

            print("Please enter a valid age.")

    if age < 12:

        print("\nSorry, you must be at least 12 years old.")
        return

    print("\n")

    print(read_file("instructions.txt"))

    rooms, items = create_rooms()

    player = Player(
        name,
        age,
        rooms[0]
    )

    while True:

        print("\n")
        print("-------------------------------------------")
        print("Location:", player.location.name)
        print("Coins:", player.coins)
        print("-------------------------------------------")

        command = input("Enter command: ").lower()

        # MAP
        if command == "map":

            show_map(
                player.location.name,
                player.has_map
            )

        # EXPLORE
        elif command == "explore":

            won = explore_room(player)

            if won:

                print("\nGAME ENDS.")
                break

        # MOVE
        elif command == "move":

            move_player(
                player,
                rooms
            )

        # COLLECT
        elif command == "collect":

            player.collect_item()

        # SHOP
        elif command == "shop":

            shop(
                player,
                items["Gold Key"],
                items["Crystal of Light"]
            )

        # INVENTORY
        elif command == "items":

            player.show_inventory()

        # STATUS
        elif command == "status":

            player.show_status()

        # SAVE
        elif command == "save":

            save_game(player)

        # LOAD
        elif command == "load":

            player = load_game(
                player,
                rooms,
                items
            )

        # INSTRUCTIONS
        elif command == "instructions":

            print(
                read_file("instructions.txt")
            )

        # EXIT
        elif command == "lopeta":

            print("\nThanks for playing!")
            break

        else:

            print("\nUnknown command.")
            print(
                "Type 'instructions' "
                "to see the commands."
            )


if __name__ == "__main__":
    main()

## Project 05

### item.py

class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} (Weight: {self.weight} kg)"

### room.py

class Room:
    def __init__(self, name, description, number, item=None):
        self.name = name
        self.description = description
        self.number = number
        self.item = item

    def __str__(self):
        return f"{self.name}: {self.description}"

### player.py

class Player:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        self.coins = 0
        self.items = []
        self.has_map = False

    def move(self, room):
        self.location = room
        print(f"\nYou moved to: {room.name}")
        print(room.description)

    def collect_item(self):
        if self.location.item is None:
            print("\nThere is no item to collect here.")
            return

        item = self.location.item

        if any(existing.name == item.name for existing in self.items):
            print(f"\nYou already have the {item.name}.")
            return

        self.items.append(item)
        print(f"\nYou collected: {item.name}")

    def show_inventory(self):
        print("\n--- INVENTORY ---")

        if not self.items:
            print("Your inventory is empty.")
            return

        for item in self.items:
            print(f"- {item.name} ({item.weight} kg)")

    def show_status(self):
        print("\n--- PLAYER STATUS ---")
        print(f"Name     : {self.name}")
        print(f"Age      : {self.age}")
        print(f"Location : {self.location.name}")
        print(f"Coins    : {self.coins}")
        print(f"Map      : {'Yes' if self.has_map else 'No'}")
        print(f"Items    : {len(self.items)}")

### instructions.txt

========== GAME INSTRUCTIONS ==========

Commands:

map          - Show the world map
explore      - Explore your current room
move         - Move to the next door
collect      - Collect an item
shop         - Buy items at the Ancient Shop
items        - Show your inventory
status       - Show player status
save         - Save your game
load         - Load your saved game
instructions - Show these instructions
lopeta       - Exit the game

Game Goal:

1. Explore Door 1 and collect the Green Key.
2. Go to Door 2 and collect the Silver Key.
3. Go to Door 3 and collect the Blue Key.
4. Go to Door 4 and buy the Gold Key.
5. Buy the Crystal of Light.
6. Go to Door 5.
7. Open the Sacred Vault.
8. Find the Lost Artifact.
9. FINAL WIN!

========================================

### intro.txt

Welcome to The Lost Artifact!

You are a brave adventurer searching for a mysterious lost artifact.

Explore the five doors, collect keys, earn coins,
and find the Crystal of Light.

Your final destination is the Sacred Vault.

Can you find the Lost Artifact?
Good luck, adventurer!

### main.py

import os
from game.item import Item
from game.room import Room
from game.player import Player


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FILE = os.path.join(BASE_DIR, "savegame.txt")


def show_map(current_room_name, has_map):
    if not has_map:
        print("\nYou do not have the map yet.")
        print("Explore Door 1 first.")
        return

    print("\n========== WORLD MAP ==========")
    print("Door 1 - The Forest Gate")
    print("   |")
    print("Door 2 - The Dark Cave")
    print("   |")
    print("Door 3 - The Sunken Ruins")
    print("   |")
    print("Door 4 - The Ancient Shop")
    print("   |")
    print("Door 5 - The Sacred Vault")
    print("===============================")
    print("Current location:", current_room_name)


def read_file(filepath):
    file_path = os.path.join(BASE_DIR, filepath)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"File not found: {filepath}"


def has_item(player, item_name):
    return any(item.name == item_name for item in player.items)


def save_game(player):
    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        file.write(f"{player.name}\n")
        file.write(f"{player.age}\n")
        file.write(f"{player.location.number}\n")
        file.write(f"{player.coins}\n")
        file.write(f"{int(player.has_map)}\n")
        file.write(",".join(item.name for item in player.items))

    print("\nGame saved successfully!")


def load_game(player, rooms, items):
    if not os.path.exists(SAVE_FILE):
        print("\nNo saved game found.")
        return player

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            lines = file.read().splitlines()

        name = lines[0]
        age = int(lines[1])
        room_number = int(lines[2])
        coins = int(lines[3])
        has_map = bool(int(lines[4]))

        saved_items = []

        if len(lines) > 5 and lines[5]:
            saved_items = lines[5].split(",")

        new_player = Player(
            name,
            age,
            rooms[room_number - 1]
        )

        new_player.coins = coins
        new_player.has_map = has_map

        for item_name in saved_items:
            if item_name in items:
                new_player.items.append(items[item_name])

        print("\nGame loaded successfully!")

        return new_player

    except (IndexError, ValueError, KeyError):
        print("\nSave file is damaged or invalid.")
        return player


def create_rooms():

    green_key = Item("Green Key", 1)
    silver_key = Item("Silver Key", 1)
    blue_key = Item("Blue Key", 1)
    gold_key = Item("Gold Key", 1)
    crystal = Item("Crystal of Light", 2)

    rooms = [

        Room(
            "Door 1: The Forest Gate",
            "A mysterious forest gate stands before you.",
            1,
            green_key
        ),

        Room(
            "Door 2: The Dark Cave",
            "A dark cave filled with strange sounds.",
            2,
            silver_key
        ),

        Room(
            "Door 3: The Sunken Ruins",
            "Ancient ruins lie beneath the water.",
            3,
            blue_key
        ),

        Room(
            "Door 4: The Ancient Shop",
            "An ancient shop offers special items for coins.",
            4
        ),

        Room(
            "Door 5: The Sacred Vault",
            "A huge golden door protects the final chamber.",
            5
        )
    ]

    item_dict = {
        "Green Key": green_key,
        "Silver Key": silver_key,
        "Blue Key": blue_key,
        "Gold Key": gold_key,
        "Crystal of Light": crystal
    }

    return rooms, item_dict


def explore_room(player):

    room = player.location

    print(f"\nYou explore {room.name}...")
    print(room.description)

    # Door 1
    if room.number == 1:

        if not player.has_map:
            player.has_map = True
            print("\nYou found the World Map!")

        else:
            print("\nYou already found the map.")

    # Door 2
    elif room.number == 2:

        if not has_item(player, "Silver Key"):
            player.coins += 10

            print("\nYou found 10 coins!")
            print("Total coins:", player.coins)

        else:
            print("\nYou already explored this area.")

    # Door 3
    elif room.number == 3:

        if not has_item(player, "Blue Key"):
            player.coins += 10

            print("\nYou found 10 coins!")
            print("Total coins:", player.coins)

        else:
            print("\nYou already explored this area.")

    # Door 4
    elif room.number == 4:

        print("\nYou are at the Ancient Shop.")
        print("Use the 'shop' command to buy items.")

    # Door 5
    elif room.number == 5:

        if (
            has_item(player, "Gold Key")
            and has_item(player, "Crystal of Light")
        ):

            print("\n")
            print("****************************************")
            print("          SACRED VAULT OPENED!")
            print("****************************************")

            print("The golden door slowly opens...")
            print("You enter the final chamber.")

            print("")
            print("        LOST ARTIFACT FOUND!")
            print("")

            print("        ★ FINAL WIN ★")
            print("")

            print("You completed the adventure!")

            print("****************************************")

            return True

        else:

            print("\nThe Sacred Vault is locked.")

            if not has_item(player, "Gold Key"):
                print("You need the Gold Key.")

            if not has_item(player, "Crystal of Light"):
                print("You need the Crystal of Light.")

    return False


def move_player(player, rooms):

    try:
        destination = int(
            input("Enter door number (1-5): ")
        )

    except ValueError:

        print("\nPlease enter a valid number.")
        return

    if destination < 1 or destination > 5:

        print("\nInvalid door number.")
        return

    current = player.location.number

    if destination != current + 1:

        if destination <= current:
            print("\nYou cannot go backwards.")

        else:
            print("\nYou must complete the doors in order.")

        return

    required_keys = {
        2: "Green Key",
        3: "Silver Key",
        4: "Blue Key",
        5: "Gold Key"
    }

    if destination in required_keys:

        required_key = required_keys[destination]

        if not has_item(player, required_key):

            print(
                f"\nYou need the {required_key} "
                f"to enter Door {destination}."
            )

            return

    player.move(rooms[destination - 1])


def shop(player, gold_key, crystal):

    if player.location.number != 4:

        print("\nThe shop is only available at Door 4.")
        return False

    while True:

        print("\n")
        print("================================")
        print("         ANCIENT SHOP")
        print("================================")
        print("1. Gold Key          - 5 coins")
        print("2. Crystal of Light  - 15 coins")
        print("3. Exit")
        print("================================")

        choice = input("Choose an item: ")

        # Buy Gold Key
        if choice == "1":

            if has_item(player, "Gold Key"):

                print("\nYou already have the Gold Key.")

            elif player.coins >= 5:

                player.coins -= 5
                player.items.append(gold_key)

                print("\nYou bought the Gold Key!")
                print("5 coins were used.")
                print("Remaining coins:", player.coins)

            else:

                print("\nYou need 5 coins to buy the Gold Key.")
                print("Your coins:", player.coins)

        # Buy Crystal of Light
        elif choice == "2":

            if not has_item(player, "Gold Key"):

                print("\nYou need the Gold Key first!")

            elif has_item(player, "Crystal of Light"):

                print("\nYou already have the Crystal of Light.")

            elif player.coins >= 15:

                player.coins -= 15
                player.items.append(crystal)

                print("\nYou bought the Crystal of Light!")
                print("15 coins were used.")
                print("Remaining coins:", player.coins)

                print("\nNow go to Door 5.")
                print("Open the Sacred Vault to find the Lost Artifact.")

                # Shop closes automatically
                return False

            else:

                print("\nYou need 15 coins to buy the Crystal.")
                print("Your coins:", player.coins)

        # Exit shop
        elif choice == "3":

            print("\nYou left the shop.")
            return False

        else:

            print("\nInvalid choice.")
            print("Please choose 1, 2, or 3.")


def main():

    print("\n")
    print("===================================================")
    print("          THE LOST ARTIFACT ADVENTURE")
    print("===================================================")

    print(read_file("intro.txt"))

    name = input("\nEnter your name: ")

    if not name:
        name = "Hero"

    while True:

        try:
            age = int(
                input("Enter your age: ")
            )

            break

        except ValueError:

            print("Please enter a valid age.")

    if age < 12:

        print("\nSorry, you must be at least 12 years old.")
        return

    print("\n")

    print(read_file("instructions.txt"))

    rooms, items = create_rooms()

    player = Player(
        name,
        age,
        rooms[0]
    )

    while True:

        print("\n")
        print("-------------------------------------------")
        print("Location:", player.location.name)
        print("Coins:", player.coins)
        print("-------------------------------------------")

        command = input("Enter command: ").lower()

        # MAP
        if command == "map":

            show_map(
                player.location.name,
                player.has_map
            )

        # EXPLORE
        elif command == "explore":

            won = explore_room(player)

            if won:

                print("\nGAME ENDS.")
                break

        # MOVE
        elif command == "move":

            move_player(
                player,
                rooms
            )

        # COLLECT
        elif command == "collect":

            player.collect_item()

        # SHOP
        elif command == "shop":

            shop(
                player,
                items["Gold Key"],
                items["Crystal of Light"]
            )

        # INVENTORY
        elif command == "items":

            player.show_inventory()

        # STATUS
        elif command == "status":

            player.show_status()

        # SAVE
        elif command == "save":

            save_game(player)

        # LOAD
        elif command == "load":

            player = load_game(
                player,
                rooms,
                items
            )

        # INSTRUCTIONS
        elif command == "instructions":

            print(
                read_file("instructions.txt")
            )

        # EXIT
        elif command == "lopeta":

            print("\nThanks for playing!")
            break

        else:

            print("\nUnknown command.")
            print(
                "Type 'instructions' "
                "to see the commands."
            )


if __name__ == "__main__":
    main()