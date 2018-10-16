# TODO: implement function to find item by name

import pdb

import os
from shops import blacksmith, druid

from text_messages import *
from player import Player
from item import Item
import json_serialization
import village
from dungeon.monster import Monster
from gamedata import GameData
import dungeon.dungeon as dungeon

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


def start(args):
    global savefile
    savefile = args.savefile

    if args.print_bonus:
        print_bonus_tasks()
        quit()

    if args.new_game:
        create_char()
    else:
        load_game()
    if args.bonus_tasks:
        bonus_tasks = True
        print()
        # TODO: implement bonus tasks

    init()
    village.show()


def create_char():
    char_name = input(MESSAGE_WELCOME_CREATE)

    while True:
        print(MESSAGE_ASSIGN_POINTS)
        char_attack = read_stat(MESSAGE_ASSIGN_ATTACK)
        char_defense = read_stat(MESSAGE_ASSIGN_DEFENSE)
        char_speed = read_stat(MESSAGE_ASSIGN_SPEED)

        if (char_attack + char_defense + char_speed) > 100:
            print(MESSAGE_TOO_MANY_POINTS)
        else:
            break

    print("Before you store your character please confirm your stats!")
    confirm_text = MESSAGE_CONFIRM_STATS.replace("{char_name}", char_name).replace("{char_attack}",
                                                                                   str(char_attack)) \
        .replace("{char_defense}", str(char_defense)).replace("{char_speed}", str(char_speed))
    if not confirm_stats(confirm_text):
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
    init_items()
    init_monsters()


def init_items():
    filename = os.path.join(os.path.dirname(__file__), "res/items.json")

    for item in json_serialization.load_file(filename):
        item.name = item.name.lower()
        items.append(item)
        if item.passive_effect:
            blacksmith.inventory.append(item)
        else:
            druid.inventory.append(item)


def init_monsters():
    filename = os.path.join(os.path.dirname(__file__), "res/monsters.json")
    monsters_loaded = (json_serialization.load_file(filename)["monsters"])

    for monster_json in monsters_loaded:
        monster = Monster(**monster_json)
        monster.name = monster.name.lower()
        monsters.append(monster)


def enter_village():
    village.show()


def confirm_stats(confirm_text):
    confirm = input(confirm_text)
    while confirm.lower() != "y" and confirm.lower() != "n":
        print(MESSAGE_WRONG_CONFIRM_CHAR)
        confirm = input()
    if confirm.lower() == "n":
        return False
    else:
        return True


def read_stat(stat_text):
    stat = int(input(stat_text))

    if stat <= 0:
        print(MESSAGE_NEGATIVE_ASSIGNED)
        return read_stat(stat_text)
    return stat


def invalid_village_choice():
    print(MESSAGE_INVALID_CHOICE)


def quit_game():
    action = input("Save before exiting? (Y/N)")
    if action.lower() == "n":
        quit()
    else:
        save_game()
        quit()


# TODO: replace item list with dict for easier access
def find_item_by_name(item_name, item_list=items):
    for item in item_list:
        if item.name == item_name:
            return item
    return None


# TODO: replace monster list with dict for easier access
def find_monster_by_name(name):
    for monster in monsters:
        if monster.name == name:
            return monster
    return None


def print_bonus_tasks():
    # TODO: insert the tasks you implemented
    bonus_tasks = []
    print(",".join(str(x) for x in bonus_tasks))


def save_game():
    gamedata = GameData(
        **{"player": player, "dungeon_room": dungeon.cur_room, "bonus_tasks": False, "savefile": savefile})
    json_serialization.save_file(gamedata, savefile)


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
