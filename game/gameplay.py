from game.backpack import BackPack
from game.game_creator import GameCreator
from game.player import Player
from game.location import Location


class Gameplay:
    """
    Class representing the gameplay logic and actions
    """

    def __init__(self):
        self.setup = GameCreator()
        self.game_map = self.setup.setup_game('world.json')
        self.player = None

    def start_game(self):
        """
        Starts the game by initializing the player and displaying the intro scene && Goal
        """
        self.setup.print_separator()
        self.setup.the_goal()
        self.setup.intro_scene()
        self.setup.print_separator()
        print("Please enter your name:")
        name = input('>')
        self.player = Player(name, self.game_map)

        if self.player.backpack is None:
            self.player.backpack = BackPack([])

        print(f'Welcome {self.player.name}')
        self.game_map.serialize()

    @staticmethod
    def show_location_items(location: Location) -> None:
        """
        Displays the items in a given location

        Args: location (Location)
        """
        if location.items:
            print('You see the following items in this location')
            for item in location.items:
                print(f'{item.name} : {item.description}')
        else:
            print('There are no items in this location')

    @staticmethod
    def show_prompt_response(location: Location) -> None:
        """
        Shows the available prompts and corresponding actions for a location

        Args: location (Location)
        """
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
        """Displays items currently in players backpack"""
        if len(self.player.backpack) > 0:
            print(f'you currently have {len(self.player.backpack)} items')
            self.player.backpack.list()
        else:
            print('You have no items in your backpack')

    def pick_up_item(self, location):
        """Allows a player to pick up an item from the available items in a given location

        Arg: location(Location)
        """
        print('Which item would you like to pick up?')
        found_item = input('>').strip().lower()
        for item in location.items:
            if item.name == found_item:
                if item.can_pick_up:
                    self.player.backpack.add(item)
                    print(f'You picked up a {item.name}')
                else:
                    print('You cannot pick the item up')

    def move_player_in_game(self):
        """Prompts the player to choose a direction, and then moves the player in that direction"""
        print('what direction do you want to go? (n)North, (e)East, (s)South, (w)West')
        direction = input('>').strip().lower()
        if direction == 'q':
            quit()
        is_none = self.game_map.move_player(direction)
        if is_none is None:
            return
        else:
            self.game_map.serialize()
            print('Your Map:')
            print(self.game_map.display_map())

    def check_for_weapon(self):
        """Allows the player to check if they have any weapons in the bag
        ToDo: add if statements for additional weapons []

        """
        print('What would you like to use:')
        weapon_choice = input('>')
        if self.player.backpack.found_in_backpack(weapon_choice) == 'baseball bat':
            print('You have a baseball bat, you arm yourself with it')
        else:
            print('you dont have a weapon')

    def game_over(self, location):
        """Handles the game over scenarios and what to check for in each room"""
        if location is None:
            print("It is overrun with zombies, you get mauled and die, "
                  "do you want to replay? (y/n)")
            replay = input('>')
            if replay != 'y':
                print(f'Thank you for playing')
                quit()
            else:
                return False
        elif location.is_dangerous():
            weapon = 'baseball bat'
            if self.player.backpack.in_backpack(weapon):
                print(location.description)
                self.setup.print_separator()
                print('This area is dangerous')
            else:
                print('This area is dangerous')
                print("You don't have a weapon to defend yourself.")
                print("You get attacked by zombies and die.")
                replay = input("Do you want to replay? (y/n) ")
                if replay != 'y':
                    print(f'Thank you for playing {self.player.name}')
                    quit()
                else:
                    return False
        else:
            print(location.description)
