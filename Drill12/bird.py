import game_framework
from pico2d import *
import random

# Drill12 주석 ----------------------------------------------------------------
# 새의 크기 1.5m
# 새의 속도 40 km/h
# 맵크기 1600x600 pixel = 48m x 18 m
# Bird 생성 위치 상공 12m ~ 18m
# ----------------------------------------------------------------------------

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
FLY_SPEED_KMPH = 40.0  # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    def __init__(self):
        self.x, self.y = random.randint(0, 1600) , random.randint(400, 600)
        self.image = load_image('bird100x100x14.png')
        if random.randint(0, 1) == 0:
            self.dir = 1
        else:
            self.dir = -1

        self.velocity = 1
        self.frame = 0

    def update(self):
        print('bird', self.x, self.y, self.dir)
        if self.dir == 1:
            self.x += FLY_SPEED_PPS * self.velocity * game_framework.frame_time
        else:
            self.x -= FLY_SPEED_PPS * self.velocity * game_framework.frame_time

        if self.x >= 1600 - 25:
            self.dir = -1
        elif self.x <= 25:
            self.dir = 1

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 0, '', self.x - 25, self.y - 25,
                                          50, 50)
        else:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 0, 'h', self.x + 25,
                                          self.y - 25, 50, 50)
