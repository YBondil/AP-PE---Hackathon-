from random import choice

class Map:
    walls = [" ", "-", "|"]

    def __init__(self, map_size,player, enemies = [], items = []):
        self.grid = [[" " for _ in range(map_size)] for _ in range(map_size)]
        self.rooms = []
        self.player = player
        self.enemies = enemies
        self.items = items

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
    
    def render(self):
        if 0 <= self.player.y < len(self.grid) and 0 <= self.player.x < len(self.grid[0]):
            if self.player.has_moved : 
                self.grid[self.player.last_y][self.player.last_x] = "."
            self.grid[self.player.y][self.player.x] = str(self.player)

        if self.enemies:
            for enemy in self.enemies:
                if not enemy.is_dead and 0 <= enemy.y < len(self.grid) and 0 <= enemy.x < len(self.grid[0]):
                    self.grid[enemy.y][enemy.x] = str(enemy)

        if self.items:
            for item in self.items:
                if 0 <= item.y < len(self.grid) and 0 <= item.x < len(self.grid[0]) and not item.got_picked:
                    self.grid[item.y][item.x] = str(item)

        for row in self.grid:
            print("".join(row))

        print(f"\nHP: {self.player.life_point} | Gold: {self.player.gold} | Hunger: {self.player.hunger}")

    def get_free_tiles(self):
        free_tiles = []

        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == ".":
                    # éviter le joueur
                    if x == self.player.x and y == self.player.y:
                        continue

                    # éviter les ennemis
                    if any(e.x == x and e.y == y and not e.is_dead for e in self.enemies):
                        continue

                    # éviter les items déjà placés
                    if any(i.x == x and i.y == y and not i.got_picked for i in self.items):
                        continue

                    free_tiles.append((x, y))

        return free_tiles

    def place_item_randomly(self, item):
        free_tiles = self.get_free_tiles()
        if not free_tiles:
            return False  # pas de place disponible

        x, y = choice(free_tiles)
        item.x = x
        item.y = y
        self.items.append(item)
        return True
    
    def place_enemy_randomly(self, enemy):
        free_tiles = self.get_free_tiles()
        if not free_tiles:
            return False  # pas de place disponible

        x, y = choice(free_tiles)
        enemy.x = x
        enemy.y = y
        self.enemies.append(enemy)
        return True