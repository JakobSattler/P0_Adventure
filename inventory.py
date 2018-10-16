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
        return close_inventory()
        # village.show()
    else:
        handle_item(inventory_action.lower())


def close_inventory():
    importlib.import_module(src_module_name).show()


def handle_item(item_name):
    # TODO: what to do, when item existing, but not in inventory?
    if item_name not in [item.name for item in game.items]:
        print(text_messages.MESSAGE_ITEM_NOT_EXISTING)
        show(src_module_name)
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
    remove_item(item)
    print(text_messages.get_message_item_dropped(item))


def use_item(item):
    if item.passive_effect:
        print(text_messages.MESSAGE_ITEM_NOT_USABLE)
    else:
        game.player.update_stat(item.influenced_stat, item.amount)
        remove_item(item)
        print(text_messages.get_message_item_used(item, game.player))
    close_inventory()

def add_item(item):
    if item.passive_effect:
        game.player.update_stat(item.influenced_stat, item.amount)
    game.player.inventory.append(item)

def remove_item(item):
    print("removing item " + item.name)
    if item.passive_effect:
        game.player.update_stat(item.influenced_stat, item.amount * -1)
    game.player.inventory.remove(item)
