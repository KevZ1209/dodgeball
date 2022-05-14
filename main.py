from turtle import Turtle, Screen
from player import Player
from enemy import Enemy
from boundary import Boundary
import time
import random

my_screen = Screen()
my_screen.setup(width=1000, height=1000)
my_screen.bgcolor("black")
my_screen.title("DODGEBALL")
my_screen.tracer(0)

player = Player()
boundary = Boundary()

# game status turtle
status = Turtle()
status.color("white")
status.penup()
status.hideturtle()
status.goto(-80, 150)
status.write("Dodgeball!", font=("Courier", 24, "normal"))
status.goto(-100, 0)



my_screen.listen()
my_screen.onkey(player.move_up, "w")
my_screen.onkey(player.move_down, "s")
my_screen.onkey(player.move_left, "a")
my_screen.onkey(player.move_right, "d")

all_enemies = []

game_is_on = True
difficulty = 5
iterations = 0
while game_is_on:
    my_screen.update()
    time.sleep(0.05)
    if random.randint(0, difficulty) == 1:
        all_enemies.append(Enemy())

    # loop through all enemies
    for e in all_enemies:
        if e.x < -310:
            e.bye()
            del e
        else:
            if player.x <= e.x <= player.x+20 and e.y == player.y:
                status.write("OOF! Click to Exit", font=("Courier", 24, "normal"))
                game_is_on = False
            else:
                e.update()



my_screen.exitonclick()