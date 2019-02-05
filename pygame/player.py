class Player:
    def __init__(self, **player):
        self.name = ""
        self.health = 100
        self.attack = 0
        self.defense = 0
        self.speed = 0
        self.gold = 100
        self.inventory = []
        self.rect = None
        self.movex = 0
        self.movey = 0
        self.__dict__.update(player)

    def print_stats(self):
        print("Name: {}".format(self.name))
        print("Attributes:")
        print()
        print("  * Attack: {}".format(self.attack))
        print("  * Defense: {}".format(self.defense))
        print("  * Speed: {}".format(self.speed))
        print()

    def update_stat(self, influenced_stat, amount):
        if influenced_stat:
            stat = getattr(self, influenced_stat)
            setattr(self, influenced_stat, stat + amount)

    def update(self):
        self.rect.x += self.movex
        self.rect.y += self.movey

    def moveUp(self):
        self.movey += -1

    def moveDown(self):
        self.movey += 1

    def moveLeft(self):
        self.movex += -1

    def moveRight(self):
        self.movex += 1

    def stopRight(self):
        self.movex += -1

    def stopLeft(self):
        self.movex += 1

    def stopDown(self):
        self.movey += -1

    def stopUp(self):
        self.movey += 1
