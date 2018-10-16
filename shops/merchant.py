from text_messages import *
import game
from shops import shop
import village

ACTION_QUIT = "quit"


def show_merchant():
    if game.player.inventory:
        action = input(get_message_welcome_merchant(game.player))
        execute_merchant_action(action.lower())
    else:
        print(MESSAGE_NOTHING_TO_SELL)
        game.enter_village()


def execute_merchant_action(action):
    if action == ACTION_QUIT:
        village.show()
    else:
        sell_item(action)


# def sell_item(item_name):
#         item = game.find_first_item_by_name(item_name)
#         if item not in game.player.inventory:
#             print(get_message_item_not_owned(item_name))
#         else:
#             game.player.gold += item.price * 0.5
#             game.player.inventory.remove(item)
#             print(get_message_item_sold(item, game.player))
#         show_merchant()

def sell_item(item_name):
    shop.sell(item_name)
    show_merchant()
