import arcade
from player import Player

class Deplacement(Player):

    def __init__(self, name, x_init, y_init, room):
        super().__init__(name, x_init, y_init)
        self.room = room

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

        if key == arcade.key.RIGHT and self.room[self.x + 1][self.y] not in objets_infranchissables:
            self.turn_right()
        elif key == arcade.key.LEFT and self.room[self.x - 1][self.y] not in objets_infranchissables:
            self.turn_left()
        elif key == arcade.key.UP and self.room[self.x][self.y + 1] not in objets_infranchissables:
            self.turn_up()
        elif key == arcade.key.DOWN and self.room[self.x][self.y - 1] not in objets_infranchissables:
            self.turn_down()
