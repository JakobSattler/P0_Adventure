from shops.shop import Shop


class Druid(Shop):
    def __init__(self, shop_inventory):
        super(Druid, self).__init__("druid", shop_inventory, False)
