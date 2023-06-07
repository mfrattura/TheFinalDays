from game.gameplay import Gameplay

if __name__ == "__main__":
    gameplay = Gameplay()
    gameplay.start_game()
    while True:
        x, y = gameplay.game_map.get_player_location()
        current_location = gameplay.game_map.get_location(x, y)
        print(current_location.description)
        while True:
            gameplay.setup.print_separator()
            gameplay.setup.show_controls()
            choice = input('>').strip().lower()
            if choice == 'l':
                gameplay.show_location_items(current_location)
                continue
            elif choice == 'o':
                gameplay.show_prompt_response(current_location)
                continue
            elif choice == 'a':
                gameplay.check_for_weapon()
            elif choice == 'i':
                gameplay.show_backpack_items()
                continue
            elif choice == 'p':
                gameplay.pick_up_item(current_location)
                continue
            elif choice == 'm':
                gameplay.move_player()
                break
