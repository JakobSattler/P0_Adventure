import game

OPTION_INVENTORY = "Inventory"
OPTION_MERCHANT = "Merchant"
OPTION_BLACKSMITH = "blacksmith"
OPTION_DRUID = "Druid"
OPTION_DUNGEON = "Dungeon"
OPTION_TREASURE_CHEST = "Treasure chest"
OPTION_GRAVE_DIGGER = "Grave digger"
OPTION_PORT_TO_DUNGEON = "Use portal to dungeon"
OPTION_SAVE = "Save game"
OPTION_QUIT_GAME = "Quit game"

OPTION_LOOK_AROUND = "Look Around"
OPTION_ATTACK = "Attack"
OPTION_OPEN_CHEST = "Open chest"
OPTION_MOVE = "Move"
OPTION_PORT_TO_VILLAGE = "Use portal to village"
OPTION_RUN = "Run away (leave dungeon)"


VILLAGE_OPTIONS = [OPTION_INVENTORY, OPTION_MERCHANT, OPTION_BLACKSMITH, OPTION_DRUID, OPTION_DUNGEON, OPTION_SAVE, OPTION_QUIT_GAME]
DUNGEON_OPTIONS = [OPTION_INVENTORY, OPTION_LOOK_AROUND, OPTION_ATTACK, OPTION_OPEN_CHEST, OPTION_MOVE, OPTION_RUN]

ERROR_NOT_INTEGER = "Error: please input an integer"

MESSAGE_WELCOME_CREATE = "Welcome to P0 Dungeon Quest character creator!\n" \
                         "Enter your name: "

MESSAGE_ASSIGN_POINTS = "You have 100 points to assign to your character.\n" \
                        "Start now to assign those Points to your characters attack, defense and speed."
MESSAGE_ASSIGN_ATTACK = "Attack: "
MESSAGE_ASSIGN_DEFENSE = "Defense: "
MESSAGE_ASSIGN_SPEED = "Speed: "
MESSAGE_NEGATIVE_ASSIGNED = "Please input a positive integer."
MESSAGE_TOO_MANY_POINTS = "Sorry, it seems like you spent more than 100 ability points on your character... " \
                          "Try that again!\n"

MESSAGE_CONFIRM_STATS = "Name: {char_name}\n" \
                        "Attributes:\n\n" \
                        "  * Attack: {char_attack}\n" \
                        "  * Defense: {char_defense}\n" \
                        "  * Speed: {char_speed}\n\n" \
                        "Is this correct? (Y/N) "

MESSAGE_WRONG_CONFIRM_CHAR = "Please enter Y/y for yes or N/n for no!"


def get_confirm_stats_message(char_name, char_attack, char_defense, char_speed):
    return MESSAGE_CONFIRM_STATS.replace("{char_name}", char_name).replace("{char_attack}", char_attack) \
        .replace("{char_defense}", char_defense).replace("{char_speed}", char_speed)


# vil
MESSAGE_WELCOME_VILLAGE = "Welcome to Prog0 Village!\n" \
                          "What do you want to do?\n" \
                          "{options}" \
                          "> "
MESSAGE_INVALID_CHOICE = "Invalid choice. Try again."

# inventory
MESSAGE_INVENTORY_EMPTY = "Your inventory is empty."
MESSAGE_WELCOME_INVENTORY = "Welcome to your inventory {char_name}!\n" \
                            "These are your items:\n\n" \
                            "{items}\n" \
                            "Type 'quit' or the name of the item you want to use/drop:\n" \
                            "> "
MESSAGE_USE_OR_DROP = "Do you want to 'use' or 'drop' {item_name}? Else 'quit'.\n" \
                      "> "
MESSAGE_NOTHING_DONE = "Nothing done.\n"
MESSAGE_ITEM_NOT_EXISTING = "Item does not exist."
MESSAGE_ITEM_USED = "You used {item_name}.\n" \
                    "It increased your {influenced_attribute} by {amount}.\n" \
                    "You now have {new_stat_amount} {influenced_attribute}."
MESSAGE_ITEM_DROPPED = "You dropped {item_name}.\n"

MESSAGE_ITEM_NOT_USABLE = "You cannot use this item.\n"

MESSAGE_WELCOME_TREASURE_CHEST = "Welcome to your treasure chest {char_name}!\n" \
                                 "You can leave your items here while fighting yourself " \
                                 "through the dungeon so you won't " \
                                 "loose your items!\n" \
                                 "These are the items currently placed in the chest:\n\n" \
                                 "{items}\n" \
                                 "Do you want to 'leave' or 'take' an item? Else 'quit'.\n" \
                                 "> "


def get_message_welcome_village(options):
    options_text = ""
    for option in options:
        key = options.index(option) + 1 if not option == OPTION_QUIT_GAME else 0
        options_text += "  {}) {}\n".format(key, option.capitalize())
    options_text += "\n"
    return MESSAGE_WELCOME_VILLAGE.replace("{options}", options_text)


def get_message_treasure_chest(chest):
    return MESSAGE_WELCOME_TREASURE_CHEST.replace("{char_name}", game.player.name).replace("{items}",
                                                                                           get_inventory_list(chest))


def get_message_inventory_welcome(items):
    return MESSAGE_WELCOME_INVENTORY.replace("{items}", get_inventory_list(items)).replace("{char_name}",
                                                                                           game.player.name)


def get_inventory_list(items):
    item_text = ""
    for item in items:
        item_desc = "({:+d} {} when {})".format(item.amount, item.influenced_stat,
                                                "held" if item.passive_effect else "used")
        item_text += "  * {:20} {}\n".format(item.name.capitalize(), item_desc)
    return item_text


def get_message_item_used(item):
    # TODO: Exception for stat not existing
    if item.influenced_stat:
        new_stat = str(getattr(game.player, str(item.influenced_stat).lower()))
        return MESSAGE_ITEM_USED.replace("{item_name}", item.name.capitalize()) \
            .replace("{influenced_attribute}", item.influenced_stat) \
            .replace("{new_stat_amount}", new_stat) \
            .replace("{amount}", str(item.amount))
    return MESSAGE_ITEM_USED.replace("{item_name}", item.name.capitalize())


def get_message_use_or_drop(item):
    return MESSAGE_USE_OR_DROP.replace("{item_name}", item.name.capitalize())


def get_message_item_dropped(item):
    return MESSAGE_ITEM_DROPPED.replace("{item_name}", item.name.capitalize())


MESSAGE_WELCOME_MERCHANT = "Welcome to the merchant!\n" \
                           "You have {amount_of_gold} gold. This is what I would pay for your items:\n\n" \
                           "{items}\n" \
                           "Type 'quit' or the name of the item you want to sell.\n" \
                           "> "
MESSAGE_ITEM_NOT_OWNED = "You do not possess a {item_name}.\n"
MESSAGE_ITEM_SOLD = "You have chosen {item_name}.\n" \
                    "You now have {amount_of_gold} gold left.\n" \
                    "Removed item from inventory.\n"
MESSAGE_NOTHING_TO_SELL = "Sorry, you have nothing to sell.\n" \
                          "Thanks for visiting!\n"
MESSAGE_ITEM_BOUGHT = "You have chosen {item}.\n" \
                      "You have {amount_of_gold} gold left.\n"
MESSAGE_ITEM_NOT_SELLING = "I do not sell '{item_name}'.\n"
MESSAGE_NOT_ENOUGH_GOLD = "Not enough gold.\n"


def get_message_item_not_owned(item_name):
    return MESSAGE_ITEM_NOT_OWNED.replace("{item_name}", item_name.title())


def get_message_item_sold(item):
    return MESSAGE_ITEM_SOLD.replace("{item_name}", item.name.capitalize()).replace("{amount_of_gold}",
                                                                                    str(game.player.gold))


def get_message_item_bought(item):
    return MESSAGE_ITEM_BOUGHT.replace("{item}", item.name.capitalize()).replace("{amount_of_gold}",
                                                                                 str(game.player.gold))


def get_message_item_not_selling(item_name):
    return MESSAGE_ITEM_NOT_SELLING.replace("{item_name}", item_name)


MESSAGE_WELCOME_BLACKSMITH = "Welcome to the blacksmith\n" \
                             "You have {amount_of_gold} gold to spend. This is what I'm selling:\n\n" \
                             "{items}\n" \
                             "Type 'quit' or the name of the item you want to buy.\n" \
                             "> "

MESSAGE_WELCOME_SHOP_BUY = "Welcome to the {shop_name}\n" \
                           "You have {amount_of_gold} gold to spend. This is what I'm selling:\n\n" \
                           "{items}\n" \
                           "Type 'quit' or the name of the item you want to buy.\n" \
                           "> "

MESSAGE_WELCOME_SHOP_SELL = "Welcome to the {shop_name}!\n" \
                            "You have {amount_of_gold} gold. This is what I would pay for your items:\n\n" \
                            "{items}\n" \
                            "Type 'quit' or the name of the item you want to sell.\n" \
                            "> "


def get_message_shop_welcome(shop):
    item_text = ""
    for item in shop.inventory:
        price = item.price if not shop.buyer else int(item.price * 0.5)
        item_desc = "({:+d} {} when {})".format(item.amount, item.influenced_stat,
                                                "held" if item.passive_effect else "used") if not shop.buyer else ""
        item_text += "  * {:20} for {:4d} gold {}\n".format(item.name.capitalize(),
                                                            price, item_desc)
    if not shop.buyer:
        return MESSAGE_WELCOME_SHOP_BUY.replace("{amount_of_gold}", str(game.player.gold)).replace("{items}",
                                                                                                   item_text).replace(
            "{shop_name}", shop.name)
    else:
        return MESSAGE_WELCOME_SHOP_SELL.replace("{amount_of_gold}", str(game.player.gold)).replace("{items}",
                                                                                                    item_text).replace(
            "{shop_name}", shop.name)


# dungeon
MESSAGE_DUNGEON_DESC = "You see {description}."
MESSAGE_DUNGEON_MENU = "What do you want to do?\n\n" \
                       "{options}" \
                       "> "
MESSAGE_DUNGEON_ROOM_EMPTY = "You are alone in this room."
MESSAGE_DUNGEON_FIGHT = "You see the following enemies:\n\n" \
                        "{monsters}\n\n" \
                        "You have {health} health.\n" \
                        "Which enemy would you like to attack?\n" \
                        "> "
MESSAGE_DUNGEON_DEFENDING = "{monster_name} attacked you and dealt {damage} damage."
MESSAGE_DUNGEON_ATTACKING = "You attacked {monster_name} and dealt {damage} damage."
MESSAGE_DUNGEON_PLAYER_DIED = "You were killed by {monster_name}."
MESSAGE_DUNGEON_MONSTER_DIED = "{monster_name} died. It dropped {gold_earned} gold."
MESSAGE_DUNGEON_ENEMIES_DEFEATED = "All enemies defeated.\n" + MESSAGE_DUNGEON_ROOM_EMPTY
MESSAGE_DUNGEON_MONSTERS_BLOCKING = "Monsters are blocking your way."

MESSAGE_DUNGEON_CHEST_EMPTY = "The chest is empty."
MESSAGE_DUNGEON_CHEST_REWARD = "You collected {item_name} from the chest."
MESSAGE_DUNGEON_WRONG_MONSTER = "Please input a positive integer between 1 and the number of monsters."


def get_message_dungeon_menu(options):
    options_text = ""
    for option in options:
        key = options.index(option) + 1 if not option == options[len(options) - 1] else 0
        options_text += "  {}) {}\n".format(key, option)
    options_text += "\n"
    return MESSAGE_DUNGEON_MENU.replace("{options}", options_text)


def get_message_dungeon_desc(monsters):
    description = ""
    for i in range(0, len(monsters)):
        if i < len(monsters) - 1:
            if i < len(monsters) - 2:
                description += "a " + monsters[i].name + ", "
            else:
                description += "a " + monsters[i].name + " "
        else:
            description += "and a " + monsters[i].name + " "
    description += "eyeballing you"
    return MESSAGE_DUNGEON_DESC.replace("{description}", description)


def get_message_dungeon_fight(monsters):
    monster_text = ""
    for i in range(0, len(monsters)):
        monster_text += " {}) {:15} ({} HP)\n".format(i + 1, monsters[i].name.title(), monsters[i].health)
    return MESSAGE_DUNGEON_FIGHT.replace("{monsters}", monster_text).replace("{health}", str(game.player.health))


def get_message_defending(monster, damage):
    return MESSAGE_DUNGEON_DEFENDING.replace("{monster_name}", monster.name.title()).replace("{damage}", damage)


def get_message_attacking(monster, damage):
    return MESSAGE_DUNGEON_ATTACKING.replace("{monster_name}", monster.name.title()).replace("{damage}", damage)


def get_message_dungeon_player_died(monster):
    return MESSAGE_DUNGEON_PLAYER_DIED.replace("{monster_name}", monster.name.title())


def get_message_dungeon_monster_died(monster, reward):
    return MESSAGE_DUNGEON_MONSTER_DIED.replace("{monster_name}", monster.name.title()).replace("{gold_earned}", reward)


def get_message_dungeon_chest_reward(item_name):
    return MESSAGE_DUNGEON_CHEST_REWARD.replace("{item_name}", item_name)
