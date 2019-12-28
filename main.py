import turtle
import os

# Setup Game Screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Chicken Invaders - Python")

# Draw Game Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.left(90)
border_pen.hideturtle()

# Player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player_speed = 15

# Moving The Player

## Left
def move_left():
    x = player.xcor()
    if(x > -280):
        x -= player_speed
        player.setx(x)

def move_right():
    x = player.xcor()
    if(x < 280):
        x += player_speed
        player.setx(x)

# Keyboard Bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

delay = input("Press enter to finish")