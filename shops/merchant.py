from shops.shop import Shop
import game
import text_messages


class Merchant(Shop):
    def __init__(self):
        super().__init__("merchant", game.player.inventory, True)

    def show(self):
        if not self.inventory:
            print(text_messages.MESSAGE_NOTHING_TO_SELL)
            self.close()
        else:
            super().show()
