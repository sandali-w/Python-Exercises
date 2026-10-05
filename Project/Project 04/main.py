import os
from modules.item import Item
from modules.room import Room
from module.player import Player


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