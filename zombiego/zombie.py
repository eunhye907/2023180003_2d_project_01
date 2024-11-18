from pico2d import *
import random
import game_framework
import game_world

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 5.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10.0

animation_names = ['Walk']

class Zombie:
    image = None

    def __init__(self):
        if Zombie.image is None:
            Zombie.image = load_image('zombie.png')

        self.x = 500
        self.y = 300
        self.size = 150
        self.frame = 0
        self.dir = -1
        self.hp = 5
        self.removed = False

    def update(self):
        if not self.removed:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    def draw(self):
        if not self.removed:
            if self.dir == -1:
                self.image.clip_draw(int(self.frame) * 100, 100, 90, 90, self.x, self.y, self.size, self.size)
            else:
                self.image.clip_composition_draw(int(self.frame) * 100, 100, 90, 90, self.x, self.y, self.size, self.size)

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def handle_collision(self, group, other):
        if group == 'zombie:arrow':
            self.hp -= 1
            print(f'zombie hit, HP: {self.hp}')
            if self.hp <= 0 and not self.removed:
                self.removed = True
                game_world.remove_object(self)
