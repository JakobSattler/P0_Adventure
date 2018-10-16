from json_serialization import json_class

@json_class
class Room:
    def __init__(self, monster_list, reward_list):
        self.monsters = monster_list
        self.rewards = reward_list

