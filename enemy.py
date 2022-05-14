from turtle import Turtle
import random
MOVE_DISTANCE = 10


class Enemy:
    def __init__(self):
        self.x = 390
        self.y = random.randint(-6, 6)*20
        self.enemy = Turtle(shape="square")
        self.enemy.color("red")
        self.enemy.speed("fastest")
        self.enemy.penup()
        self.enemy.goto(self.x, self.y)

    def update(self):
        self.x -= 10
        self.enemy.goto(self.x, self.y)

    def bye(self):
        self.enemy.reset()