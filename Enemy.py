import random

class Enemy:

    def __init__(self, hp, x, y):
        self.life_point = hp
        self.x = x
        self.y = y
        self.damage = 10
        self.is_dead = 0
         
    def __repr__(self):
        return "E"
    

    def got_hit(self, damage):
        dodge = random.randint(1,10)
        if dodge <= 2 and self.life_point >= 0: #20% de chance d'esquive
            print("the enemy has dodged tour attack")
        else:
            self.life_point -= damage
            if self.life_point <= 0:
                self.is_dead = 1
                print("Enemy defeated")


class Item:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type
        self.got_picked = 0
    
    def got_picked(self):
        self.got_picked = 1



class Weapon (Item):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.life_point = 5
        self.weapon_type
        self.type = "weapon"

    def attack(self):
        self.life_point -= 1
        

class Sword (Weapon):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.strengh = 2
        self.weapon_type = "sword"

    def __repr__(self):
        return "!"

    
class Bow (Weapon):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.strengh = 1
        self.weapon_type = "bow"

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

    def __init__(self, x, y, effect): #0 pour invisible, 1 pour force
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

    def __repr__(self):
        return "w"
        







    

 







