from pico2d import *
import random

running = True

x = 600
y = 300

handXPos = random.randint(0, 1200)
handYPos = random.randint(0, 600)

dir = 0

def createHand():
    global handXPos
    global handYPos
    handXPos = random.randint(0, 1200)
    handYPos = random.randint(0, 600)
def checkHand():
    if x == handXPos and y == handYPos:
        createHand()

def movePlayer():
    global x
    global y
    global dir
    moveXVec = handXPos - x
    moveYVec = handYPos - y

    dis = math.sqrt(math.pow(moveXVec, 2)) + math.sqrt(math.pow(moveYVec, 2))


    moveXVec += moveXVec / dis
    moveXVec += moveXVec / dis

    x += moveXVec * 0.001
    y += moveYVec * 0.001

    if moveXVec > 0:
        dir = 0
    elif moveXVec < 0:
        dir = 1
    checkHand()


open_canvas(1200, 600)

# fill here
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


frame = 0
#hide_cursor()

handXPos = random.randint(0, 1200)
handYPos = random.randint(0, 600)

while running:
    clear_canvas()
    character.clip_draw(frame * 100 + (100*dir), 100 * 1 - (dir * 100), 100, 100, x, y)
    hand.draw(handXPos, handYPos)
    movePlayer()
    update_canvas()
    frame = (frame + 1) % 8

close_canvas()




