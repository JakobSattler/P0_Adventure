import game
import text_messages



def sell(item_name):
    item = game.find_item_by_name(item_name.lower())
    if not item:
        print(text_messages.get_message_item_not_owned(item_name))
    else:
        game.player.gold += int(item.price * 0.5)
        game.player.inventory.remove(item)
        print(text_messages.get_message_item_sold(item, game.player))


def buy(item_name, shop_inventory):
    item = game.find_item_by_name(item_name.lower(), shop_inventory)
    if not item:
        print(text_messages.get_message_item_not_selling(item_name))
        return

    if game.player.gold < item.price:
        print(text_messages.MESSAGE_NOT_ENOUGH_GOLD)
    else:
        game.player.gold -= item.price
        game.player.inventory.append(item)
        print(text_messages.get_message_item_bought(item, game.player))
