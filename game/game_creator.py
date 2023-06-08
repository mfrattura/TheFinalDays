import json
from game.prompt import Prompt
from game.location import Location
from game.item import Item
from game.map import Map


class GameCreator:
    """
    Class responsible for creating the game world and set-up

    """
    def __init__(self):
        self.player_map = Map(size=(4, 4))

    def create_world(self, filename):
        """
        Creates the game world based on the provided JSON file

        :param filename:

        """
        with open(filename, 'r') as file:
            data = json.load(file)

            locations_data = data['locations']

            for location_data in locations_data:
                prompts = [Prompt(prompt['id'], prompt['prompt'], prompt['response'])
                           for prompt in location_data['prompts']]
                location = Location(
                    location_data['id'],
                    location_data['name'],
                    location_data['description'],
                    prompts,
                    [Item(*item.values()) for item in location_data['items']
                     if isinstance(item, dict)],
                    location_data.get('is_dangerous', False)
                )
                self.player_map.add_location(
                    location_data['coordinates'][0],
                    location_data['coordinates'][1],
                    location)

    def setup_game(self, filename):
        """
        Sets up the game by creating the game world and returning the player map
        :param filename:
        :return: the player map representing the game world
        """
        self.create_world(filename)
        return self.player_map



    @staticmethod
    def the_goal():
        """
        Displays the goal of the game to the player

        """
        print('In this zombie adventure game, your goal is to navigate through \n'
              'various locations, including your bedroom, bathroom, living \n'
              'room, hallway, garage, street, highway, mall, and tunnel, while \n'
              'avoiding or defeating zombies and other dangers. \n'
              'Your primary objective is to stay alive and find a\n'
              'secure place where you can establish a safe haven away from the undead')

    @staticmethod
    def print_separator():
        print('*------------------------------------------------------------------------------------*')

    @staticmethod
    def intro_scene():
        """
        Displays the introductory scene of the game to the player

        """
        print('*------------------------------------------------------------------------------------*')
        print('You wake up in your bedroom, feeling groggy and disoriented. As you sit up in bed you \n'
              'notice a strange smell in the air, something is wrong.. you glance around your room \n'
              'and everything seems fine.. ')
        print('You check your phone, but as you tap the screen you start to notice there is no service \n'
              'you start to feel uneasy, you get up and walk over to the window to have a look and you see \n'
              'something that makes your heart sink into your chest.. ')
        print('the streets are deserted, there are no people or cars on the road. The world has come to a halt \n'
              'then you see it - a person runs out of their house, being chase by something, they are \n'
              'screaming, its a zombie.\n')
        print('This must be the Final Days, what is your name?')

    @staticmethod
    def show_controls():
        """
        Shows the controls of the game to the player

        """
        print("What would you like to do?")
        print("Options:")
        print("  - Press 'l' to look around.")
        print("  - Press 'a' to arm yourself.")
        print("  - Press 'i' to check inventory.")
        print("  - Press 'p' to pick up items.")
        print("  - Press 'm' to move locations.")
        print("  - Press 'o' for additional options.")



