import turtle

startXPos = -200
startYPos = 200

width =5
height = 5
distance = 100

i = 0
j = 0

while i < 5 :
    while j < 5 :
        turtle.penup()
        turtle.goto(startXPos + j * 100, startYPos - i* 100)
        turtle.pendown()
        turtle.forward(distance)
        turtle.right(90)
        turtle.forward(distance)
        turtle.right(90)
        turtle.forward(distance)
        turtle.right(90)
        turtle.forward(distance)
        turtle.right(90)
        j += 1
    i += 1
    j = 0
    
    

