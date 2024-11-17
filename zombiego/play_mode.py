from pico2d import*

import game_framework
import game_world
import load_mode
from arrow import R_arrow, L_arrow
from player import Player
from zombie import Zombie


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(load_mode)
        else:
            player.handle_event(event)

def init():
    global player
    global zombie
    global arrows

    player = Player()
    game_world.add_object(player, 1)

    zombie = Zombie()
    game_world.add_object(zombie, 1)

    arrow = R_arrow() or L_arrow()
    game_world.add_object(arrow, 1)

    game_world.add_collision_pair(arrow, zombie, 'zombie:arrow')
    game_world.add_collision_pair(zombie, player, 'player:zombie')

def finish():
    game_world.clear()
    pass

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass