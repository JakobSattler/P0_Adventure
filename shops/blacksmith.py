from text_messages import *
import game
from shops import shop
import village

ACTION_QUIT = "quit"
inventory = []


def show_blacksmith():
    action = input(get_message_welcome_blacksmith(inventory, game.player))
    execute_merchant_action(action)

def execute_merchant_action(action):
    if action == ACTION_QUIT:
        village.show()
    else:
        buy_item(action)


# def sell_item(item_name):
#         item = game.find_first_item_by_name(item_name)
#         if item not in game.player.inventory:
#             print(get_message_item_not_owned(item_name))
#         else:
#             game.player.gold += item.price * 0.5
#             game.player.inventory.remove(item)
#             print(get_message_item_sold(item, game.player))
#         show_merchant()

def buy_item(item_name):
    shop.buy(item_name, inventory)
    show_blacksmith()
