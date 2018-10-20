# TODO: implement function to find item by name

import os

import dungeon.dungeon as dungeon
import json_serialization
import village
from dungeon.monster import Monster
from gamedata import GameData
from item import Item
from player import Player
import text

keymap = {
    "ACTION_VILLAGE_INVENTORY": "1",
    "ACTION_VILLAGE_MERCHANT": "2",
    "ACTION_VILLAGE_BLACKSMITH": "3",
    "ACTION_VILLAGE_DRUID": "4",
    "ACTION_VILLAGE_DUNGEON": "5",
    "ACTION_VILLAGE_SAVE": "6",
    "ACTION_VILLAGE_QUIT": "0"
}

ACTION_INVENTORY_QUIT = "quit"

ACTION_ITEM_USE = "use"
ACTION_ITEM_DROP = "drop"

player = Player()

items = []

monsters = []

savefile = None

bonus_tasks = False
impl_bonus_tasks = ["5", "6", "7"]


def start(args):
    global savefile
    savefile = args.savefile

    if args.print_bonus:
        print_bonus_tasks()
        quit()

    if args.bonus_tasks:
        global bonus_tasks
        bonus_tasks = True
        # TODO: implement bonus tasks

    if args.new_game:
        create_char()
    else:
        load_game()

    init()
    village.show()


def create_char():
    char_name = input(text.MESSAGE_WELCOME_CREATE)

    while True:
        print(text.MESSAGE_ASSIGN_POINTS)
        char_attack = read_stat(text.MESSAGE_ASSIGN_ATTACK)
        char_defense = read_stat(text.MESSAGE_ASSIGN_DEFENSE)
        char_speed = read_stat(text.MESSAGE_ASSIGN_SPEED)

        if (char_attack + char_defense + char_speed) > 100:
            print(text.MESSAGE_TOO_MANY_POINTS)
        else:
            break

    print("Before you store your character please confirm your stats!")
    confirm_text = text.MESSAGE_CONFIRM_STATS.replace("{char_name}", char_name).replace("{char_attack}",
                                                                                        str(char_attack)) \
        .replace("{char_defense}", str(char_defense)).replace("{char_speed}", str(char_speed))
    if not get_confirm(confirm_text, True):
        create_char()
    else:
        # assign values to player-object
        player.name = char_name
        player.attack = char_attack
        player.defense = char_defense
        player.speed = char_speed


# looked up how to get relative path in python
# https://stackoverflow.com/questions/918154/relative-paths-in-python
def init():
    init_items("res/items.json")
    if bonus_tasks:
        init_items("res/items_bonus.json")
    init_monsters()
    village.init()


def init_items(path):
    filename = os.path.join(os.path.dirname(__file__), path)

    for item in json_serialization.load_file(filename):
        item.name = item.name.lower()
        items.append(item)


def init_monsters():
    filename = os.path.join(os.path.dirname(__file__), "res/monsters.json")
    monsters_loaded = (json_serialization.load_file(filename)["monsters"])

    for monster_json in monsters_loaded:
        monster = Monster(**monster_json)
        monster.name = monster.name.lower()
        monsters.append(monster)


def enter_village():
    village.show()


def read_stat(stat_text):
    try:
        stat = int(input(stat_text))
        if stat <= 0:
            print(text.MESSAGE_NEGATIVE_ASSIGNED)
            return read_stat(stat_text)
        return stat
    except ValueError:
        print("Error: Please input an integer")
        return read_stat(stat_text)


def get_confirm(confirm_text, validate):
    confirm = input(confirm_text).lower()
    while confirm != "y" and confirm != "n" and validate:
        print(text.MESSAGE_WRONG_CONFIRM_CHAR)
        confirm = input().lower()

    if confirm == "y":
        return True
    else:
        return False


def invalid_village_choice():
    print(text.MESSAGE_INVALID_CHOICE)


def quit_game():
    if get_confirm("Save before exiting? (Y/N)", False):
        save_game()
        quit()
    else:
        quit()


# TODO: replace item list with dict for easier access
def find_item_by_name(item_name, item_list=items):
    try:
        return [item for item in item_list if item.name == item_name][0]
    except IndexError:
        return None


# TODO: replace monster list with dict for easier access
def find_monster_by_name(name):
    try:
        return [monster for monster in monsters if monster.name == name][0]
    except IndexError:
        return None


def print_bonus_tasks():
    print(",".join(str(x) for x in impl_bonus_tasks))


def save_game():
    gamedata = GameData(
        **{"player": player, "dungeon_room": dungeon.cur_room, "bonus_tasks": bonus_tasks, "savefile": savefile})
    json_serialization.save_file(gamedata, savefile)
    print("Game saved to " + savefile)
    village.show()


def load_game():
    global savefile
    global player
    global bonus_tasks

    gamedata = json_serialization.load_file(savefile)
    player = gamedata.player
    dungeon.cur_room = gamedata.dungeon_room
    bonus_tasks = gamedata.bonus_tasks

    savefile = gamedata.savefile

    init()
    village.show()


# variable to not remove item import when organizing imports
__all__ = ["Item"]
