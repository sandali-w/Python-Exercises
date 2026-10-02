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