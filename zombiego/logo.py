import game_framework
import start
from pico2d import load_image, delay, clear_canvas, update_canvas, get_events, get_time



logo_W, logo_H = 800, 600
def init():
    global image
    global logo_start_time
    image = load_image('logo.jpg')
    logo_start_time = get_time()

def finish():
    global image
    del image

def update():
    global logo_start_time
    if get_time() - logo_start_time >=2.0:
        logo_start_time = get_time()
        game_framework.change_mode(start)

def draw():
    clear_canvas()
    image.draw(logo_W // 2,logo_H // 2)
    update_canvas()

def handle_events():
    events = get_events()

def pause(): pass

def resume(): pass