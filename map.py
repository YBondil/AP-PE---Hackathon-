from random import randint, choice

class Map:
    walls = [" ", "-", "|"]

    def __init__(self, map_size, player):
        self.size = map_size
        self.grid = [[" " for _ in range(map_size)] for _ in range(map_size)]
        self.player = player
        self.rooms_centers = []
        self.enemies = []
        self.items = []

    def new_room(self, w, h):
        room = [["." for _ in range(w)] for _ in range(h)]
        for k in range(w):
            room[0][k] = room[-1][k] = "-"
        for k in range(h):
            room[k][0] = room[k][-1] = "|"
        return room

    def can_place(self, x, y, w, h):
        if x < 0 or y < 0 or x + w >= self.size or y + h >= self.size:
            return False
        for r_y in range(y - 1, y + h + 1):
            for r_x in range(x - 1, x + w + 1):
                if 0 <= r_y < self.size and 0 <= r_x < self.size:
                    if self.grid[r_y][r_x] != " ":
                        return False
        return True

    def create_room(self, x, y, w, h):
        room = self.new_room(w, h)
        for i in range(h):
            for j in range(w):
                self.grid[y + i][x + j] = room[i][j]
        # Sauvegarde le centre pour les couloirs
        self.rooms_centers.append((x + w // 2, y + h // 2))

    def create_corridor(self, start, end):
        x1, y1 = start
        x2, y2 = end
        
        curr_x, curr_y = x1, y1
        
        def draw_path(target_x, target_y):
            nonlocal curr_x, curr_y

            step_x = 1 if target_x > curr_x else -1
            step_y = 1 if target_y > curr_y else -1
            
            while curr_x != target_x:
                if self.grid[curr_y][curr_x] == " ": self.grid[curr_y][curr_x] = "#"
                curr_x += step_x
            while curr_y != target_y:
                if self.grid[curr_y][curr_x] == " ": self.grid[curr_y][curr_x] = "#"
                curr_y += step_y

        if choice([True, False]):
            draw_path(x2, y2)
        else:
            while curr_y != y2:
                if self.grid[curr_y][curr_x] == " ": self.grid[curr_y][curr_x] = "#"
                curr_y += 1 if y2 > curr_y else -1
            while curr_x != x2:
                if self.grid[curr_y][curr_x] == " ": self.grid[curr_y][curr_x] = "#"
                curr_x += 1 if x2 > curr_x else -1

        self.grid[y1][x1] = "+"
        self.grid[y2][x2] = "+"



    def randomize(self, num_rooms):
        for _ in range(num_rooms):
            w, h = randint(4, 8), randint(4, 8)
            x, y = randint(1, self.size - w - 1), randint(1, self.size - h - 1)
            
            if self.can_place(x, y, w, h):
                self.create_room(x, y, w, h)
                if len(self.rooms_centers) > 1:
                    self.create_corridor(self.rooms_centers[-2], self.rooms_centers[-1])
        
        if self.rooms_centers:
            self.player.x, self.player.y = self.rooms_centers[0]

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

