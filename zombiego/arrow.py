from pico2d import *
import game_world


class R_arrow:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if R_arrow.image == None:
           R_arrow.image = load_image('right_arrow.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y, 100, 50)

    def update(self):
        self.x += self.velocity

        if self.x > 1000 - 100:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if group == 'zombie:arrow':
            print('zombie hit by arrow')
            game_world.remove_object(self)

class L_arrow:
    image = None

    def __init__(self, x=400, y=300, velocity=1):
        if L_arrow.image == None:
           L_arrow.image = load_image('left_arrow.png')
        self.x, self.y, self.velocity = x, y, -velocity

    def draw(self):
        self.image.draw(self.x, self.y, 100, 50)

    def update(self):
        self.x += self.velocity

        if self.x < 100:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if group == 'zombie:arrow':
            print('zombie hit by arrow')
            game_world.remove_object(self)