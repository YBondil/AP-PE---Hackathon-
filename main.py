from player import Player
from Enemy import *
from Map import *
from deplacement import *

def combat(player, enemy):
    print(f"Fight : {player.name} vs enemy")
    while player.life_point > 0 and not enemy.is_dead:
        print(f"{player.name} attacks with {player.weapon.weapon_type} !")
        enemy.got_hit(player.damage())
        print(f"Enemy hp : {enemy.life_point}, Player hp : {player.life_point}")
        if enemy.is_dead:
            print("Battle won !")
        else:
            print(f"Enemy attacks {player.name} !")
            player.got_hit(enemy.damage)
            print(f"Enemy hp : {enemy.life_point}, Player hp : {player.life_point}")

#tests
tomoki = Player("zizi", 0, 0)

arm = Sword(0,0)
tomoki.pick_item(arm)

leonard = Enemy(25,0,0)


while True :
    move = Deplacement()

