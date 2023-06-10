from .item import Item


class BackPack:
    """
    Class representing the backpack used by the player
    """

    def __init__(self, items):
        """
        Initialize the backpack with an empty list of items

        :param items:
        """
        self._backpack: list = []
        if items is None:
            items = []
        for item in items:
            self._backpack.append(item)
        self.sort()

    def sort(self):
        """
        sort the items in the backpack
        :return:
        """
        self._backpack.sort()

    def __len__(self):
        """
        Return the number of items in the backpack.
        :return: int: the number of items in the backpack
        """
        return len(self._backpack)

    def list(self):
        """
        list the items in the backpack

        """
        for item in self._backpack:
            print(item.name)

    def add(self, item):
        """
        Add an item to the backpack.
        :param item:
        """
        if item is not None:
            self._backpack.append(item)
            self.sort()

    def remove(self, item):
        """
        Remove an item from the backpack
        :param item:
        :return:
        """
        if item is not None:
            self._backpack.remove(item)
            self.sort()

    def __getitem__(self, index):
        return self._backpack[index]

    def found_in_backpack(self, item_name):
        """
        finds an item in the backpack using binary search and by object name
        returns -1 or False if not found
        returns position if found
        :param item_name:
        :return: -1 | False | integer
        """
        #
        if len(self) == 0:
            return -1
        left = 0
        right = len(self) - 1
        while left <= right:
            mid = (left + right) // 2
            if item_name == self[mid].name:
                return self[mid].name
            elif self[mid].name < item_name:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def in_backpack(self, bag_item):
        """
        Checks if an item is in the backpack and returns true or false
        :param bag_item:
        :return: bool: if item is in backpack
        """
        for item in self._backpack:
            if item.name == bag_item:
                return True
        return False

