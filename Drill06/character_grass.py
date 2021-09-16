from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

startPoint = 0
isCircleMove = False
# 0 = Right, 1 = Up, 2 = Left, 3 = Down
moveDirection = 0
prevMove =0 
isOver = False


x = 500
y = 90
degree = 270
while isOver == False:
    clear_canvas_now()
    grass.draw_now(400, 30)
    if isCircleMove==False:
        if(moveDirection == 0):
            if(x > 760):
                moveDirection = 1
            x += 15
            if x >= 500:
                if prevMove == 3:
                    prevMove = 0
                    isCircleMove = True
        if(moveDirection == 1):
            if(y > 560):
                moveDirection = 2
            y += 15
        if(moveDirection == 2):
            if(x < 30):
                moveDirection = 3
            x -= 15
        if(moveDirection == 3):
            if(y < 90):
                moveDirection = 0
                prevMove = 3
            y -= 15
     
    if isCircleMove==True:
        moveX = math.sin(degree / 360 * 2 * math.pi) * 100
        moveY = math.cos(degree / 360 * 2 * math.pi) * -100
        degree -= 30
        x += moveX
        y += moveY
        if degree == -90:
            isCircleMove = False
            degree= 270
    character.draw_now(x, y)
    delay(0.1)


close_canvas()
