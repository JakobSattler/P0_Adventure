import text_messages
import game
import inventory
import village

items = []


def show():
    action = input(
        text_messages.get_message_treasure_chest(items, game.player).replace("inventory", "treasure chest"))
    if action == "leave":
        leave_item()
    elif action == "take":
        take_item()
    elif action == "quit":
        village.show()
    else:
        print("Invalid input")
        return show()


def leave_item():
    item_name = input("Which item do you want to leave?\n> ")
    item = game.find_item_by_name(item_name, game.player.inventory)
    if not item:
        print("Sorry, you do not own " + item_name + ".")
        return show()
    else:
        items.append(item)
        inventory.remove_item(item)
        return show()


def take_item():
    item_name = input("Which item do you want to take?\n> ")
    item = game.find_item_by_name(item_name, items)
    if not item:
        print("Sorry, item " + item_name + " not in chest.")
        return show()
    else:
        inventory.add_item(item)
        items.remove(item)
        return show()