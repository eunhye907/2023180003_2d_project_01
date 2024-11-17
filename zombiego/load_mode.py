from pico2d import load_image, get_events, clear_canvas, update_canvas
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE, SDLK_KP_ENTER
import game_framework
import play_mode

load_W, load_H = 800, 600

def init():
    global image
    image = load_image('load_mode.png')

def finish():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(play_mode)

def draw():
    clear_canvas()
    image.draw(load_W // 2, load_H // 2)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass