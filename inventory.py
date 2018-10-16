import game
import text_messages
import importlib

ACTION_ITEM_USE = "use"
ACTION_ITEM_DROP = "drop"
ACTION_INVENTORY_QUIT = "quit"

src_module_name = ""


def show(p_src_module_name):
    global src_module_name
    src_module_name = p_src_module_name
    # TODO: remove test items, load existing ones
    if not game.player.inventory:
        print(text_messages.MESSAGE_INVENTORY_EMPTY)
        # TODO: add return before call to save memory/keep from overflow?
        return close_inventory()

    inventory_action = input(text_messages.get_message_inventory_welcome(game.player.inventory, game.player))
    execute_inventory_action(inventory_action)


def execute_inventory_action(inventory_action):
    if inventory_action == ACTION_INVENTORY_QUIT:
        print(text_messages.MESSAGE_NOTHING_DONE)
        return close_inventory()
        # village.show()
    else:
        handle_item(inventory_action.lower())


def close_inventory():
    importlib.import_module(src_module_name).show()


def handle_item(item_name):
    # TODO: what to do, when item existing, but not in inventory?
    item = game.find_item_by_name(item_name)
    if item_name not in [item.name for item in game.items]:
        print(text_messages.MESSAGE_ITEM_NOT_EXISTING)
        show()
    else:
        for i in game.items:
            if i.name == item_name:
                item = i
        action = input(text_messages.get_message_use_or_drop(item))
        execute_item_action(action, item)


def execute_item_action(item_action, item):
    if item_action == ACTION_ITEM_USE:
        use_item(item)
    elif item_action == ACTION_ITEM_DROP:
        drop_item(item)
        close_inventory()
    else:
        print("Wrong input")


def drop_item(item):
    game.player.inventory.remove(game.find_item_by_name(item.name))
    print(text_messages.get_message_item_dropped(item))


def use_item(item):
    if item.passive_effect:
        print(text_messages.MESSAGE_ITEM_NOT_USABLE)
    else:
        stat = getattr(game.player, item.influenced_stat)
        setattr(game.player, item.influenced_stat, stat + item.amount)
        game.player.inventory.remove(item)
        print(text_messages.get_message_item_used(item, game.player))
    close_inventory()
