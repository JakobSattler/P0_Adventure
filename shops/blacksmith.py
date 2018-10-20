from shops.shop import Shop


class Blacksmith(Shop):
    def __init__(self, shop_inventory):
        super().__init__("blacksmith", shop_inventory, False)
