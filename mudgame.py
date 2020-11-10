import dungeon_master
import game_map


def main():
    game_manager = dungeon_master.Dungeon_Master()   #game manager is a reference variable, Dungeon Master creates an object...game_manager points to the object (colloquially, game_manager is also called an object...but to be 100% correct, game_manager is a reference variable) 
    game_manager.create_enemies()
    game_manager.game_map = game_map.Map(game_manager.enemies)
    game_manager.create_player()
    game_manager.game_map.map_entrance.room_content.player = game_manager.player
    game_manager.clear_terminal()

    while (True):
        game_manager.print_current_room_info()
        player_action = game_manager.request_and_handle_player_action()
        if (player_action.lower() == 'exit'):
            print("Thank you for playing \"Knife in Chicago\".\nBe sure to smash that like button and subscribe for more content!\nhttps://www.youtube.com/channel/UCyRSaiIh7wFL9VhShOqSNUw\nShoutouts:  Duke, because he basically made this whole thing, heh.")
            break

main()



    # this is BFS and djikstra testing
    # for room in game_map.Map.bfs_list_map(game_manager.game_map.map_entrance):
    #     print(room.room_content.room_name)
    # shortest_paths = game_manager.dijkstra(game_manager.game_map.map_entrance)
    # for entry in shortest_paths.keys():
    #     output_string = str(entry.room_content.room_name) + ': '
    #     for path in shortest_paths[entry]:
    #         output_string += str(path.room_content.room_name) + ', '
    #     print (output_string[:-2])




# things to do:
  # Make items do something
    # manipulate dmg/atk calculations
        # subtract_hp...
        # need to add a "calculate_dmg" instead of using player's base atk
  # Make rest of items into dictioniaries 
    # make a map generator which generates random(n) number of rooms, all connected, with availability for pre-set rooms (boss rooms, treasure rooms, etc)  (Good fucking luck)
   

    