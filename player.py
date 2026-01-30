

class Player:
    def __init__(self,name,x_init, y_init):
        #caracteristcs 
        self.name = name
        self.x = x_init
        self.y = y_init
        self.has_moved = False
        self.life_point = 50
        self.thurst = 0
        self.hunger = 0 

        self.status = {"life point" : self.life_point, "thurst" : self.thurst, "hunger" : self.hunger}
        #fight
        self.strength = 1 
        self.weapon = None
        
        #items
        self.gold = 0
        self.potion = 0
        self.inventory = {"gold" : self.gold, "potions" : self.potion}

        
    def __repr__(self):
        return "@"
    
    def teleport(self, x_destination,y_destination ):
        self.x = x_destination
        self.y = y_destination

    def get_status(self):
        return self.status
    
    def get_inventory(self):   
        return self.inventory

    # item picking
    def pick_gold(self, gold_amount):
        self.gold += gold_amount
        print(f"{self.name} found {gold_amount} gold ! ")

    def pick_potion(self):
        self.potion += 1

    def pick_weapon(self, weapon):
        if self.weapon != None :
            print(f"{self.name} found {weapon}, do you want to pick it up ? ")
            answer = input()
            if answer == "Y" :
                self.weapon = weapon
                print(f"{self.name} pick {weapon} up ! ")
            else :
                print(f"{self.name} keeps {self.weapon}.")
        else:
            self.weapon = weapon
            print(f"{self.name} picks {weapon}")
                  
        
    def pick_water(self, water):
        self.thurst = max(0, self.thurst - water.thirst)
        print(f"{self.name} drinks, current thirst : {self.thurst}")

    def pick_food(self, food):
        self.hunger = max(0, self.hunger - food.nutrition)
        print(f"{self.name} eats, current hunger : {self.hunger}")

    def pick_item(self, item):
        item.is_picked()
        if item.type == "water":
            self.pick_water(item)
        elif item.type == "food":
            self.pick_food(item)
        elif item.type == "weapon":
            self.pick_weapon(item)
        elif item.type == "potion":
            self.pick_potion()
    
    #item using
    def use_potion(self):
        if self.potion <= 0 :
            print(f"{self.name} has no potion to use.")
        else :
            self.potion -= 1 
            self.life_point += 20
            print(f"{self.name} drinks a potion : +20hp ")
    
    #fight 
    def damage(self):
        return round(self.strength * self.weapon.damage)
    
    def got_hit(self, damage_dealt):
        self.life_point -= damage_dealt
        if self.life_point <= 0 :
            print(f"{self.name} died...")
    def is_alive(self):
        return self.life_point>0

    def move(self, key, game_map):
        self.has_moved = True
        self.last_x, self.last_y = self.x, self.y
        new_x, new_y = self.x, self.y

        if key in ['z', 'w']: new_y -= 1
        elif key == 's':      new_y += 1
        elif key in ['q', 'a']: new_x -= 1
        elif key == 'd':      new_x += 1

        obstacles = [" ", "-", "|"]

        if 0 <= new_y < len(game_map) and 0 <= new_x < len(game_map[0]):
            if game_map[new_y][new_x] not in obstacles:
                self.x, self.y = new_x, new_y

