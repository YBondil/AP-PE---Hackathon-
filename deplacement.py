import arcade
import Player.py   

class Deplacement(Player):

    def turn_right(self):
        self.x += 1
    def turn_left(self):
        self.x -= 1
    def turn_up(self):
        self.y += 1
    def turn_down(self):
        self.y -= 1

    def on_key_press(self, key, modifiers):

        objets_infranchissables = [' ', '|', '-']

        if key == arcade.key.RIGHT and room[self.player.x + 1][self.player.y] not in objets_infranchissables:
            self.turn_right()
        elif key == arcade.key.LEFT and room[self.player.x - 1][self.player.y] not in objets_infranchissables:
            self.turn_left()
        elif key == arcade.key.UP and room[self.player.x][self.player.y + 1] not in objets_infranchissables:
            self.turn_up()
        elif key == arcade.key.DOWN and room[self.player.x][self.player.y - 1] not in objets_infranchissables:
            self.turn_down()