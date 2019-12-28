import turtle
import os

# Setup Game Screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Chicken Invaders - Python")
player_speed = 15
enemy_speed = 2
bullet_speed = 20
lifes = 5
bullet_state = "ready"

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

# Enemies
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

# Bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(.25, .25)
bullet.hideturtle()

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

def fire():
    # Define bullet state
    global bullet_state

    if bullet_state == "ready":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet.setpos(x, y + 15)
        bullet.showturtle()

# Key Bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire, "space")

# Main Game
while True:
    # Move the enemy
    y = enemy.ycor()
    y -= enemy_speed
    enemy.sety(y)

    if y < -280:
        # Lost one life
        print("Debug: reached bottom")
        enemy_speed *= -1
    if y > 280:
        print("Debug: reached top")
        enemy_speed *= -1

    # Move the bullet
    if bullet_state == "fire":
        bullet_y = bullet.ycor()
        bullet_y += bullet_speed
        bullet.sety(bullet_y)
        
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

delay = input("Press enter to finish")