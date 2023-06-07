from item import Item


class BackPack:
    """
    BackPack Class
    ToDo: [X] Instantiate backpack
    ToDo: [X] Add Item
    ToDo: [X] Remove Item
    ToDo: [X] List Items
    ToDo: [X] Count items
    ToDo: [X] in backpack (Search for Item - Student to do)
    ToDo: [X] Sort Items
    """

    def __init__(self, items):
        self._backpack: list = []
        if items is None:
            items = []
        for item in items:
            self._backpack.append(item)
        self.sort()

    def sort(self):
        self._backpack.sort()

    def __len__(self):
        return len(self._backpack)

    def list(self):
        for item in self._backpack:
            print(item.name)

    def add(self, item):
        if item is not None:
            self._backpack.append(item)
            self.sort()

    def __getitem__(self, index):
        return self._backpack[index]

    def in_backpack(self, item_name):
        """
        Complete this method using a binary search
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

