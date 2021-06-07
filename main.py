import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.setup(height=600, width=800)

r_paddle = Paddle((-355, 0))
l_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "w")
screen.onkeypress(r_paddle.go_down, "s")
screen.onkeypress(l_paddle.go_up, "Up")
screen.onkeypress(l_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 320 and ball.distance(l_paddle) < 50 or ball.xcor() > -350 and ball.distance(r_paddle) < 50:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
