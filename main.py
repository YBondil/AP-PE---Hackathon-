import os
import sys
from player import Player
import Enemy as itm
from map import Map

try:
    import termios
    import tty
except ImportError:
    import msvcrt

def get_char():
    if os.name == 'nt': 
        return msvcrt.getch().decode('utf-8').lower()
    else: 
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch.lower()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



def combat(player, enemy):
    clear_screen()
    print(f"!!! Fight : {player.name} vs Enemy !!!")
    while player.life_point > 0 and not enemy.is_dead:
        # Player attacks
        dmg = player.damage()
        enemy.got_hit(dmg)
        
        if not enemy.is_dead:
            # Enemy attacks back
            player.got_hit(enemy.damage)
            print(f"Enemy hits you for {enemy.damage}!")
        
        print(f"Your HP: {player.life_point} | Enemy HP: {enemy.life_point}")
        print("\nPress any key for next turn...")
        get_char()

def main():
    # Setup Player and Map
    hero = Player("Tomoki", 5, 5)
    weapon = itm.Sword(0,0)
    hero.pick_item(weapon)

    leonard = itm.Enemy(10, 8,8)
    
    water = itm.Water(1,3)
    potion = itm.Magic_Potion(2, 3)
    bow = itm.Bow(3, 3)

    items = []
    enemies = []
    
    m = Map(map_size=20, player=hero, enemies = enemies, items = items)

    m.place_item_randomly(potion)
    m.place_item_randomly(bow)
    m.place_item_randomly(water)

    # Create a room and place it
    room = m.new_room(width=12, height=8)
    m.create_room(room, (1, 1))
    
    print("Controls: ZSQD to move, X to quit. Press any key to start...")
    get_char()

    while hero.is_alive():
        clear_screen()
        m.render()
        
        # Capture input
        key = get_char()
        if key == 'x':
            break
    
        hero.move(key, m.grid)
        
        
        for e in enemies:
            if hero.x == e.x and hero.y == e.y and not e.is_dead:
                combat(hero, e)
        for i in items:
            if hero.x == i.x and hero.y == i.y and not i.got_picked:
                clear_screen()
                hero.pick_item(i)
                
                print("Press any key to continue...")
                get_char() 

    if hero.life_point <= 0:
        print("\nGAME OVER - You died.")
    else:
        print("\nGame exited.")

if __name__ == "__main__":
    main()