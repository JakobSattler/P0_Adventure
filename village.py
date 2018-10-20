import game
import inventory
import text
import treasure_chest
from dungeon import dungeon
from shop import Shop
from functools import partial

actions = None
druid = None
blacksmith = None
merchant = None
grave_digger = None


def init():
    global grave_digger
    grave_digger = Shop("grave digger", [], False)

    global druid
    druid = Shop("druid", [item for item in game.items if not item.passive_effect], False)

    global blacksmith
    blacksmith = Shop("blacksmith", [item for item in game.items if item.passive_effect], False)

    global merchant
    merchant = Shop("merchant", game.player.inventory, True)

    # init action-dict
    global actions
    actions = {
        text.VILLAGE_OPTIONS.index("inventory") + 1: partial(inventory.show, __name__),
        text.VILLAGE_OPTIONS.index("merchant") + 1: merchant.show,
        text.VILLAGE_OPTIONS.index("blacksmith") + 1: blacksmith.show,
        text.VILLAGE_OPTIONS.index("druid") + 1: druid.show,
        text.VILLAGE_OPTIONS.index("dungeon") + 1: partial(dungeon.init, False),
        text.VILLAGE_OPTIONS.index("save game") + 1: game.save_game,
        0: game.quit_game
    }

    if game.bonus_tasks:
        text.VILLAGE_OPTIONS.insert(text.VILLAGE_OPTIONS.index("save game"), "treasure chest")
        text.VILLAGE_OPTIONS.insert(text.VILLAGE_OPTIONS.index("save game"), "grave digger")

        actions.update({
            text.VILLAGE_OPTIONS.index("treasure chest") + 1: treasure_chest.show,
            text.VILLAGE_OPTIONS.index("grave digger") + 1: grave_digger.show
        })


def show():
    if dungeon.portal_used:
        text.VILLAGE_OPTIONS.insert(text.VILLAGE_OPTIONS.index("save game"), "use portal to dungeon")
    elif "use portal to dungeon" in text.VILLAGE_OPTIONS:
        text.VILLAGE_OPTIONS.remove("use portal to dungeon")
    execute_village_action(input(text.get_message_welcome_village(text.VILLAGE_OPTIONS)))


# https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
# TODO: implement kind of switch
def execute_village_action(action):
    try:
        actions[int(action)]()
    except (KeyError, ValueError):
        print(text.MESSAGE_INVALID_CHOICE)
        show()
# if action == str(text.VILLAGE_OPTIONS.index("inventory") + 1):
#     inventory.show(__name__)
# elif action == str(text.VILLAGE_OPTIONS.index("merchant") + 1):
#     merchant.show()
# elif action == str(text.VILLAGE_OPTIONS.index("blacksmith") + 1):
#     blacksmith.show()
# elif action == str(text.VILLAGE_OPTIONS.index("druid") + 1):
#     druid.show()
# elif action == str(text.VILLAGE_OPTIONS.index("dungeon") + 1):
#     dungeon.init(False)
# elif action == str(text.VILLAGE_OPTIONS.index("save game") + 1):
#     game.save_game()
#     print("Game saved to " + game.savefile)
#     show()
# elif action == str(0):
#     game.quit_game()
# elif game.bonus_tasks:
#     if action == str(text.VILLAGE_OPTIONS.index("treasure chest") + 1):
#         treasure_chest.show()
#     elif action == str(text.VILLAGE_OPTIONS.index("grave digger") + 1):
#         grave_digger.show()
#     elif action == str(text.VILLAGE_OPTIONS.index("use portal to dungeon") + 1):
#         dungeon.show()
# else:
#     print(text.MESSAGE_INVALID_CHOICE)
#     show()
