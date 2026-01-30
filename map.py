from random import randint

class Map:
    walls = [" ", "-", "|"]

    def __init__(self, map_size,player, nb_enemies, objects):
        self.grid = [[" " for _ in range(map_size)] for _ in range(map_size)]
        self.rooms = []
        self.player = player

    def new_room(self, width, height):
        room = [["." for _ in range(width)] for _ in range(height)]
        for k in range(width):
            room[0][k] = "-"
            room[-1][k] = "-"
        for k in range(height):
            room[k][0] = "|"
            room[k][-1] = "|"
        return room

    def create_room(self, room, pos):
        pos_x, pos_y = pos
        width, height = len(room[0]), len(room)
        n = len(self.grid)
        
        assert (pos_x + width <= n and pos_y + height <= n)
        
        for y in range(height):
            for x in range(width):
                self.grid[pos_y + y][pos_x + x] = room[y][x]

    def is_walkable(self, x, y):
        if 0 <= y < len(self.grid) and 0 <= x < len(self.grid[0]):
            return self.grid[y][x] not in self.walls
        return False

    def affichage(self):
        
        for row in self.grid:
            print("".join(row))