import random
import math

class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.got_picked = False
        
    def is_picked(self):
        self.got_picked = True

class Enemy:

    def __init__(self, hp, x, y):
        self.life_point = hp
        self.x = x
        self.y = y
        self.last_x = x
        self.last_y = y
        self.damage = 15
        self.is_dead = 0
         
    def __repr__(self):
        return "E"
    
    def got_hit(self, damage):
        dodge = random.randint(1,10)
        if dodge <= 2 and self.life_point >= 0: #20% de chance d'esquive
            print("the enemy has dodged your attack")
        else:
            self.life_point -= damage
            if self.life_point <= 0:
                self.is_dead = 1
                print("Enemy defeated")

    def move(self, player, game_map):
        self.last_x, self.last_y = self.x, self.y
        dmin = 100
        rayon_action = 10
        obstacles = [" ", "-", "|"]
        best_move = (self.x, self.y)
        if not self.is_dead:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if (abs(dx) + abs(dy)) != 2: #on exclut les diagonales
                        new_x, new_y = self.x + dx, self.y + dy
                        if 0 <= new_y < len(game_map) and 0 <= new_x < len(game_map[0]):
                            if game_map[new_y][new_x] not in obstacles:
                                d = math.sqrt((new_x - player.x)**2 +(new_y - player.y)**2)
                                if d < dmin and d < rayon_action:
                                    dmin = d
                                    best_move = (new_x, new_y)

            self.x, self.y = best_move


class Weapon (Item):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.life_point = 5
        self.weapon_type = ""
        self.type = "weapon"

    def attack(self):
        self.life_point -= 1
        

class Sword (Weapon):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.strengh = 2
        self.weapon_type = "sword"
        self.damage = 10

    def __repr__(self):
        return "!"

    
class Bow (Weapon):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.strengh = 1
        self.weapon_type = "bow"
        self.damage = 10

    def __repr__(self):
        return ")"
     

class Gold (Item):

    def __init__(self, x, y, nb):
        super().__init__(x, y)
        self.number_of_gold = nb
        self.type = "gold"
    
    def __repr__(self):
        return "*"


class Magic_Potion (Item):

    def __init__(self, x, y, effect=None): #0 pour invisible, 1 pour force
        super().__init__(x, y)
        self.type = "magic potion"
        if effect == 0:
            self.is_invisible = 1
            self.strengh = 0
        else:
            self.is_invisible = 0
            self.strengh = 3
        self.is_consumed = 0
        self.life_point = 5
    
    def __repr__(self):
        return "j"

    def is_consumed(self):
        self.is_consumed = 1
    
    def update(self):
        if self.is_consumed and self.life_point > 0:
            self.life_point -= 1
            if self.life_point <= 0:
                print("Potion is no more effevctive")
    


class Armor (Item):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "armor"
        self.life_point = 10
        self.is_worn = 0

    def __repr__(self):
        return "a"
    
    def is_worn(self):
        self.is_worn = 1
    
    def is_attacked(self, damage):
        if self.life_point >= 0 and self.is_worn:
            self.life_point -= damage
        if self.life_point < 0:
            print("The armor is broken, cheh")


class Food (Item):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "food"
        self.is_eaten = 0
        self.food_recovery = 20

    def __repr__(self):
        return "f"

    def is_eaten(self):
        self.is_eaten = 1
        print("miam")



class Water (Item):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "water"
        self.water_recovery = 10
        self.thirst = 8

    def __repr__(self):
        return "w"
        







    

 







