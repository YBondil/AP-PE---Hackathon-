
import math

def distance(x,y):
    return math.sqrt(x**2 + y**2)

class Grid:
    
def __init__(self, player, ennemies):
    self.player = player
    self.ennemies = ennemies
    self.grid =[[]]
    self.room = None

def is_there_enemy(self):
    for enemy in self.ennemies:
        if self.player.x == enemy.x and self.player.y == enemy.y:
            return enemy
    print("No ennemy on your position")
    return None

def initialize(self):
    grid[self.player.y][self.player.x] = "@"
    for enemy in self.ennemies:
        grid[enemy.y][enemy.x] = "E"
    
def update(self):
    self.player.move()
    self.ennemies.move()
