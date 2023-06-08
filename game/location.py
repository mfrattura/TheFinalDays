from game.item import Item


class Location:
    """
    Class representing a location in the game world
    """
    def __init__(self, id, name, description, prompts=None, items=None, is_dangerous=False):
        """
        Initialize the location object

        :param id:
        :param name:
        :param description:
        :param prompts:
        :param items:
        :param is_dangerous:
        """
        self.id = id
        self.name = name
        self.description = description
        self.prompts = prompts or []
        self.items = list(items) if items else []
        self.is_visited = False
        self.dangerous = is_dangerous

    def __repr__(self):
        """
        Returns a string representation of the location object

        """
        return f'{Location}({self.id}, {self.name}, {self.description}, ' \
               f'{self.prompts}, {self.items})'

    def __str__(self):
        """
        Return a string representation of the location when printed on the game map
        :return:  str: 'X' if the location is visited, otherwise the name of the location.

        """
        return 'X' if self.is_visited else self.name

    def is_dangerous(self):
        """
        Check if the location is dangerous

        :return: bool: whatever bool is in the JSON file
        """
        return self.dangerous


