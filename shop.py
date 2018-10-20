import game
import text
import inventory
import village


class Shop:
    def __init__(self, name, shop_inventory, buyer):
        self.name = name
        self.inventory = shop_inventory
        self.buyer = buyer

    @staticmethod
    def sell(item_name):
        item = game.find_item_by_name(item_name.lower())
        if not item:
            print(text.get_message_item_not_owned(item_name))
        else:
            game.player.gold += int(item.price * 0.5)
            inventory.remove_item(item)
            print(text.get_message_item_sold(item))

    def buy(self, item_name):
        item = game.find_item_by_name(item_name.lower(), self.inventory)
        if not item:
            print(text.get_message_item_not_selling(item_name))
            return

        if game.player.gold < item.price:
            print(text.MESSAGE_NOT_ENOUGH_GOLD)
        else:
            game.player.gold -= item.price
            inventory.add_item(item)
            if self.name == "grave digger":
                self.inventory.remove(item)
            print(text.get_message_item_bought(item))

    def show(self):
        if self.buyer and not self.inventory:
            print(text.MESSAGE_NOTHING_TO_SELL)
            self.close()
        else:
            action = input(text.get_message_shop_welcome(self))
            self.execute_action(action)

    @staticmethod
    def close():
        village.show()

    def execute_action(self, action):
        if action == "quit":
            self.close()
        else:
            if self.buyer:
                self.sell(action)
            else:
                self.buy(action)
            self.show()
