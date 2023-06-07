import json
from game.location import Location
from game.item import Item


class Map:
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
        with open('../map.txt', 'w') as file:
            for row in self.grid:
                for col in row:
                    if col is None:
                        col = '[  ]'
                    else:
                        col = str(col)  # convert location object to string
                    file.write(col)
                file.write('\n')

    def add_location(self, x: int, y: int, location: Location):
        self.grid[x][y] = location

    def set_visited(self, x, y):
        self.grid[x][y].is_visited = True

    def move_player(self, direction):
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
        return self.player_x, self.player_y

    def display_map(self):
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
        return self.grid[x][y]

    def add_locations_from_file(self, file_name):
        with open(file_name, 'r') as f:
            data = json.load(f)
        locations_data = data['locations']
        for location_data in locations_data:
            location = Location(
                location_data['id'],
                location_data['name'],
                location_data['description'],
                None,
                [Item(*item.values()) for item in location_data['items']
                 if isinstance(item, dict)
                 ]
            )


