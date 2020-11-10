import random

weapons_list = [
    {'name': 'Club', 'atk': 1, 'defnc': 0, 'weight': 1, 'value': 10, 'location': 'hands'},
    {'name': 'Dagger', 'atk': 1, 'defnc': 0, 'weight': 1, 'value': 10, 'location': 'hands'},
    {'name': 'Greatclub', 'atk': 1, 'defnc': 0, 'weight': 1, 'value': 10, 'location': 'hands'},
    {'name': 'Handaxe', 'atk': 1, 'defnc': 0, 'weight': 1, 'value': 10, 'location': 'hands'},
    {'name': 'Javelin', 'atk': 1, 'defnc': 0, 'weight': 1, 'value': 10, 'location': 'hands'}
]

# weapons_list = [
#     ['Club', 1, 0],
#     ['Dagger', 1, 0],
#     ['Greatclub', 1, 0],
#     ['Handaxe', 1, 0],
#     ['Javelin', 1, 0],
#     ['Hammer', 1, 0],
#     ['Mace', 1, 0],
#     ['Quarterstaff', 1, 0],
#     ['Sickle', 1, 0],
#     ['Spear', 1, 0],
#     ['Crossbow', 1, 0],
#     ['Shortbow', 1, 0],
#     ['Battleaxe', 1, 0],
#     ['Flail', 1, 0],
#     ['Greataxe', 1, 0],
#     ['Greatsword', 1, 0],
#     ['Halberd', 1, 0],
#     ['Lance', 1, 0],
#     ['Longsword', 1, 0],
#     ['Maul', 1, 0],
#     ['Pike', 1, 0],
#     ['Rapier', 1, 0],
#     ['Scimitar', 1, 0],
#     ['Shortsword', 1, 0],
#     ['Trident', 1, 0],
#     ['Warhammer', 1, 0],
#     ['Longbow', 1, 0],
# ]

head_armor_list = [
    ['Ballcap', 0, 1],
    ['Duncecap', 0, 1],
    ['Beanie', 0, 1],
    ['Bowler', 0, 1],
    ['10-Gallon_hat', 0, 1],
    ['Visor', 0, 1],
    ['Space Helmet', 0, 1],
]

body_armor_list = [
    ['Sweatshirt', 0, 1],
    ['Jersey', 0, 1],
    ['Chainmail', 0, 1],
    ['T-shirt', 0, 1],
    ['Wooly_Coat', 0, 1],
    ['Vest', 0, 1],
    ['Space Suit', 0, 1],
]

arm_armor_list = [
   ['Gauntlet', 0, 1],
   ['Brassard', 0, 1],
   ['Vambrace', 0, 1],
   ['Bracers', 0, 1],
   ['Fists', 0, 1],
   ['Grips', 0, 1],
   ['Warfists', 0, 1],
   ['Handguards', 0, 1],
]

leg_armor_list = [
   ['Chausses', 0, 1],
   ['Cuisses', 0, 1],
   ['Greaves', 0, 1],
   ['Poleyn', 0, 1]
]

shoe_list = [
   ['Sabaton', 0, 1],
   ['Solleret', 0, 1],
   ['Greatboots', 0, 1],
   ['Boots', 0 , 1],
   ['Footguards', 0, 1],
   ['Spurs', 0, 1],
   ['Stompers', 0, 1],
   ['Sandals', 0, 1],
   ['Shoes', 0, 1],
]



class Item:
    def __init__(self, name='', atk = 0, defnc = 0, weight=0, value=0, location = ''):
        self.name = name
        self.atk = atk
        self.defnc = defnc
        self.weight = weight
        self.value = value
        self.location = location

    def item_randomizer():
        random_item_type = random.randrange(0,6)
        if random_item_type == 0:
            item_index = random.randrange(len(weapons_list)-1)
            return Item(name = weapons_list[item_index]['name'], 
                        atk = weapons_list[item_index]['atk'],
                        defnc = weapons_list[item_index]['defnc'],
                        location = weapons_list[item_index]['location'])
        elif random_item_type == 1:
            return Item(head_armor_list[random.randrange(len(head_armor_list)-1)][0], location = 'head')
        elif random_item_type == 2:
            return Item(body_armor_list[random.randrange(len(body_armor_list)-1)][0], location = 'body')
        elif random_item_type == 3:
            return Item(arm_armor_list[random.randrange(len(arm_armor_list)-1)][0], location = 'arm')
        elif random_item_type == 4:
            return Item(leg_armor_list[random.randrange(len(leg_armor_list)-1)][0], location = 'leg')
        elif random_item_type == 5:
            return Item(shoe_list[random.randrange(len(shoe_list)-1)][0], location = 'shoe')
        else:
            print("Something went wrong with the range of random when choosing an item")
            return None    
            
    def item_generator(num = 1):
        return_list = []
        for i in range(num):
            return_list.append(Item.item_randomizer())
        return return_list

class Equipment:
    def __init__(self, hands=None, head = None, arm=None, body=None, leg=None, shoe=None):
        self.hands = hands
        self.head = head
        self.arm = arm
        self.body = body
        self.leg = leg
        self.shoe = shoe
    
    def equip_item(self, item, backpack):
        if item.location == 'hands':
            if (self.hands != None):
                backpack.add_item(self.hands)
            self.hands = item
        if item.location == 'head':
            if (self.head != None):
                backpack.add_item(self.head)
            self.head = item
        if item.location == 'arm':
            if (self.arm != None):
                backpack.add_item(self.arm)
            self.arm = item
        if item.location == 'body':
            if (self.body != None):
                backpack.add_item(self.body)
            self.body = item
        if item.location == 'leg':
            if (self.leg != None):
                backpack.add_item(self.leg)
            self.leg = item
        if item.location == 'shoe':
            if (self.shoe != None):
                backpack.add_item(self.shoe)
            self.shoe = item

    def print_equipment(self):
        equipment_list = []
        if self.hands != None:
            equipment_list.append(self.hands)
        if self.head != None:
            equipment_list.append(self.head)
        if self.arm != None:
            equipment_list.append(self.arm)
        if self.body != None:
            equipment_list.append(self.body)
        if self.leg != None:
            equipment_list.append(self.leg)
        if self.shoe != None:
            equipment_list.append(self.shoe)
        if (len(equipment_list) != 0):
            print('\nYour equipped items are:')
            for my_item in equipment_list:
                print(my_item.location + ': ' + my_item.name)
        else:
            print('You have nothing equipped right now.')

class Backpack:

    def __init__(self, item_list=None, name = ''):
        if (item_list == None):
            item_list = []
        self.name = name
        self.item_list = item_list
        self.max_weight = 0
    
    def find_item(self, name):
        for my_item in self.item_list:
            if (my_item.name.lower() == name.lower()):
                return my_item
        return None

    def add_item(self, item_input):
        self.item_list.append(item_input)
        
    def remove_item(self, item_input):
        if (item_input in self.item_list):
            self.item_list.remove(item_input)
            return True
        return False

    def print_content(self):
        if (len(self.item_list) != 0):
            if (len(self.item_list) != 0):
                print('\nYour backpack contents:')
                for my_item in self.item_list:
                    print(my_item.name)
        else:
            print("There are no items in the " + self.name)


    
