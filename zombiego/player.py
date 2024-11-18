from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT

import zombie
from state_machine import start_event, right_down, left_up, left_down, right_up, space_down, StateMachine, time_out
from arrow import R_arrow, L_arrow
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Idle:
    @staticmethod
    def enter(player, e):
        if start_event(e):
            player.action = 3
            player.face_dir = 1
        elif right_down(e) or left_up(e):
            player.action = 2
            player.face_dir = -1
        elif left_down(e) or right_up(e):
            player.action = 3
            player.face_dir = 1

        player.frame = 0
        player.wait_time = get_time()

    @staticmethod
    def exit(player, e):
        if space_down(e):
            player.fire_arrow()

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 8

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 100, player.action * 100, 100, 100, player.x, player.y)


class Run:
    @staticmethod
    def enter(player, e):
        if right_down(e) or left_up(e):
            player.dir, player.face_dir, player.action = 1, 1, 1
        elif left_down(e) or right_up(e):
            player.dir, player.face_dir, player.action = -1, -1, 0

    @staticmethod
    def exit(player, e):
        if space_down(e):
            player.fire_arrow()

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 8
        player.x += player.dir * 5

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 100, player.action * 100, 100, 100, player.x, player.y)

class Player:

    def __init__(self):
        self.x, self.y = 200, 300
        self.face_dir = -1
        self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, space_down: Idle},
                Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, space_down: Run},
            }
        )

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))
        pass

    def draw(self):
        self.state_machine.draw()

    def fire_arrow(self):
        if self.face_dir == 1:
            arrow = R_arrow(self.x, self.y, self.face_dir * 3)
            game_world.add_object(arrow,1)
            game_world.add_collision_pair(arrow, zombie, 'zombie:arrow')
        elif self.face_dir == -1:
            arrow = L_arrow(self.x, self.y, self.face_dir * -3)
            game_world.add_object(arrow, 1)
            game_world.add_collision_pair(arrow, zombie, 'zombie:arrow')

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def handle_collision(self, group, other):
        pass
