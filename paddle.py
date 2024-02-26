from turtle import Turtle
import random
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def ping_pong_ball(self):
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("light blue")
        self.speed("fastest")



