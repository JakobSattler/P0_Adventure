import game
import inventory
import text_messages
import treasure_chest
from dungeon import dungeon
from shops.blacksmith import Blacksmith
from shops.druid import Druid
from shops.merchant import Merchant

options = ["inventory", "merchant", "blacksmith", "druid", "dungeon", "save game", "quit game"]

druid = None
blacksmith = None
merchant = None

keymap = {
    "ACTION_VILLAGE_INVENTORY": "1",
    "ACTION_VILLAGE_MERCHANT": "2",
    "ACTION_VILLAGE_BLACKSMITH": "3",
    "ACTION_VILLAGE_DRUID": "4",
    "ACTION_VILLAGE_DUNGEON": "5",
    "ACTION_VILLAGE_SAVE": "6",
    "ACTION_VILLAGE_QUIT": "0"
}


def init():
    if game.bonus_tasks:
        options.insert(options.index("save game"), "treasure chest")
        options.insert(options.index("save game"), "grave digger")

    global druid
    druid = Druid([item for item in game.items if not item.passive_effect])

    global blacksmith
    blacksmith = Blacksmith([item for item in game.items if item.passive_effect])

    global merchant
    merchant = Merchant()


def show():
    if dungeon.portal_used:
        options.insert(options.index("save game"), "use portal to dungeon")
    elif "use portal to dungeon" in options:
        options.remove("use portal to dungeon")
    execute_village_action(input(text_messages.get_message_welcome_village(options)))


# https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
# TODO: implement kind of switch
def execute_village_action(action):
    if action == str(options.index("inventory") + 1):
        inventory.show(__name__)
    elif action == str(options.index("merchant") + 1):
        merchant.show()
    elif action == str(options.index("blacksmith") + 1):
        blacksmith.show()
    elif action == str(options.index("druid") + 1):
        druid.show()
    elif action == str(options.index("dungeon") + 1):
        dungeon.init(False)
    elif action == str(options.index("save game") + 1):
        game.save_game()
        print("Game saved to " + game.savefile)
        show()
    elif action == str(0):
        game.quit_game()
    elif game.bonus_tasks:
        if action == str(options.index("treasure chest") + 1):
            treasure_chest.show()
        elif action == str(options.index("grave digger") + 1):
            grave_digger()
        elif action == str(options.index("use portal to dungeon") + 1):
            dungeon.show()
    else:
        print(text_messages.MESSAGE_INVALID_CHOICE)
        show()


def grave_digger():
    print("Here you can buy the items you lost when dying for 50% of the normal price")