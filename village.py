import game
import text_messages
import inventory
from shops import merchant, druid, blacksmith
from dungeon import dungeon

keymap = {
    "ACTION_VILLAGE_INVENTORY": "1",
    "ACTION_VILLAGE_MERCHANT": "2",
    "ACTION_VILLAGE_BLACKSMITH": "3",
    "ACTION_VILLAGE_DRUID": "4",
    "ACTION_VILLAGE_DUNGEON": "5",
    "ACTION_VILLAGE_SAVE": "6",
    "ACTION_VILLAGE_QUIT": "0"
}


def show():
    execute_village_action(input(text_messages.MESSAGE_WELCOME_VILLAGE))


# https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
# TODO: implement kind of switch
def execute_village_action(action):
    if action == keymap.get("ACTION_VILLAGE_INVENTORY"):
        inventory.show(__name__)
    elif action == keymap.get("ACTION_VILLAGE_MERCHANT"):
        merchant.show_merchant()
    elif action == keymap.get("ACTION_VILLAGE_BLACKSMITH"):
        blacksmith.show_blacksmith()
    elif action == keymap.get("ACTION_VILLAGE_DRUID"):
        druid.show_druid()
    elif action == keymap.get("ACTION_VILLAGE_QUIT"):
        game.quit_game()
    elif action == keymap.get("ACTION_VILLAGE_DUNGEON"):
        dungeon.init(False)
    elif action == keymap.get("ACTION_VILLAGE_SAVE"):
        game.save_game()
        print("Game saved to " + game.savefile)
        show()
    else:
        print(text_messages.MESSAGE_INVALID_CHOICE)
        show()
