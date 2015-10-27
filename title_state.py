import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image
    image = load_image('PIC1.PNG')

def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.change_state(main_state)
            elif(event.type,event.key) == (SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image.draw(600,400,1200,800)
    update_canvas()

def update():
    pass

def pause():
    pass


def resume():
    pass






