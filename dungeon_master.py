from random import Random
import characters
from characters import EnemyStatus, enemy_generator
import roomstuff
import items
import random
import os

  



class Dungeon_Master:

    def __init__(self):
        self.game_map = None
        self.player = None
        self.enemies = []
        # self.items = None   # probably no longer used, keeping commented just in case
        self.current_room = None
        
    def clear_terminal(self): 
        if os.name == 'nt':  #windows machines
            _ = os.system('cls') 
        else:   #posix/mac machines
            _ = os.system('clear') 


    def move_player(self, direction, room):

        '''
        Moves player to a room.

        Parameters:

            direction:  direction to move player
            room:  room to move player to

        Returns:
            Nothing
        ''' 


        if (direction == 'north') and (room.north_exit != None):
            return room.north_exit  
        elif (direction == 'east') and (room.east_exit != None):
            return room.east_exit
        elif (direction == 'south') and (room.south_exit != None):
            return room.south_exit
        elif (direction == 'west') and (room.west_exit != None):
            return room.west_exit
        else:
            print('Your player did not move any direction.  Please choose a valid direction.')
            return room

    def print_current_room_info(self):

        '''
        Prints the current room info, including available movements, items, enemies, and the player.

        Parameters:
            No parameters

        Returns:
            No returns
        ''' 
        this_room = self.get_current_room()
        print('')
        print('You are now in the ' + this_room.room_content.room_name)
        print(this_room.room_content.description)

        # print(this_room.room_content.description)

        output_string = ''
        for item in this_room.room_content.items:
            if (item != None):
                if (output_string == ''):
                    output_string += 'Items in this room: \n' 
                output_string += (item.name + ' ' + item.location + '\n')
        if (output_string != ''):
            print(output_string)
        else:
            print('There are no items in the room.\n')

        output_string = ''
        for enemy in this_room.room_content.enemies: 
            if (enemy != None):
                if (output_string == ''):
                    output_string += 'Enemies in room:\n'
                output_string += (enemy.name + ' the ' + enemy.type + ' (' + enemy.backpack.name + ')\n')
        if (output_string != ''):
            print(output_string)
        else:
            print('There are no enemies in the room.\n')

        if (this_room.room_content.chest != None):
            print('There is a ' + this_room.room_content.chest.name + ' in this room.\n')

        available_movements = []
        if this_room.north_exit != None:
                available_movements.append('north')
        if this_room.east_exit != None:
                available_movements.append('east')
        if this_room.south_exit != None:
                available_movements.append('south')
        if this_room.west_exit != None:
                available_movements.append('west')
        if (len(available_movements) == 0):
            print('There are no directions avabilable to move.  You''re stuck here for eternity.  Sorry about that, that probably wasn\'t supposed to happen.\n')
        else:
            print('Available exits are: ' + str(available_movements))

    def request_and_handle_player_action(self):

        # change to grab [item] other ?
        # action [target] modifier

        '''
        Handles requesting and taking action on player input.  
        
        Includes:
        
        Movement to different rooms, dropping items (in current room and in current room's chest), attacking enemies, showing player inventory, and showing chest contents.

        Parameters:
            No parameters

        Returns:
            No returns
        ''' 
        action = self.player.get_action()
        action_parsed = action.split()
        self.clear_terminal()
        # TBD can we shorten commands (e.g. 'nor'/'no'/'n' instead of 'north')
        # TBD: kill goblin2 (the 2 is indexing the 2nd goblin in the room...also applies to items/dropping...)
        # something like...('north'.startswith(action_parsed[0].lower()))...maybe???

        if (action_parsed[0].lower() == 'north') or (action_parsed[0].lower() == 'east') or (action_parsed[0].lower() == 'south') or (action_parsed[0].lower() == 'west'):
            previous_room = self.get_current_room()
            next_room = self.move_player(action_parsed[0].lower(), previous_room)
            previous_room.room_content.player = None
            next_room.room_content.player = self.player

        elif (len(action_parsed) > 1) and ((action_parsed[0].lower() == 'take') or (action_parsed[0].lower() == 'grab') or (action_parsed[0].lower() == 'hold')):
            this_room = self.get_current_room()
            item_found = False
            if (len(action_parsed) < 3): #not looking in chest
                for item in this_room.room_content.items:
                    if (item != None) and (item.name.lower() == action_parsed[1].lower()):
                        self.player.backpack.add_item(item)
                        this_room.room_content.items.remove(item)
                        # item = None # <-- this is a memory leak...craig's minor memory leak...should be replaced by something like above line
                        item_found = True
                        break
            elif (action_parsed[2] == this_room.room_content.chest.name):
                for item in this_room.room_content.chest.item_list:
                    if (item != None) and (item.name.lower() == action_parsed[1].lower()):
                        self.player.backpack.add_item(item)
                        this_room.room_content.chest.remove_item(item)
                        # item = None # <-- this is a memory leak...craig's minor memory leak...should be replaced by something like above line
                        item_found = True
                        break
            if item_found == False:
                print("There is no item by that name")

        elif (len(action_parsed) > 1) and ((action_parsed[0].lower() == 'drop') or (action_parsed[0].lower() == 'place') or (action_parsed[0].lower() == 'put')):
            this_room = self.get_current_room()
            this_item = self.player.backpack.find_item(action_parsed[1].lower())
            
            if (this_item != None):
                self.player.backpack.remove_item(this_item)
                if (len(action_parsed) < 3): #not putting in chest
                    this_room.room_content.items.append(this_item)
                elif (action_parsed[2] == this_room.room_content.chest.name):
                    this_room.room_content.chest.add_item(this_item)
            else:
                print("You don't have this item in your backpack") 

        elif (len(action_parsed) > 1) and ((action_parsed[0].lower() == 'equip') or (action_parsed[0].lower() == 'wield') or (action_parsed[0].lower() == 'wear')):
            this_item = self.player.backpack.find_item(action_parsed[1].lower())
            if (this_item != None):
                self.player.equipment.equip_item(this_item, self.player.backpack)
                self.player.backpack.remove_item(this_item)
            else:
                print("You don't have this item in your backpack")

        elif (len(action_parsed) > 1) and ((action_parsed[0].lower() == 'kill') or (action_parsed[0].lower() == 'attack') or (action_parsed[0].lower() == 'murder')):
            this_room = self.get_current_room()           
            enemy_found = False
            for enemy in this_room.room_content.enemies:
                if (enemy != None) and (enemy.name.lower() == action_parsed[1].lower()):
                    enemy_status, items_dropped = enemy.subtract_hp(this_room.room_content.player.atk)
                    if enemy_status == EnemyStatus.DEAD:
                        this_room.room_content.items = [y for x in [this_room.room_content.items, items_dropped] for y in x]
                    enemy_found = True
                    print("The enemy has " + str(enemy.hp) + " hp.")
                    break
            if enemy_found == False:
                print("There is no enemy by that name")

        elif (action_parsed[0].lower() == 'inventory') or (action_parsed[0].lower() == 'i') or (action_parsed[0].lower() == 'items'):
            self.player.backpack.print_content()
            self.player.equipment.print_equipment()


        elif (action_parsed[0].lower() == 'look') or (action_parsed[0].lower() == 'search'):
            this_room = self.get_current_room()

            if (action_parsed[1].lower() == this_room.room_content.chest.name):
                output_string = ''
                for item in this_room.room_content.chest.item_list:
                    if (item != None):
                        if (output_string == ''):
                            output_string += 'Items in the ' + this_room.room_content.chest.name + ' in this room: \n'
                        output_string += ((item.name) + '\n')
                if (output_string !=''):
                    print(output_string)
                else:
                    print("There are no items in the " + this_room.room_content.chest.name + " in this room.")
            else:
                print('Nothing here by that name')
        
        return action
        
    def create_enemies(self):
        self.enemies = characters.enemy_generator()        

    def create_player(self):
        self.player = characters.Player(backpack = items.Backpack(name = 'backpack'), equipment= items.Equipment())

    def get_current_room(self):
        '''
        Gets the current room to be able to be called from a pointer

        Parameters:
            No parameters

        Returns:
            Current room
        ''' 
        return self.game_map.bfs_player(self.game_map.map_entrance)
