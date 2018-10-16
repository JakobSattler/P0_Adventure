from dungeon.room import Room
import game
import text_messages
import inventory
from random import randint

import copy

random = False
monsters = []

default_rooms = []
cur_room = None

ACTION_INVENTORY = "1"
ACTION_LOOK_AROUND = "2"
ACTION_ATTACK = "3"
ACTION_OPEN_CHEST = "4"
ACTION_MOVE = "5"
ACTION_RUN_AWAY = "0"


def init(p_random=False):
    global random
    random = p_random

    if not random:
        set_default_rooms()
        global cur_room
        if not cur_room:
            cur_room = default_rooms[0]
    else:
        # do stuff
        print("randon dungeon not implemented yet")

    print_description()
    show()


def show():
    action = input(text_messages.MESSAGE_DUNGEON_MENU)
    if action == ACTION_INVENTORY:
        inventory.show(__name__)
    elif action == ACTION_LOOK_AROUND:
        print_description()
        show()
    elif action == ACTION_ATTACK:
        attack()
    elif action == ACTION_OPEN_CHEST:
        open_chest()
    elif action == ACTION_MOVE:
        move()
    elif action == ACTION_RUN_AWAY:
        global cur_room
        cur_room = None
        game.enter_village()


def move():
    global cur_room
    if cur_room.monsters:
        print(text_messages.MESSAGE_DUNGEON_MONSTERS_BLOCKING)
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
    print(text_messages.get_message_dungeon_desc(cur_room.monsters))


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


# TODO: REFACTOR TO LESS CODE!!!!!
def attack():
    if not cur_room.monsters:
        print(text_messages.MESSAGE_DUNGEON_ROOM_EMPTY)
        return show()

    while cur_room.monsters:
        while True:
            target = int(input(text_messages.get_message_dungeon_fight(
                cur_room.monsters, game.player)))
            if not 1 <= target <= len(cur_room.monsters):
                print(
                    "Please input a positive integer between 1 and the number of monsters")
            else:
                break

        target = cur_room.monsters[target - 1]

        attackers = cur_room.monsters.copy()
        attackers.append(game.player)
        attackers.sort(key=lambda x: x.speed, reverse=True)

        for attacker in attackers:
            if not isinstance(attacker, type(game.player)):
                defender = game.player
                # TODO: function to get damage
                if attacker.health > 0:
                    print(text_messages.get_message_defending(
                        attacker, str(deal_damage(attacker, defender))))
                if defender.health <= 0:
                    print(text_messages.get_message_dungeon_player_died(attacker))
                    reset_player()
                    return game.enter_village()
            else:
                defender = target
                print(text_messages.get_message_attacking(
                    defender, str(deal_damage(attacker, defender))))
                if defender.health <= 0:
                    reward = get_reward(defender)
                    game.player.gold += reward
                    cur_room.monsters.remove(defender)
                    print(text_messages.get_message_dungeon_monster_died(
                        defender, str(reward)))

    print(text_messages.MESSAGE_DUNGEON_ENEMIES_DEFEATED)
    show()


def reset_player():
    inventory.clear()
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
        print(text_messages.MESSAGE_DUNGEON_MONSTERS_BLOCKING)
        return show()

    if cur_room.rewards:
        print(text_messages.MESSAGE_DUNGEON_CHEST_REWARD)
        game.player.inventory = game.player.inventory + cur_room.rewards
    else:
        print(text_messages.MESSAGE_DUNGEON_CHEST_EMPTY)
    show()


def get_reward(monster):
    return randint(monster.reward_min, monster.reward_max)
