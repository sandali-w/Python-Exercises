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