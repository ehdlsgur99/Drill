from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = random.randint(0, 7)
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 800), 599
        self.speed = random.randint(1, 10)
        self.size = random.randint(0, 1)

        if self.size == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
    def update(self):
        if self.y > 75:
            self.y -= self.speed
        elif self.y <= 75 and self.size == 1:
            self.y = 75
        elif self.y <= 75 and self.size == 0:
            self.y = 65

    def draw(self):
        print(self.size,self.x, self.y )
        if self.size == 0:
            self.image.clip_draw(0, 0, 21, 21, self.x, self.y)
        else:
            self.image.clip_draw(0, 0, 41, 41, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
team = [Boy() for i in range(11)]
balls = [Ball() for j in range(20)]
grass = Grass()
running = True
# game main loop code
while running:
    handle_events()
    for boy in team:
        boy.update()
    for b in balls:
        b.update()
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for b in balls:
        b.draw()

    update_canvas()
    delay(0.05)
close_canvas()

# finalization code