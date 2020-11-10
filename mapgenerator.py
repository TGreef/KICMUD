import random
# a starting room needs at least 1 exit
# every exit of a room needs to have that exit room to have the opposite direction as at least 1 available exit.  (room1_available_exits = east  -  room2_available_exits = west)
#
# could encase in a while loop that has "while # of total rooms <= desired maximum and >= desired minimum"  
#  ^^^^^^^^ ***THIS WONT WORK, BECAUSE THE WAY WE HAVE IT CURRENTLY, I BELIEVE IT REQUIRES A  RANDOM NUMBER OF ROOMS TO BE SET FIRST, THEN POPULATE ALL THE ROOMS, THEN WE CAN CONNECT THEM FROM THERE.

#How to potentially connect them:  Imposssible for my math-dumb mind.  See desktop diagram of math sadness.



# class generate_map:
    # def __init__(self, first_room, previous)
# total_num_of_rooms = 0
# while total_num_of_rooms >= 4 and <= 11:

#    Dungeon_Master.create_enemies()
#         room1content = roomstuff.RoomContent('Name here', self.enemies(random_number_in_enemy_list_from_self.enemies))
#         room1populated = roomstuff.RoomNode(room1content)
#         Dungeon_Master.room_list.append(room1populated)
#         Dungeon_Master.game_map = roomstuff.GameMap()
#         Dungeon_Master.game_map.map_entrance = room1populated

# MAP_ARRAY = [
#     ['0','0','0','0','0','0','0','0','0','0'],
#     ['0','1','1','1','1','0','0','0','0','0'],
#     ['0','1','1','1','1','0','0','0','0','0'],
#     ['0','1','1','1','1','0','0','0','0','0'],
#     ['0','0','0','1','0','0','0','0','0','0'],
#     ['0','0','0','1','0','0','0','0','0','0'],
#     ['0','0','1','1','1','1','1','1','1','0'],
#     ['0','0','1','1','1','1','1','1','1','0'],
#     ['0','0','1','1','1','1','1','1','1','0'],
#     ['0','0','0','0','0','0','0','0','0','0']
# ]

# map_array = [
#     ['0','0','0','0','0','0','0','0','0','0'],
#     ['0','0','0','0','0','0','0','0','0','0'],
#     ['0','0','0','0','0','0','0','0','0','0'],
#     ['0','0','0','0','0','0','0','0','0','0'],
#     ['0','0','0','0','0','0','0','0','0','0'],
#     ['0','0','0','0','0','0','0','0','0','0'],
#     ['0','0','0','0','0','0','0','0','0','0'],
#     ['0','0','0','0','0','0','0','0','0','0'],
#     ['0','0','0','0','0','0','0','0','1','0']
# ]

# max_column = len(map_array[0])
# max_row = len(map_array)

# print(max_column)
# print(max_row)

# for matrix in map_array:
#   for scalar in matrix:
#     print(scalar)


# MAP_ARRAY[row][column]
# for (i in something):
#     MAP_ARRAY[row][i] ### vertical walk
#     MAP_ARRAY[i][column] ### horizontal walk

# while(True)
#     rand_row = get the random row
#     rand_column = get the random column
#     if (it is a 1):
#         break

# MAP_ARRAY =  ['0','0','0','0','0','0','0','0','0','0']
# MAP_ARRAY[column]

###########################################################
#  IF WE INSTALL NUMPY, WE CAN RUN 
#  numpy.zeros(shape, dtype=float, order='C')
#  TO GENERATE AN ARRAY OF GIVEN SHAPE AND TYPE, FILLED WITH 0's
###########################################################