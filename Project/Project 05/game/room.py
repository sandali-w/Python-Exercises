class Room:
    def __init__(self, name, description, number, item=None):
        self.name = name
        self.description = description
        self.number = number
        self.item = item

    def __str__(self):
        return f"{self.name}: {self.description}"