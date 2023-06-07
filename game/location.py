from game.item import Item


class Location:
    def __init__(self, id, name, description, prompts=None, items=None):
        self.id = id
        self.name = name
        self.description = description
        self.prompts = prompts or []
        self.items = list(items) if items else []
        if items:
            self.items = list(items)
        else:
            self.items = []
        self.is_visited = False

    def __repr__(self):
        return self.name

    def __str__(self):
        if self.is_visited:
            return 'X'
        else:
            return self.name

    def add_items_to_list(self, name, description, can_pick_up: bool):
        self.items[name][description][can_pick_up] = Item
        self.items.append(Item)

