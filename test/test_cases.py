import unittest
from game.location import Location
from game.item import Item
from game.map import Map
from game.backpack import BackPack


class MyTestClass(unittest.TestCase):

    def setUp(self) -> None:
        # create backpack object
        self.backpack = BackPack([])
        # create a map object
        self.map = Map(size=(3, 3))
        # create test items
        self.baseball_bat = Item('baseball bat', 'a baseball bat that is used as a weapon')
        self.razor = Item('a razor', 'a razor used to shave')
        self.item3 = Item('item 3', 'item 3')
        self.item4 = Item('item 4', 'item 4')
        self.item5 = Item('item 5', 'item 5')
        # create a test location
        self.location1 = Location(
            id=1,
            name='bedroom',
            description='the bedroom',
            prompts=['prompt one', 'prompt two'],
            items=[self.razor, self.baseball_bat],
            is_dangerous=False
        )
        self.location2 = Location(
            id=2,
            name='bathroom',
            description='the bathroom',
            prompts=['prompt one', 'prompt two'],
            items=[self.razor, self.baseball_bat],
            is_dangerous=False
        )
        self.location3 = Location(
            id=2,
            name='bathroom',
            description='the bathroom',
            prompts=['prompt one', 'prompt two'],
            items=[self.razor, self.baseball_bat],
            is_dangerous=False
        )

    def test_adding_location_to_map(self):
        self.map.add_location(0, 0, self.location1)
        self.map.add_location(1, 1, self.location2)
        self.map.add_location(2, 2, self.location3)

        self.assertEqual(self.map.grid[0][0], self.location1)
        self.assertEqual(self.map.grid[1][1], self.location2)
        self.assertEqual(self.map.grid[2][2], self.location3)

    def test_adding_items_to_backpack(self):
        self.backpack.add(self.baseball_bat)
        self.backpack.add(self.razor)

        self.assertEqual(len(self.backpack), 2)

    def test_found_item_in_backpack_with_binary_search(self):
        self.backpack.add(self.baseball_bat)
        self.backpack.add(self.razor)
        self.backpack.add(self.item3)
        self.backpack.add(self.item4)

        self.assertEqual(self.backpack.found_in_backpack(self.item3.name), self.item3.name)
        self.assertEqual(self.backpack.found_in_backpack(self.item5.name), -1)

    def test_in_backpack(self):
        self.backpack.add(self.baseball_bat)
        self.backpack.add(self.razor)
        self.backpack.add(self.item3)
        self.backpack.add(self.item4)

        self.assertTrue(self.backpack.in_backpack(self.razor.name))
        self.assertFalse(self.backpack.in_backpack(self.item5.name))


if __name__ == '__main__':
    unittest.main()
