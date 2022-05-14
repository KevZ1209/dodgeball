from turtle import Turtle
MOVE_DISTANCE = 10


class Player:
    def __init__(self):
        self.x = -200
        self.y = 0
        self.player = Turtle(shape="square")
        self.player.color("white")
        self.player.speed("fastest")
        self.player.penup()
        self.player.goto(self.x, self.y)

    def move_left(self):
        if (self.x > -310):
            self.x -= 20
            self.player.goto(self.x, self.y)

    def move_right(self):
        if (self.x < 370):
            self.x += 20
            self.player.goto(self.x, self.y)

    def move_up(self):
        if (self.y < 110):
            self.y += 20
            self.player.goto(self.x, self.y)

    def move_down(self):
        if (self.y > -110):
            self.y -= 20
            self.player.goto(self.x, self.y)
