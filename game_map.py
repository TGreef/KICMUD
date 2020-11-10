import roomstuff
import characters
import dungeon_master
import items
import random

class Map:

    def __init__(self, enemies = None):  #enemies is a pramater only, not being "saved" into Map anywhere.
        '''
        Initializer of the Map class

        Attributes:
            enemies(list): Our list of enemies

        Returns:
            No returns
        ''' 
        if (enemies == None):
            enemies = []
        self.map_entrance = self.create_map(enemies)

    
    def create_map(self, enemies):

        '''
        Populates the content inside rooms with items/enemies/players/things from RoomContent.

        Parameters:
            enemies(list):  Our list of enemies

        Returns:
            Manually-set entrance of the map (In this case:  top-left)
        ''' 
        #  THE BELOW CODE IS FOR THE DONUT

        # self.create_enemies()
        top_left_room_content = roomstuff.RoomContent('top left room')
        top_left_room_content.items.append(items.Item.item_randomizer())
        top_left_room_content.items.append(items.Item.item_randomizer())
        top_left_room_content.description = "The faint smell of elderberries lies in the distance...\n"
        top_center_room_content = roomstuff.RoomContent('top center room', [enemies[3]])
        top_right_room_content = roomstuff.RoomContent('top right room', [enemies[2]])
        middle_right_room_content = roomstuff.RoomContent('center right room')
        bottom_right_room_content = roomstuff.RoomContent('bottom right room')
        bottom_center_room_content = roomstuff.RoomContent('bottom center room')
        bottom_left_room_content = roomstuff.RoomContent('bottom left room')
        middle_left_room_content = roomstuff.RoomContent('center left room', enemies = [enemies[7]], chest=items.Backpack(name='chest'))
        middle_left_room_content.items.append(items.Item.item_randomizer())
        middle_left_room_content.chest.add_item(items.Item.item_randomizer())
        middle_left_room_content.description = "As you entered, you spilled bongwater on the floor, you oaf!  Watch your clodhoppers.\n The previously-sweet smell of elderberries is no-more."
        #THE BELOW CODE IS FOR THE CROSS


        # topmost_room_content = roomstuff.RoomContent('Top of Cross (AKA: ORIGIN)', enemy_list[0], True)
        # middle_of_top_room_content = roomstuff.RoomContent('Middle of the Top of the cross', enemy_list[1], True)
        # center_of_cross_room_content = roomstuff.RoomContent('Center of the cross', enemy_list[2])
        # middle_of_right_room_content= roomstuff.RoomContent('Middle of the Right of the cross', enemy_list[3],False,True)
        # rightmost_room_content =roomstuff.RoomContent('Rightmost of the cross', enemy_list[4], True)
        # middle_of_bottom_room_content = roomstuff.RoomContent('Middle of the Bottom of the cross', enemy_list[5])
        # bottommost_room_content = roomstuff.RoomContent('Bottommost of the cross', enemy_list[6])
        # middle_of_left_room_content = roomstuff.RoomContent('Middle of the Left of the cross', enemy_list[7])
        # leftmost_room_content = roomstuff.RoomContent('Leftmost of the cross', enemy_list[8], True)


        #  THIS SETS THE temporary POINTERS FOR THE INSTANTIATED INSTANCES OF THE ROOMNODE OBJECTS OF THE CROSS (maybe worded right?)

        # topmost = roomstuff.RoomNode(topmost_room_content)    
        # middle_of_top = roomstuff.RoomNode(middle_of_top_room_content)
        # center_of_cross = roomstuff.RoomNode(center_of_cross_room_content)
        # middle_of_right = roomstuff.RoomNode(middle_of_right_room_content)
        # rightmost = roomstuff.RoomNode(rightmost_room_content)
        # middle_of_bottom = roomstuff.RoomNode(middle_of_bottom_room_content)
        # bottommost = roomstuff.RoomNode(bottommost_room_content)
        # middle_of_left = roomstuff.RoomNode(middle_of_left_room_content)
        # leftmost = roomstuff.RoomNode(leftmost_room_content)


        # UNCOMMENT THIS BELOW FOR THE DONUT

        top_left = roomstuff.RoomNode(top_left_room_content)        
        top_center = roomstuff.RoomNode(top_center_room_content)
        top_right = roomstuff.RoomNode(top_right_room_content)
        middle_right = roomstuff.RoomNode(middle_right_room_content)
        bottom_right = roomstuff.RoomNode(bottom_right_room_content)
        bottom_center = roomstuff.RoomNode(bottom_center_room_content)
        bottom_left = roomstuff.RoomNode(bottom_left_room_content)
        middle_left = roomstuff.RoomNode(middle_left_room_content)

        # self.game_map = roomstuff.GameMap()
        # self.game_map.map_entrance = top_left    


        #THE CODE BELOW IS FOR THE CROSS WITH 9 SQUARES IN IT (ALL SIDES EQUAL LENGTH - PERFECT T)

        # topmost.south_exit = middle_of_top
        # middle_of_top.north_exit = topmost
        # middle_of_top.south_exit = center_of_cross
        # center_of_cross.north_exit = middle_of_top
        # center_of_cross.east_exit = middle_of_right
        # center_of_cross.south_exit = middle_of_bottom
        # center_of_cross.west_exit = middle_of_left
        # middle_of_right.west_exit = center_of_cross
        # middle_of_right.east_exit = rightmost
        # rightmost.west_exit = middle_of_right
        # middle_of_bottom.north_exit = center_of_cross
        # middle_of_bottom.south_exit = bottommost
        # bottommost.north_exit = middle_of_bottom
        # middle_of_left.east_exit = center_of_cross
        # middle_of_left.west_exit = leftmost
        # leftmost.east_exit = middle_of_left
        # -----------------------------------------------------------------------

        # THIS IS THE CODE FOR A DONUT SHAPED MAP WITH 8 SQUARES (HOLE IN THE MIDDLE)

        top_left.east_exit = top_center         
        top_left.south_exit = middle_left
        top_center.west_exit = top_left
        top_center.east_exit = top_right
        top_right.west_exit = top_center
        top_right.south_exit = middle_right
        middle_right.north_exit = top_right
        middle_right.south_exit = bottom_right
        bottom_right.north_exit = middle_right
        bottom_right.west_exit = bottom_center
        bottom_center.east_exit = bottom_right
        bottom_center.west_exit = bottom_left
        bottom_left.east_exit = bottom_center
        bottom_left.north_exit = middle_left
        middle_left.south_exit = bottom_left
        middle_left.north_exit = top_left    
        #-------------------------------------------------------------------

        #  THIS WAS OUR ORIGINAL CODE FOR A 4-ROOM SQUARE
        # top_left.south_exit = bottom_left     
        # bottom_left.east_exit = bottom_right
        # bottom_right.north_exit = top_right
        # top_right.west_exit = top_left

        return top_left
    
    def bfs_player(self, entry_node):
        visited_nodes = []
        search_nodes = []
        return self.bfs_player_recursion(entry_node, visited_nodes, search_nodes)

    def bfs_player_recursion(self, node, my_visited_nodes, my_search_nodes):
        if (node == None): # i dont think this should ever happen (defensive programming)
            return None
        # print(node.room_content.room_name)
        if (node.room_content.player != None):
            return node
        my_visited_nodes.append(node)
        if (node.north_exit != None) and (not node.north_exit in my_visited_nodes) and (not node.north_exit in my_search_nodes):
            my_search_nodes.append(node.north_exit)
        if (node.east_exit != None) and (not node.east_exit in my_visited_nodes) and (not node.east_exit in my_search_nodes):
            my_search_nodes.append(node.east_exit)
        if (node.west_exit != None) and (not node.west_exit in my_visited_nodes) and (not node.west_exit in my_search_nodes):
            my_search_nodes.append(node.west_exit)
        if (node.south_exit != None) and (not node.south_exit in my_visited_nodes) and (not node.south_exit in my_search_nodes):
            my_search_nodes.append(node.south_exit)    
        if (len(my_search_nodes) != 0):
            return self.bfs_player_recursion(my_search_nodes.pop(0), my_visited_nodes, my_search_nodes)  #this adds it to the queue

    def bfs_list_map(self):
        visited_nodes = []
        search_nodes = []
        return_list = []
        return self.bfs_map_recursion(self.game_map.map_entrance, visited_nodes, search_nodes, return_list)

    def bfs_map_recursion(self, node, my_visited_nodes, my_search_nodes, return_list):
        if (node == None):
            return None
        return_list.append(node)
        my_visited_nodes.append(node)
        if (node.north_exit != None) and (not node.north_exit in my_visited_nodes) and (not node.north_exit in my_search_nodes):  #if the north exit exists, and it's not in my_visited_notes, and not in my_search, append it to my_search
            my_search_nodes.append(node.north_exit)
        if (node.east_exit != None) and (not node.east_exit in my_visited_nodes) and (not node.east_exit in my_search_nodes):
            my_search_nodes.append(node.east_exit)
        if (node.west_exit != None) and (not node.west_exit in my_visited_nodes) and (not node.west_exit in my_search_nodes):
            my_search_nodes.append(node.west_exit)
        if (node.south_exit != None) and (not node.south_exit in my_visited_nodes) and (not node.south_exit in my_search_nodes):
            my_search_nodes.append(node.south_exit)
        
        if (len(my_search_nodes) != 0):  #if the length of the node list to be searched isn't 0, with attributes: and "return list" WHAT IS THAT?
            return self.bfs_map_recursion(my_search_nodes.pop(0), my_visited_nodes, my_search_nodes, return_list)
        
        return return_list
    
    def dijkstra(self, start_node, search_list = [], shortest_dict = {}):

        something_changed = False
        if (len(shortest_dict) == 0):
            for node in self.bfs_list_map():  # this probably isnt necessary, can probably be built on the fly
                shortest_dict[node] = []
            shortest_dict[start_node].append(start_node)
            something_changed = True
        else:
            entry_list = []
            if (start_node.north_exit != None):
                entry_list.append(start_node.north_exit)
            if (start_node.south_exit != None):
                entry_list.append(start_node.south_exit)
            if (start_node.east_exit != None):
                entry_list.append(start_node.east_exit)
            if (start_node.west_exit != None):
                entry_list.append(start_node.west_exit)
            for other_node in entry_list:
                length_to_self = len(shortest_dict[start_node])
                length_to_other = len(shortest_dict[other_node])
                length_to_self_thru_other = length_to_other + 1
                if ((length_to_other > 0) and ((length_to_self == 0) or (length_to_self_thru_other < length_to_self))):
                    shortest_dict[start_node] = []
                    for entry in shortest_dict[other_node]:
                        shortest_dict[start_node].append(entry)
                    shortest_dict[start_node].append(start_node)
                    something_changed = True
        
        if (something_changed == True):
            if (start_node.north_exit != None):
                search_list.append(start_node.north_exit)
            if (start_node.south_exit != None):
                search_list.append(start_node.south_exit)
            if (start_node.east_exit != None):
                search_list.append(start_node.east_exit)
            if (start_node.west_exit != None):
                search_list.append(start_node.west_exit)
        
        if (len(search_list) > 0):
            return self.dijkstra(search_list.pop(0), search_list, shortest_dict)
        else:
            return shortest_dict
            
# recursion length = 0    Queue:  Get there first, dealt with first
# recursion length = 1    Stack:  Get there first, dealt with last.
# recursion length = 2
# recursion length = 3
# recursion length = 4
# recursion length = 5
# recursion length = 6