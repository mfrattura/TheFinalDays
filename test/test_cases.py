import unittest
from game.location import Location
from game.player import Player
from game.backpack import BackPack


class MyTestClass(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def setup(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
