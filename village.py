import game
import inventory
import text
import treasure_chest
from dungeon import dungeon
from shop import Shop
from functools import partial

actions = {}
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

    if game.bonus_tasks:
        text.VILLAGE_OPTIONS.insert(text.VILLAGE_OPTIONS.index(text.OPTION_SAVE), text.OPTION_TREASURE_CHEST)
        text.VILLAGE_OPTIONS.insert(text.VILLAGE_OPTIONS.index(text.OPTION_SAVE), text.OPTION_GRAVE_DIGGER)

    update_actions()


def update_actions():
    global actions
    if game.bonus_tasks:
        actions.update({
            text.VILLAGE_OPTIONS.index(text.OPTION_TREASURE_CHEST) + 1: treasure_chest.show,
            text.VILLAGE_OPTIONS.index(text.OPTION_GRAVE_DIGGER) + 1: grave_digger.show
        })

    if dungeon.portal_used:
        text.VILLAGE_OPTIONS.insert(text.VILLAGE_OPTIONS.index(text.OPTION_SAVE), text.OPTION_PORT_TO_DUNGEON)
        actions.update({
            text.VILLAGE_OPTIONS.index(text.OPTION_PORT_TO_DUNGEON) + 1: dungeon.show
        })
    elif text.OPTION_PORT_TO_DUNGEON in text.VILLAGE_OPTIONS:
        text.VILLAGE_OPTIONS.remove(text.OPTION_PORT_TO_DUNGEON)

    actions.update({
        text.VILLAGE_OPTIONS.index(text.OPTION_INVENTORY) + 1: partial(inventory.show, __name__),
        text.VILLAGE_OPTIONS.index(text.OPTION_MERCHANT) + 1: merchant.show,
        text.VILLAGE_OPTIONS.index(text.OPTION_BLACKSMITH) + 1: blacksmith.show,
        text.VILLAGE_OPTIONS.index(text.OPTION_DRUID) + 1: druid.show,
        text.VILLAGE_OPTIONS.index(text.OPTION_DUNGEON) + 1: partial(dungeon.init, False),
        len(text.VILLAGE_OPTIONS) - 1: game.save_game,
        0: game.quit_game
    })


def show():
    update_actions()
    try:
        action = int(input(text.get_message_welcome_village(text.VILLAGE_OPTIONS)))
        actions[int(action)]()
    except (KeyError, ValueError):
        print(text.MESSAGE_INVALID_CHOICE)
        show()
