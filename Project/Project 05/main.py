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