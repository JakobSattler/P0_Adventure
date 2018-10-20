import game
import text
import inventory
import village
from random import randint
from functools import partial

import copy

from dungeon.room import Room

random = False
monsters = []

default_rooms = []

cur_room = None

portal_used = False

actions = None


def init(p_random=False):
    global random
    random = p_random

    if not random:
        set_default_rooms()
        global cur_room
        cur_room = default_rooms[0]
    else:
        # do stuff
        print("Error - random dungeon not implemented yet")
        game.enter_village()

    if not actions:
        init_actions()

    print_description()
    show()


def init_actions():
    global actions
    actions = {
        text.DUNGEON_OPTIONS.index(text.OPTION_INVENTORY) + 1: partial(inventory.show, __name__),
        text.DUNGEON_OPTIONS.index(text.OPTION_LOOK_AROUND) + 1: look_around,
        text.DUNGEON_OPTIONS.index(text.OPTION_ATTACK) + 1: attack,
        text.DUNGEON_OPTIONS.index(text.OPTION_OPEN_CHEST) + 1: open_chest,
        text.DUNGEON_OPTIONS.index(text.OPTION_MOVE) + 1: move,
        0: partial(leave_dungeon, False)
    }


def look_around():
    print_description()
    show()


def open_portal():
    global actions

    if not actions:
        init_actions()

    text.DUNGEON_OPTIONS.insert(text.DUNGEON_OPTIONS.index(text.OPTION_RUN), text.OPTION_PORT_TO_VILLAGE)
    actions.update({
        text.DUNGEON_OPTIONS.index(text.OPTION_PORT_TO_VILLAGE) + 1: partial(leave_dungeon, True)
    })


def close_portal():
    global actions
    del actions[text.DUNGEON_OPTIONS.index(text.OPTION_PORT_TO_VILLAGE) + 1]
    text.DUNGEON_OPTIONS.remove(text.OPTION_PORT_TO_VILLAGE)


def show():
    try:
        action = int(input(text.get_message_dungeon_menu(text.DUNGEON_OPTIONS)))
        actions[action]()
    except (KeyError, ValueError):
        print(text.MESSAGE_INVALID_CHOICE)
        show()


def leave_dungeon(portal):
    global portal_used
    portal_used = portal
    if portal_used:
        close_portal()
    game.enter_village()


def move():
    global cur_room
    if cur_room.monsters:
        print(text.MESSAGE_DUNGEON_MONSTERS_BLOCKING)
        show()
    if not random:
        if cur_room == default_rooms[0]:
            index = 1
        else:
            index = 0
        set_default_rooms()
        cur_room = default_rooms[index]

    show()


def print_description():
    print(text.get_message_dungeon_desc(cur_room.monsters))


def set_default_rooms():
    room_1_monsters = [copy.deepcopy(game.find_monster_by_name("rat")),
                       copy.deepcopy(game.find_monster_by_name("gnoll"))]
    room_1_rewards = None
    room_2_monsters = [copy.deepcopy(game.find_monster_by_name("wolf")),
                       copy.deepcopy(game.find_monster_by_name("rat"))]
    room_2_rewards = [game.find_item_by_name("potion")]
    room_1 = {"monsters": room_1_monsters, "rewards": room_1_rewards}
    room_2 = {"monsters": room_2_monsters, "rewards": room_2_rewards}
    global default_rooms
    default_rooms = [Room(**room_1), Room(**room_2)]


def attack():
    if not cur_room.monsters:
        print(text.MESSAGE_DUNGEON_ROOM_EMPTY)
        return show()

    while cur_room.monsters:
        while True:
            try:
                target = int(input(text.get_message_dungeon_fight(
                    cur_room.monsters)))
                if not 1 <= target <= len(cur_room.monsters):
                    print(text.MESSAGE_DUNGEON_WRONG_MONSTER)
                else:
                    break
            except ValueError:
                print(text.MESSAGE_DUNGEON_WRONG_MONSTER)

        target = cur_room.monsters[target - 1]

        attackers = cur_room.monsters.copy()
        attackers.append(game.player)
        attackers.sort(key=lambda x: x.speed, reverse=True)

        for attacker in attackers:
            if not isinstance(attacker, type(game.player)):
                defender = game.player
                if attacker.health > 0:
                    print(text.get_message_defending(
                        attacker, str(deal_damage(attacker, defender))))
                if defender.health <= 0:
                    print(text.get_message_dungeon_player_died(attacker))
                    reset_player()
                    return game.enter_village()
            else:
                defender = target
                print(text.get_message_attacking(
                    defender, str(deal_damage(attacker, defender))))
                if defender.health <= 0:
                    reward = get_reward(defender)
                    game.player.gold += reward
                    cur_room.monsters.remove(defender)
                    print(text.get_message_dungeon_monster_died(
                        defender, str(reward)))

    print(text.MESSAGE_DUNGEON_ENEMIES_DEFEATED)
    show()


def reset_player():
    village.grave_digger.inventory = copy.deepcopy(game.player.inventory)
    inventory.clear_inventory()
    game.player.health = 100
    global cur_room
    cur_room = None


def deal_damage(attacker, defender):
    damage = int((attacker.attack * attacker.attack) /
                 (attacker.attack + defender.defense))
    defender.health -= damage
    return damage


def open_chest():
    if cur_room.monsters:
        print(text.MESSAGE_DUNGEON_MONSTERS_BLOCKING)
        return show()

    if cur_room.rewards:
        print(text.MESSAGE_DUNGEON_CHEST_REWARD)
        game.player.inventory = game.player.inventory + cur_room.rewards
    else:
        print(text.MESSAGE_DUNGEON_CHEST_EMPTY)
    show()


def get_reward(monster):
    return randint(monster.reward_min, monster.reward_max)
