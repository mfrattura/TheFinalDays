from game.backpack import BackPack


class Player:
    """Class representing the player in the game."""
    def __init__(self, name, _map):
        """
        initializes the player.

        :param name:
        :param _map:
        """
        self.name = name
        self._map = _map
        self.current_location = None
        self.backpack = BackPack([])

    def __repr__(self):
        """
        Return a string representation of the player
        :return: string player
        """
        return f'Person{self.name}'






