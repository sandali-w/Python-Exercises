# Module 12

## item.py

class Item:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"

## player.py

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

## room.py

class Room:
    def __init__(self, name: str, item=None):
        self.name = name
        self.item = item  # Can contain 0 or 1 Item

    def __str__(self):
        item_info = f" containing {self.item.name}" if self.item else " with no items"
        return f"{self.name}{item_info}"

## main.py

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