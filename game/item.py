class Item:
    def __init__(self, name, description, can_pick_up=True):
        self.name = name
        self.description = description
        self.can_pick_up = can_pick_up

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"{self.name} : {self.description}"

    def __lt__(self, other):
        return self.name < other.name
