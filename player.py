
class Player :
    def __init__(self,name,x_init, y_init):
        #caracteristcs 
        self.name = name
        self.x = x_init
        self.y = y_init
        self.life_point = 50
        self.thurst = 0
        self.hunger = 0 
        #fight
        self.strength = 1 
        self.weapon = None
        
        #objects
        self.gold = 0
        self.magic_pot = 0
        
        
    
    def __repr__(self):
        return "@"
    
    def got_hit(self, damage_dealt):
        self.life_point -= damage_dealt
        if self.life_point <= 0 :
            print(f"{self.name} died...")
    #Object picking
    def pick_gold(self, gold_amound):
        self.gold += gold_amound
        print(f"{self.name} found {gold_amound} gold ! ")

    def pick_potion(self):
        self.potion

    def pick_weapon(self, weapon):
        if self.weapon != None :
            print(f"{self.name} found {weapon}, do you want to pick it up ? ")
            answer = input()
            if answer == "Y" :
                self.weapon = weapon
                print(f"{self.name} pick {weapon} up ! ")
            else :
                print(f"{self.name} keeps {self.weapon}.")
    def pick_water(self, water):
        self.thurst = max(0, self.thurst-water)
        print(f"{self.name} drinks, current thirst : {self.thurst}")
    
    def pick_food(self, food):
        self.hunger = max(0, self.hunger - food.nutrition)
        print(f"{self.name} eats, current hunger : {self.hunger}")

    def pick_object(self, object):
        object.got_picked()
        if consumable.type == "water" :
            self.pick_water()
        elif consumable.type == "food" : 
            self.pick_food()
        elif consumable.type == "weapon" : 
            self.pick_weapon ()
        elif consumable.type == "potion" : 
            self.pick_potion()
    

         
        



test = Player("titi", 2,1)
print(test)
print(type(test) == )