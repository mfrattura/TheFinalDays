from game.backpack import BackPack
from game.game_creator import GameCreator
from game.player import Player
from game.location import Location


class Gameplay:
    def __init__(self):
        self.setup = GameCreator()
        self.game_map = self.setup.setup_game('world.json')
        self.player = None

    def start_game(self):
        self.setup.print_separator()
        self.setup.the_goal()
        self.setup.intro_scene()
        self.setup.print_separator()
        print("Please enter your name:")
        name = input('>')
        self.player = Player(name, self.game_map)
        self.player.backpack = BackPack([])
        print(f'Welcome {self.player.name}')
        self.game_map.serialize()

    @staticmethod
    def show_location_items(location: Location) -> None:
        if location.items:
            print('You see the following items in this location')
            for item in location.items:
                print(f'{item.name} : {item.description}')
        else:
            print('There are no items in this location')

    @staticmethod
    def show_prompt_response(location: Location) -> None:
        if location.prompts:
            for prompt in location.prompts:
                print(f'{prompt.id} : {prompt.prompt}')
                print('Choose the corresponding number to take your action')
                choice = input('>')
                if choice == 1:
                    print(location.prompts[0])
        else:
            print("There are no additional options for this room")

    def show_backpack_items(self):
        if len(self.player.backpack) > 0:
            print(f'you currently have {len(self.player.backpack)} items')
            self.player.backpack.list()
        else:
            print('You have no items in your backpack')

    def pick_up_item(self, location):
        print('Which item would you like to pick up?')
        found_item = input('>').strip().lower()
        for item in location.items:
            if item.name == found_item:
                if item.can_pick_up:
                    self.player.backpack.add(item)
                    print(f'You picked up a {item.name}')
                else:
                    print('You cannot pick the item up')

    def move_player(self):
        print('what direction do you want to go? (n)North, (e)East, (s)South, (w)West')
        direction = input('>').strip().lower()
        if direction == 'q':
            exit()
        self.game_map.move_player(direction)
        self.game_map.serialize()
        print('Your Map:')
        print(self.game_map.display_map())

    def check_for_weapon(self):
        print('What would you like to use:')
        weapon_choice = input('>')
        if self.player.backpack.in_backpack(weapon_choice) == 'baseball bat':
            print('You have a baseball bat, you arm yourself with it')
        else:
            print('you dont have a weapon, you get attacked by a zombie and die')
            exit()


