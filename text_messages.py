# TODO: Create constants for variable-identifiers

# TODO: Save player in module for easier access


# character creation
MESSAGE_WELCOME_CREATE = "Welcome to P0 Dungeon Quest character creator!\n" \
                         "Enter your name: "

MESSAGE_ASSIGN_POINTS = "You have 100 points to assign to your character.\n" \
                        "Start now to assign those Points to your characters attack, defense and speed."
MESSAGE_ASSIGN_ATTACK = "Attack: "
MESSAGE_ASSIGN_DEFENSE = "Defense: "
MESSAGE_ASSIGN_SPEED = "Speed: "
MESSAGE_NEGATIVE_ASSIGNED = "Please input a positive integer."
MESSAGE_TOO_MANY_POINTS = "Sorry, it seems like you spent more than 100 ability points on your character... " \
                          "Try that again!"

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


# village
MESSAGE_WELCOME_VILLAGE = "Welcome to Prog0 Village!\n" \
                          "What do you want to do?\n" \
                          "  1) Inventory\n" \
                          "  2) Merchant\n" \
                          "  3) Blacksmith\n" \
                          "  4) Druid\n" \
                          "  5) Dungeon\n" \
                          "  6) Save game\n" \
                          "  0) Quit game\n\n" \
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
MESSAGE_NOTHING_DONE = "Nothing done."
MESSAGE_ITEM_NOT_EXISTING = "Item does not exist."  #
MESSAGE_ITEM_USED = "You used {item_name}.\n" \
                    "It increased your {influenced_attribute} by {amount}.\n" \
                    "You now have {new_stat_amount} {influenced_attribute}."
MESSAGE_ITEM_DROPPED = "You dropped {item_name}."

MESSAGE_ITEM_NOT_USABLE = "You cannot use this item."


def get_message_inventory_welcome(items, player):
    item_text = ""
    for item in items:
        item_desc = "({:+d} {} when {})".format(item.amount, item.influenced_stat,
                                                "held" if item.passive_effect else "used")
        item_text += "  * {:20} {}\n".format(item.name.capitalize(), item_desc)
    return MESSAGE_WELCOME_INVENTORY.replace("{items}", item_text).replace("{char_name}", player.name)


def get_message_item_used(item, player):
    # TODO: Exception for stat not existing
    new_stat = str(getattr(player, str(item.influenced_stat).lower()))
    return MESSAGE_ITEM_USED.replace("{item_name}", item.name.capitalize()) \
        .replace("{influenced_attribute}", item.influenced_stat) \
        .replace("{new_stat_amount}", new_stat) \
        .replace("{amount}", str(item.amount))


def get_message_use_or_drop(item):
    return MESSAGE_USE_OR_DROP.replace("{item_name}", item.name.capitalize())


def get_message_item_dropped(item):
    return MESSAGE_ITEM_DROPPED.replace("{item_name}", item.name.capitalize())


MESSAGE_WELCOME_MERCHANT = "Welcome to the merchant!\n" \
                           "You have {amount_of_gold} gold. This is what I would pay for your items:\n\n" \
                           "{items}\n" \
                           "Type 'quit' or the name of the item you want to sell.\n" \
                           "> "
MESSAGE_ITEM_NOT_OWNED = "You do not possess a {item_name}."
MESSAGE_ITEM_SOLD = "You have chosen {item_name}.\n" \
                    "You now have {amount_of_gold} gold left.\n" \
                    "Removed item from inventory."
MESSAGE_NOTHING_TO_SELL = "Sorry, you have nothing to sell.\n" \
                          "Thanks for visiting!"
MESSAGE_ITEM_BOUGHT = "You have chosen {item}.\n" \
                      "You have {amount_of_gold} gold left."
MESSAGE_ITEM_NOT_SELLING = "I do not sell '{item_name}'."
MESSAGE_NOT_ENOUGH_GOLD = "Not enough gold."


def get_message_welcome_merchant(player):
    item_text = ""
    for item in player.inventory:
        item_text += "  * {:20} for {:4d} gold\n".format(item.name.capitalize(), int(item.price * 0.5))
    return MESSAGE_WELCOME_MERCHANT.replace("{amount_of_gold}", str(player.gold)).replace("{items}", item_text)


def get_message_item_not_owned(item_name):
    return MESSAGE_ITEM_NOT_OWNED.replace("{item_name}", item_name.title())


def get_message_item_sold(item, player):
    return MESSAGE_ITEM_SOLD.replace("{item_name}", item.name.capitalize()).replace("{amount_of_gold}", str(player.gold))

def get_message_item_bought(item, player):
    return MESSAGE_ITEM_BOUGHT.replace("{item}", item.name.capitalize()).replace("{amount_of_gold}", str(player.gold))

def get_message_item_not_selling(item_name):
    return MESSAGE_ITEM_NOT_SELLING.replace("{item_name}", item_name)


MESSAGE_WELCOME_BLACKSMITH = "Welcome to the blacksmith\n" \
                             "You have {amount_of_gold} gold to spend. This is what I'm selling:\n\n" \
                             "{items}\n" \
                             "Type 'quit' or the name of the item you want to buy.\n" \
                             "> "

# def get_message_welcome_shop(shop_inventory, player):
#     item_text = ""
#     for item in shop_inventory
#         item_text +=

def get_message_welcome_blacksmith(shop_inventory, player):
    item_text = ""
    for item in shop_inventory:
            item_text += "  * {:20} for {:4d} gold ({:+d} {} when held)\n".format(item.name.capitalize(),
                                                                                  item.price, item.amount,
                                                                                  item.influenced_stat)
    return MESSAGE_WELCOME_BLACKSMITH.replace("{amount_of_gold}", str(player.gold)).replace("{items}", item_text)

MESSAGE_WELCOME_DRUID = "Welcome to the druid\n" \
                             "You have {amount_of_gold} gold to spend. This is what I'm selling:\n\n" \
                             "{items}\n" \
                             "Type 'quit' or the name of the item you want to buy.\n" \
                             "> "

def get_message_welcome_druid(shop_inventory, player):
    item_text = ""
    for item in shop_inventory:
            item_text += "  * {:20} for {:4d} gold ({:+d} {} when used)\n".format(item.name.capitalize(),
                                                                                  item.price, item.amount,
                                                                                  item.influenced_stat)
    return MESSAGE_WELCOME_DRUID.replace("{amount_of_gold}", str(player.gold)).replace("{items}", item_text)

#
# def get_message_item_list(style, player):
#     item_text = ""
#     for item in player.inventory:
#         item_text += "  * {:20} ".format(item.name.capitalize())
#         item_effect = "({:+d} {} when {})".format(item.amount, item.influenced_stat,
#                                                   "held" if item.passive_effect else "used")
#         if style == ITEM_LIST_INVENTORY:


#dungeon
MESSAGE_DUNGEON_DESC = "You see {description}."
MESSAGE_DUNGEON_MENU = "What do you want to do?\n\n" \
                       "  1) Inventory\n" \
                       "  2) Look Around\n" \
                       "  3) Attack\n" \
                       "  4) Open chest\n" \
                       "  5) Move\n" \
                       "  0) Run away (leave dungeon)\n\n" \
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


def get_message_dungeon_desc(monsters):
    description = ""
    for i in range(0, len(monsters)):
        if i < len(monsters)-1:
            if i < len(monsters)-2:
                description += "a " + monsters[i].name + ", "
            else:
                description += "a " + monsters[i].name + " "
        else:
            description += "and a " + monsters[i].name + " "
    description += "eyeballing you"
    return MESSAGE_DUNGEON_DESC.replace("{description}", description)

def get_message_dungeon_fight(monsters, player):
    monster_text = ""
    for i in range(0, len(monsters)):
        monster_text += " {}) {:15} ({} HP)\n".format(i+1, monsters[i].name.title(), monsters[i].health)
    return MESSAGE_DUNGEON_FIGHT.replace("{monsters}", monster_text).replace("{health}", str(player.health))

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

# item list styles
ITEM_LIST_INVENTORY = "inventory"
ITEM_LIST_MERCHANT = "merchant"
ITEM_LIST_BLACKSMITH = "blacksmith"
ITEM_LIST_DRUID = "druid"

ITEM_LIST_STYLES = {
    ITEM_LIST_INVENTORY: MESSAGE_WELCOME_INVENTORY,
    ITEM_LIST_MERCHANT: MESSAGE_WELCOME_MERCHANT,
    # ITEM_LIST_BLACKSMITH: MESSAGE_WELCOME_BLACKSMITH
    # ITEM_LIST_DRUID: MESSAGE_WELCOME_DRUID
}
