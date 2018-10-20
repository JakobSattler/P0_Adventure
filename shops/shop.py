import game
import text_messages
import inventory
import village


class Shop:
    def __init__(self, name, shop_inventory, selling):
        self.name = name
        self.inventory = shop_inventory
        self.selling = selling

    def sell(self, item_name):
        item = game.find_item_by_name(item_name.lower())
        if not item:
            print(text_messages.get_message_item_not_owned(item_name))
        else:
            game.player.gold += int(item.price * 0.5)
            inventory.remove_item(item)
            print(text_messages.get_message_item_sold(item, game.player))

    def buy(self, item_name):
        item = game.find_item_by_name(item_name.lower(), self.inventory)
        if not item:
            print(text_messages.get_message_item_not_selling(item_name))
            return

        if game.player.gold < item.price:
            print(text_messages.MESSAGE_NOT_ENOUGH_GOLD)
        else:
            game.player.gold -= item.price
            inventory.add_item(item)
            print(text_messages.get_message_item_bought(item, game.player))

    def show(self):
        action = input(text_messages.get_message_shop_welcome(self, game.player))
        self.execute_action(action)

    @staticmethod
    def close():
        village.show()

    def execute_action(self, action):
        if action == "quit":
            self.close()
        else:
            if self.selling:
                self.sell(action)
            else:
                self.buy(action)
            self.show()
