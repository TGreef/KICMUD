import dungeon_master
import roomstuff

# a, b, c = ['A', 'B', 'C']
# print(a)
# print(b)
# print(c)

# a, b, *c = (1, 2, 3, 4, 5, 6)
# print(a)
# print(b)
# print(c)

# a, b, *_ = (1, 2, 3, 4, 5)
# print(a)
# print(b)

# a, b, *_, d = (1, 2, 3, 4, 5)
# print(a)
# print(b)
# print(d)

# --------------------------------------------------------------------------------

# condition = True

# if condition:
#     x = 1
# else:
#     x = 0
# print (x)

# LINES 25 THROUGH 29 IS IS THE SAME AS 33 AND 34:

# x = 1 if condition else 0
# print (x)

# --------------------------------------------------------------------------------


# If we have 2 lists that correspond to one another.  We want to loop through the lists at the same time and print the corresponding names with the hero names.

# We COULD use enumerate to grab the index we're currently on, and then use that to access the same index from the other group:

# names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
# heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

# for index, name in enumerate(names):
#     hero = heroes[index]
#     print(f'{name} is actually {hero}')

# BUT instead, we can use the ZIP function.  We can add even a 3rd list.  ZIP will stop after the sho list is done.  For "longest list", you need to import itertools.

# names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
# heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
# universes = ['Marvel', 'DC', 'Marvel', 'DC']

# for name, hero, universe in zip(names, heroes, universes):
#     print(f'{name} is actually {hero} from {universe}')

# ----------------------------------------------------------------------------------

# We can dynamically add attributes and values to the objects of a class:

# class Person():
#     pass
# person = Person()
# person.first = 'Tom'
# person.last = 'Greef'
# print(person.first)
# print(person.last)

# What if the attribute we want to set, is the value of another variable?

# class Person():
#     pass
# person = Person()
# first_key = 'first'
# first_val = 'Tom'
# last_key = 'last'
# last_val = 'Greef'
# setattr(person, 'first', 'Tom',)
# setattr(person, 'last', 'Greef')
# print(person.first)
# print(person.last)


# Unlike setting attributes directly, using setattr, we can use variables!

# class Person():
#     pass
# person = Person()
# first_key = 'first'
# first_val = 'Tom'
# setattr(person, first_key, first_val)
# print(person.first)

# If we want to GET BACK a value, we can use getattr:

# class Person():
#     pass
# person = Person()
# first_key = 'first'
# first_val = 'Tom'
# setattr(person, first_key, first_val)
# first = getattr(person, first_key)
# print(first)

#--------------------------------DECORATORS (@things)------------------------------
#----------------------------------STATIC METHODS-----------------------------------
#-------------------------------------AND-------------------------------------------
#----------------------------------STATIC ATTRIBUTES--------------------------------
# class Person:
#     number_of_people = 0
#     gravity = -9.8

#     def __init__(self, name):
#         self.name = name
#         Person.add_person()

#     @classmethod
#     def get_number_of_people(cls):
#         return cls.number_of_people

#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1

# p1 = Person("tom")
# p2 = Person("craig")
# print(Person.get_number_of_people())

# -------------------------------------------------------------

# this is a generator, similar to method, but it remembers its state between executions (yield instead of return)
# def my_generator(num):
#     while (True):
#         yield num
#         num += 1

# g = my_generator(5)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# -------------------------------------------------------------

# def my_method(my_var = ''):
#     my_var.startswith('bong')
#     my_var.
#     my_var.



# if "n" in input():
#     print('THIS WORKS')
# else:
#     print('STOP USING PRINT LINES AS CODES')
# # find

# if input() in 'north':
#     print('THIS WORKS')
# else:
#     print('STOP USING PRINT LINES AS CODES')
# # rfind
# # startswith


# boople = (my_val, my_val2)

# sdfg = (my_val)

#  -----------------INHERITANCE--------------  
# class Animal:
#     def __init__(self, name = ''):
#         self.name = name
#         self.weight = 0

#     def speak(self):
#         print('i\'m speaking')

#     def eat(self):
#         print('yum')

# class Dog(Animal):
#     def __init__(self, name = ''):
#         super().__init__(name)
#         self.has_snout = True
#         self.num_legs = 4

#     def speak(self):
#         print('bark')
    
# class Terrier(Dog):
#     def __init__(self, name=''):
#         super().__init__(name)
#         self.hair_color = 'white'

#     def eat(self):l
#         print('nom nom')

# my_dog = Terrier('fido')

# my_dog.speak()
# my_dog.eat()
# print(my_dog.weight)

# class Enemy:
#     pass

# class Boss(Enemy):
#     pass

# -----------------------------------------------------

# what about the "curses" function standard lib?

#-------------------------------------------------------

action = input()
action_parsed = action.lower().split()
player_action_verb = action_parsed[0]
item_target = ' '.join([str(word) for word in action_parsed[1:-1]])
player_action_target = action_parsed[-1]

# action target
# action target modifier
# action target1 target2
# action target1 target2 modifier

# if len(action_parsed) >=3:
#     print('There are 3 or more words')
# elif len(action_parsed) ==2:
#     print('There are 2 words')
# else:
#     print('There are 0 or 1 words')
print(player_action_verb)
print(item_target)
print(player_action_target)
print(action_parsed)

# print(action_parsed[0], action_parsed[-1])

# print(action_popped1)
# print(action_popped2)

# res = len(action.split())
# print(res)

# this_room = self.get_current_room()

# if ('north') or ('south') in action_parsed:
#     print('THIS REMAINS THE SAME AS PREVIOUSLY')
# if len(action_parsed) > 1:

#     item_target = ' '.join([str(word) for word in action_parsed_poppable])
#     if item_target != '':  #if there are more than 2 words in the action parsed
#         if player_action_verb == 'take' or 'grab' or 'hold':  #if they want to hold the item
#             item_found = False
#             for item in this_room.room_content.chest.item_list: #for every item in this room's chest
#                 if (item != None) and (item.name.lower() == item_target.lower()):  #if there's an item, and it matches the name of the item (MULTI WORDED CAPABLE)
#                     self.player.backpack.add_item(item)
#                     this_room.room_content.chest.remove_item(item)
#                     # item = None # <-- this is a memory leak...craig's minor memory leak...should be replaced by something like above line
#                     item_found = True
#                     break
#             if item_found == False:
#                 print("There is no item by that name")

#     elif
#         print('There is no item target.  This is used for 2-word requests:  hold club, kill goblin, NOTE MULTI WORDED ITEMS OR MONSTERS BREAK THIS)
   




