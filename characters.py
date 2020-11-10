
from random import randrange
import items
from items import Backpack


monster_name_list = [
    "Kimonnaltev",
    "Sarind",
    "Borgart",
    "Raxxro",
    "Gorgine",
    "Aregory",
    "Petha",
    "Mothlen",
    "Avirge",
    "Phary",
    "Ssicha",
    "Karolynth",
    "Carolax",
    "Thel",
]

monster_type_list = [
    "Elder Dragon",
    "Goblik",
    "Hag",
    "Imp",
    "Kraken",
    "Ogre",
    "Sea Serpent",
    "Witch",
    "Wraith",
    "Wurm",
    "Wyvern",
    "Basilisk",
    "Griffin",
    "Mummy",
]

directions = [
    "North",
    "South",
    "East",
    "West",
]

from enum import Enum
class EnemyStatus(Enum):
    ALIVE = 0
    DEAD = 1


def enemy_generator():
    return_list = []
    for i in range(10):
        return_list.append(Enemy(monster_name_list[i],monster_type_list[i], backpack = items.Backpack(name = 'satchel')))
        return_list[i].backpack.add_item(items.Item.item_randomizer())
    return return_list

class Being:
    def __init__(self, name='', hp=1, atk=1, defnc=1, backpack=None, equipment=None):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defnc = defnc
        self.backpack = backpack
        self.equipment = equipment
    
    def subtract_hp(self, incoming_atk):
        self.hp = self.hp - (100*(incoming_atk / self.defnc))
        phat_loot = []
        enemy_status = EnemyStatus.ALIVE
        if (self.hp <= 0):
            phat_loot = self.death()
            enemy_status = EnemyStatus.DEAD
        return (enemy_status, phat_loot)

    def death(self):
        return_list = []
        if (len(self.backpack.item_list) != 0):
            for my_item in self.backpack.item_list:
                self.backpack.remove_item(my_item)
                return_list.append(my_item)
        return return_list
        

class Enemy(Being):
    def __init__(self, name='', enemy_type='', hp=100, atk=100, defnc=100, backpack=None, equipment=None):
        super().__init__(name, hp, atk, defnc, backpack, equipment)
        self.type = enemy_type
    
class Player(Being):
    def __init__(self, name='Tom', hp=100, atk=50, defnc=100, backpack=None, equipment=None):
        super().__init__(name, hp, atk, defnc, backpack, equipment)

    def get_action(self):
        return input()
