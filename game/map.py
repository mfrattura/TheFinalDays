import json
from game.location import Location
from game.item import Item


class Map:
    """
    Class representing the game map
    """
    def __init__(self, size=(4, 4)):
        self.x, self.y = size
        self.grid: list[[Location]] = []
        self.player_x = 0  # players x coordinate
        self.player_y = 0  # players y coordinate
        for i in range(self.x):
            self.grid.append([])
            for j in range(self.y):
                self.grid[i].append(None)

    def serialize(self):
        """
        Serialize the map grid and save it to a file.
        :return: map.txt
        """
        file_path = 'map.txt'
        with open(file_path, 'w') as file:
            for row in self.grid:
                for col in row:
                    if col is None:
                        col = '[  ]'
                    else:
                        col = str(col)  # convert location object to string
                    file.write(col)
                file.write('\n')

    def add_location(self, x: int, y: int, location: Location):
        """
        Add a location to the map grid at the specified coordinates
        :param x:
        :param y:
        :param location:
        """
        self.grid[x][y] = location

    def set_visited(self, x, y):
        """
        Set location on map to visited
        :param x:
        :param y:
        :return:
        """
        if self.grid[x][y] is not None:
            self.grid[x][y].is_visited = True
        else:
            return None

    def move_player(self, direction):
        """
        Move the player in a specific direction
        :param direction:
        :return:
        """
        if direction == "w":
            self.player_y -= 1
        elif direction == "s":
            self.player_x += 1
        elif direction == "e":
            self.player_y += 1
        elif direction == "n":
            self.player_x -= 1
        self.set_visited(self.player_x, self.player_y)

    def get_player_location(self):
        """
        Get the current location of the player
        :return: tuple(x, y) coordinates of the player
        """
        return self.player_x, self.player_y

    def display_map(self):
        """
        Displays a string representation of the map grid
        :return: str: String representation of the map grid
        """
        grid_str = ''
        for row in self.grid:
            for co in row:
                if co is None:
                    grid_str += '🧟'
                else:
                    grid_str += str(co) + ' '
            grid_str += '\n'
        return grid_str

    def get_location(self, x, y) -> Location:
        """
        Get the location object at the specific coordinates
        :param x:
        :param y:
        :return: Location object at the coordinates provided by (x, y)
        """
        return self.grid[x][y]

