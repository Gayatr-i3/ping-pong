from turtle import Turtle, Screen
from paddle import Paddle
from pingpong import Ping_Pong
from score import Score
import time
import random

turtle = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ping_Pong()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "q")
screen.onkey(l_paddle.go_down, "a")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()

screen.exitonclick()
