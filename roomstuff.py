class RoomContent:

    def __init__(self, room_name='', enemies=None, items=None,  chest=None, player=None):
        '''
        The constructor for the RoomContent class.  

        Required Parameters:

            room_name = (str)

            enemies = (list)

            items = (list)

            chest = (object)

            player = (object)
        
        Optional Parameters:

            description = description of room

        Returns:
            No returns
        ''' 
        if (items == None):
            items = []
        if (enemies == None):
            enemies = []
        self.room_name = room_name
        self.description = ''
        self.enemies = enemies
        self.items = items
        self.chest = chest
        self.player = player

class RoomNode:
    
    '''Takes room_content and populates it into the rooms'''

    def __init__(self, room_content=None):
        self.room_content = room_content
        self.north_exit = None
        self.south_exit = None
        self.east_exit = None
        self.west_exit = None
        # self.exits = {"west": west_room, "waterfall": hidden_room}

class GameMap:
    def __init__(self):
        self.map_entrance = None