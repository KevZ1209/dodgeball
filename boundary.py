from turtle import Turtle


def create_boundary():
    t = Turtle()
    t.color("white")
    t.hideturtle()
    t.speed("fastest")
    t.penup()
    t.goto(-330, 130)
    t.pendown()
    t.forward(720)
    t.right(90)
    t.forward(260)
    t.right(90)
    t.forward(720)
    t.right(90)
    t.forward(260)
    t.right(90)


class Boundary:
    def __init__(self):
        create_boundary()
