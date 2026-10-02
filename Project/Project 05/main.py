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