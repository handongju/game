import random
import json
import os
import math

from pico2d import *

import game_framework
import title_state

name = "MainState"

hero = None
background = None
ground = []
monster = []
font = None
mon_counter = 0

class BackGround:
    def __init__(self):
        self.image = load_image('map\\bg.png')
    def draw(self):
        self.image.draw(600,400,1200,800)

class Ground:
    def __init__(self,x,y):
        self.image = load_image('map\\block.png')
        self.x = x
        self.y = y
        self.soil = 0
        self.destroy = False
        self.delay = 0

    def update(self):
        global monster
        for i in range(len(monster)):
            if abs(self.x-monster[i].x)<=50 and abs(self.y-monster[i].y)<=50 and self.delay ==0 and self.soil < 240:
                self.soil += 1
                delay = 50000

        if self.delay > 0:
            self.delay-=1
        pass
    def draw(self):
        self.image.clip_draw(0,108-(int)(self.soil/40)*18,18,18,self.x,self.y,48,48)

class Monster:
    def __init__(self,x,y):
        self.x, self.y = x,y
        self.frame = 0
        self.dir = 1
        self.image = load_image('character\\Loki.png')

    def update(self):
        self.frame = (self.frame + 1) % 6

    def draw(self):
        self.image.clip_draw(self.frame * 48, 240, 48, 48, self.x, self.y)
        pass

def enter():
    global background,ground
    ground = []
    monster = []
    for yy in range(0,14):
        for xx in range(0,20):
            ground.append(Ground(xx*50+120,yy*50+80))
    background = BackGround()

def exit():
    global background,ground
    del(background)
    del(ground)


def pause():
    pass


def resume():
    pass


def handle_events():
    global mon_counter
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.change_state(title_state)
            if event.type == SDL_MOUSEBUTTONDOWN:
                for yy in range(0,280):
                    if(ground[yy].destroy == False):
                        if abs(event.x - ground[yy].x)<=24 and abs((800-event.y) - ground[yy].y)<=24 :
                            ground[yy].destroy = True
                            monster.append(Monster(ground[yy].x,ground[yy].y))




def update():
    for i in range(len(monster)):
        monster[i].update()
    for yy in range(0,280):
        ground[yy].update()
    delay(0.07)
    pass


def draw():
    clear_canvas()

    background.draw()
    for yy in range(0,1):
        if ground[yy].destroy == False:
            ground[yy].draw()
    for i in range(len(monster)):
        monster[i].draw()
    update_canvas()





