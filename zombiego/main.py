import game_framework
from pico2d import open_canvas, delay, close_canvas
import logo  as start_mode

open_canvas(800, 600)
game_framework.run(start_mode)
close_canvas()
