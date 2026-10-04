class Room:
    def __init__(self, name: str, item=None):
        self.name = name
        self.item = item  # Can contain 0 or 1 Item

    def __str__(self):
        item_info = f" containing {self.item.name}" if self.item else " with no items"
        return f"{self.name}{item_info}"