
class Player:
    def __init__(self,name,x_init, y_init):
        #caracteristcs 
        self.name = name
        self.x = x_init
        self.y = y_init
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
        item.got_picked()
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


if __name__ == "__main__":
    test = Player("titi", 2, 1)
    print(test)
