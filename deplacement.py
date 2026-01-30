import os
import sys

# Standard library tools to capture single keypresses without needing 'Enter'
try:
    import termios
    import tty
except ImportError:
    # Support for Windows systems
    import msvcrt

def get_char():
    """Captures a single character from the terminal input."""
    if os.name == 'nt': # Windows
        return msvcrt.getch().decode('utf-8').lower()
    else: # Linux/macOS
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch.lower()

def clear_screen():
    """Clears the terminal for a clean ASCII frame."""
    os.system('cls' if os.name == 'nt' else 'clear')

def render(game_map, player, enemies=None):
    """
    ASCII Renderer for the terminal.
    - game_map: A 2D list of characters (e.g., '#' for walls, '.' for floors)
    - player: The Player object
    - enemies: A list of Enemy objects
    """
    # Create a temporary copy of the map for drawing
    display_grid = [list(row) for row in game_map]
    
    # Overlay the Player character '@'
    if 0 <= player.y < len(display_grid) and 0 <= player.x < len(display_grid[0]):
        display_grid[player.y][player.x] = str(player)
        
    # Overlay Enemies if any
    if enemies:
        for enemy in enemies:
            if 0 <= enemy.y < len(display_grid) and 0 <= enemy.x < len(display_grid[0]):
                display_grid[enemy.y][enemy.x] = getattr(enemy, 'char', 'E')

    # Output the grid to the terminal
    for row in display_grid:
        print("".join(row))
    
    # Display Player stats at the bottom
    print(f"\nHP: {player.life_point} | Gold: {player.gold} | Hunger: {player.hunger}")
def move_player(player, key, game_map):

    new_x, new_y = player.x, player.y

    if key in ['z', 'w']: # Up
        new_y -= 1
    elif key == 's':       # Down
        new_y += 1
    elif key in ['q', 'a']: # Left
        new_x -= 1
    elif key == 'd':       # Right
        new_x += 1
    
   
   
    obstacles = [' ', '|', '-', '#'] 
    
    if 0 <= new_y < len(game_map) and 0 <= new_x < len(game_map[0]):
        # Note: Checking game_map[y][x] for standard grid orientation
        if game_map[new_y][new_x] not in obstacles:
            player.x = new_x
            player.y = new_y