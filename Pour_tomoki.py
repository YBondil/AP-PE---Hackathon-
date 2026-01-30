import numpy as np
import math

def distance(x,y):
    return math.sqrt(x**2 + y**2)

def __init__(self, player, ennemies):
    self.player = player
    self.ennemies = ennemies
    self.grid = [[]]
    self.room = None

def is_there_enemy(self):
    for enemy in self.ennemies:
        if self.player.x == enemy.x and self.player.y == enemy.y:
            return enemy
    print("No ennemy on your position")
    return None

def initialize(self):
    self.grid[self.player.y][self.player.x] = "@"
    for enemy in self.ennemies:
        self.grid[enemy.y][enemy.x] = "E"

def update(self):
    self.player.move()
    self.ennemies.move()
    if self.is_there_enemy() != None:
        E = self.is_there_enemy()
        combat(self.player, E)
