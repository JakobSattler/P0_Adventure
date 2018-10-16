from json_serialization import json_class

@json_class
class Room:
    def __init__(self, **data):
        self.monsters = []
        self.rewards = []
        self.__dict__.update(data)

