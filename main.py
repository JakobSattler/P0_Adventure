#!/usr/bin/env python3

import argparse
import game
import dungeon.dungeon


# from player import Player
# from gamedata import GameData
# from json_serialization import save_gamedata, load_gamedata
# from character_create import input_player
# from vil import village_menu


def main():
    parser = argparse.ArgumentParser(description="P0 Adventure")
    parser.add_argument('--savefile', default="game.json",
                        help="The save file. default: 'game.json'")
    parser.add_argument("--new-game", dest="new_game", default=False, action='store_true',
                        help="Create a new save file.")
    parser.add_argument("-b", dest="bonus_tasks", default=False, action="store_true", help='enable bonus tasks')
    parser.add_argument("--print-bonus", dest="print_bonus", default=False, action="store_true",
                        help='print bonus task list and exit')
    args = parser.parse_args()

    game.start(args)


if __name__ == "__main__":
    main()
