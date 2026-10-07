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

========== HOW TO PLAY ==========

COMMANDS:
map         - Show world map (need Fire Essence first)
explore     - Explore current door challenge
collect     - Collect item from room
move        - Move to next door (type door number 1-6)
shop        - Trade items (only at Door 4 Earth Village)
items       - Show your items
status      - Show coins and status
save        - Save game
load        - Load game
instructions- Show this help
lopeta      - Quit game

HOW TO WIN:
Door 1 FIRE: Type 'run' fast in 3 seconds to get Fire Essence + Map
Door 2 WATER: Answer riddle (needle) to get Water Pearl + Torch
Door 3 WIND: Choose right path to get Wind Feather
Door 4 EARTH: Trade Torch + 10 coins for Earth Stone, then 15 coins for Light Crystal
Door 5 LIGHT: Guard checks if you have 4 elements + 10 coins
Door 6 DARKNESS: Answer 3 boss questions to win Darkness Crown!

### intro.txt

Welcome to THE LOST ARTIFACT - 6 ELEMENTS EDITION!

Long ago, 6 elemental spirits guarded the world.
Fire, Water, Wind, Earth, Light, and Darkness.

The Darkness Crown was stolen by Shadow King!
You are the chosen hero who must collect all 6 elements
and defeat the Shadow King in Door 6.

Your journey starts now!

### main.py

import os
import random
import time
from game.item import Item
from game.room import Room
from game.player import Player

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FILE = os.path.join(BASE_DIR, "savegame.txt")

def show_map(current_room_name, has_map):
    if not has_map:
        print("\nYou need Fire Essence to get map! Explore Door 1!")
        return
    print("\n========== 6 ELEMENTS MAP ==========")
    print("Door 1 - FIRE INFERNO (Speed Challenge) 🔥")
    print(" |")
    print("Door 2 - WATER ABYSS (Oxygen Puzzle) 🌊")
    print(" |")
    print("Door 3 - WIND STORM (Maze Choice) 🌪️")
    print(" |")
    print("Door 4 - EARTH VILLAGE (Trading) 🏔️")
    print(" |")
    print("Door 5 - LIGHT LIBRARY (Guard Check) ✨")
    print(" |")
    print("Door 6 - DARKNESS VAULT (Boss Fight) 👑")
    print("====================================")
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
    print("\nGame saved!")

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
        new_player = Player(name, age, rooms[room_number - 1])
        new_player.coins = coins
        new_player.has_map = has_map
        for item_name in saved_items:
            if item_name in items:
                new_player.items.append(items[item_name])
        print("\nGame loaded!")
        return new_player
    except:
        print("\nSave file damaged.")
        return player

def create_rooms():
    fire = Item("Fire Essence", 1)
    pearl = Item("Water Pearl", 1)
    feather = Item("Wind Feather", 1)
    earth = Item("Earth Stone", 1)
    crystal = Item("Light Crystal", 2)
    torch = Item("Torch", 1)
    crown = Item("Darkness Crown", 1)

    rooms = [
        Room("Door 1: FIRE INFERNO", "Lava everywhere! Floor is burning!", 1, fire),
        Room("Door 2: WATER ABYSS", "You are underwater! Bubbles everywhere!", 2, pearl),
        Room("Door 3: WIND STORM", "Tornado! Two paths: left and right!", 3, feather),
        Room("Door 4: EARTH VILLAGE", "Villagers: We want Torch, not coins!", 4),
        Room("Door 5: LIGHT LIBRARY", "Light Guardian protects the secret!", 5, crystal),
        Room("Door 6: DARKNESS VAULT", "Shadow King sits on throne!", 6)
    ]

    item_dict = {
        "Fire Essence": fire,
        "Water Pearl": pearl,
        "Wind Feather": feather,
        "Earth Stone": earth,
        "Light Crystal": crystal,
        "Torch": torch,
        "Darkness Crown": crown
    }
    return rooms, item_dict

def explore_room(player):
    room = player.location
    print(f"\n>>> You explore {room.name}...")
    print(room.description)

    # DOOR 1 - FIRE - SPEED CHALLENGE
    if room.number == 1:
        if not player.has_map:
            print("\n🔥 Lava coming! Type 'run' in 3 seconds!")
            start = time.time()
            ans = input("Type now: ").lower()
            elapsed = time.time() - start
            if ans == "run" and elapsed < 3:
                player.has_map = True
                player.coins += 10
                print(f"Fast! You escaped in {elapsed:.1f}s! Got Map + Fire Essence + 10 coins!")
            else:
                print("Too slow! You burned a little but still got Map. -2 coins")
                player.coins = max(0, player.coins - 2)
                player.has_map = True
        else:
            print("\nFire is calm now.")

    # DOOR 2 - WATER - PUZZLE
    elif room.number == 2:
        if not has_item(player, "Water Pearl"):
            print("\n🌊 Oxygen low! Answer to get pearl: What has an eye but cannot see? (needle)")
            ans = input("Answer: ").lower()
            if "needle" in ans:
                print("Correct! You got Water Pearl + Torch!")
                player.coins += 10
                if not has_item(player, "Torch"):
                    from game.item import Item
                    player.items.append(Item("Torch", 1))
            else:
                print("Wrong! You lost 5 coins for air!")
                player.coins = max(0, player.coins - 5)
        else:
            print("\nWater is peaceful.")

    # DOOR 3 - WIND - MAZE CHOICE
    elif room.number == 3:
        if not has_item(player, "Wind Feather"):
            print("\n🌪️ Left path has monster, Right path has treasure! Choose: left / right")
            choice = input("Your choice: ").lower()
            if choice == "right":
                print("Smart! You found Wind Feather + 15 coins!")
                player.coins += 15
            elif choice == "left":
                print("Monster! You fight and win but lose 5 coins, still get feather!")
                player.coins = max(0, player.coins - 5)
            else:
                print("Wind blew you to right anyway! Lucky!")
                player.coins += 5
        else:
            print("\nWind stopped.")

    # DOOR 4 - EARTH - TRADING NOT SHOP
    elif room.number == 4:
        print("\n🏔️ Villager: I will give Earth Stone + Light Crystal if you give Torch + 10 coins")
        print("Use 'shop' command to trade!")

    # DOOR 5 - LIGHT - GUARD CHECK IDEA 3
    elif room.number == 5:
        print("\n✨ LIGHT GUARDIAN: I check 4 elements!")
        print(f"You have coins: {player.coins}")
        need = ["Fire Essence", "Water Pearl", "Wind Feather", "Earth Stone"]
        missing = [x for x in need if not has_item(player, x)]
        if missing:
            print(f"Guardian: Missing {', '.join(missing)}! Go back!")
            return False
        if player.coins < 10:
            print("Guardian: Need 10 coins to be worthy!")
            return False
        if not has_item(player, "Light Crystal"):
            print("Guardian: You are worthy! Take Light Crystal!")
        else:
            print("Library quiet.")

    # DOOR 6 - DARKNESS - BOSS FIGHT
    elif room.number == 6:
        print("\n👑 SHADOW KING: Answer my 3 questions!")
        if not (has_item(player, "Earth Stone") and has_item(player, "Light Crystal")):
            print("King: You need Earth Stone + Light Crystal! Go back!")
            return False

        q1 = input("Q1: What is 2+2? ").strip()
        q2 = input("Q2: What color is sky? ").lower()
        q3 = input("Q3: Say 'I am worthy': ").lower()

        if q1 == "4" and "blue" in q2 and "worthy" in q3:
            print("\n****************************************")
            print(" SHADOW KING DEFEATED!")
            print(" You got Darkness Crown!")
            print(" ★ YOU MASTERED 6 ELEMENTS! YOU WIN! ★")
            print("****************************************")
            return True
        else:
            print("\nKing: Wrong answers! Try again! You lost 3 coins!")
            player.coins = max(0, player.coins - 3)

    return False

def move_player(player, rooms):
    try:
        destination = int(input("Enter door number (1-6): "))
    except ValueError:
        print("\nEnter valid number.")
        return
    if destination < 1 or destination > 6:
        print("\nInvalid door.")
        return
    current = player.location.number
    if destination!= current + 1:
        print("\nMust go in order! Cannot skip or go back!")
        return

    required_keys = {2: "Fire Essence", 3: "Water Pearl", 4: "Wind Feather", 5: "Earth Stone", 6: "Light Crystal"}

    if destination in required_keys:
        if not has_item(player, required_keys[destination]):
            print(f"\nNeed {required_keys[destination]} to enter Door {destination}")
            return
    player.move(rooms[destination - 1])
    print(f"\nMoved to {player.location.name}")

def shop(player, earth, crystal):
    if player.location.number!= 4:
        print("\nTrading only at Door 4 Earth Village!")
        return False
    while True:
        print("\n======== EARTH VILLAGE TRADE ========")
        print("1. Trade Torch + 10 coins -> Earth Stone")
        print("2. Trade Earth Stone -> Light Crystal (15 coins)")
        print("3. Exit village")
        print("======================================")
        choice = input("Choose: ")
        if choice == "1":
            if has_item(player, "Earth Stone"):
                print("\nAlready have Earth Stone!")
            elif has_item(player, "Torch") and player.coins >= 10:
                player.coins -= 10
                # remove torch
                player.items = [i for i in player.items if i.name!= "Torch"]
                player.items.append(earth)
                print(f"\nTraded! Got Earth Stone! Coins left: {player.coins}")
            else:
                print(f"\nNeed Torch + 10 coins. You have coins {player.coins}, has Torch? {has_item(player, 'Torch')}")
        elif choice == "2":
            if not has_item(player, "Earth Stone"):
                print("\nNeed Earth Stone first! Do trade 1")
            elif has_item(player, "Light Crystal"):
                print("\nAlready have Light Crystal!")
            elif player.coins >= 15:
                player.coins -= 15
                player.items.append(crystal)
                print(f"\nGot Light Crystal! Now go to Door 5! Coins: {player.coins}")
                return False
            else:
                print(f"\nNeed 15 coins. You have {player.coins}")
        elif choice == "3":
            print("\nLeft village.")
            return False
        else:
            print("\nInvalid choice.")

def main():
    print("\n===================================================")
    print(" THE LOST ARTIFACT - 6 ELEMENTS EDITION 🔥🌊🌪️🏔️✨👑")
    print("===================================================")
    print(read_file("intro.txt"))
    name = input("\nEnter your name: ")
    if not name:
        name = "Hero"
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please enter valid age.")
    if age < 12:
        print("\nMust be 12+")
        return
    print("\n")
    print(read_file("instructions.txt"))
    rooms, items = create_rooms()
    player = Player(name, age, rooms[0])

    while True:
        print("\n-------------------------------------------")
        print("Location:", player.location.name)
        print("Coins:", player.coins)
        print("-------------------------------------------")
        command = input("Enter command: ").lower()
        if command == "map":
            show_map(player.location.name, player.has_map)
        elif command == "explore":
            won = explore_room(player)
            if won:
                print("\nGAME ENDS - YOU MASTERED ALL ELEMENTS!")
                break
        elif command == "move":
            move_player(player, rooms)
        elif command == "collect":
            player.collect_item()
        elif command == "shop":
            shop(player, items["Earth Stone"], items["Light Crystal"])
        elif command == "items":
            player.show_inventory()
        elif command == "status":
            player.show_status()
        elif command == "save":
            save_game(player)
        elif command == "load":
            player = load_game(player, rooms, items)
        elif command == "instructions":
            print(read_file("instructions.txt"))
        elif command == "lopeta":
            print("\nThanks for playing!")
            break
        else:
            print("\nUnknown command. Type 'instructions'.")

if __name__ == "__main__":
    main()