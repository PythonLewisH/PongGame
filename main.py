from turtle import Screen
from pong_actions import HalfwayLine, Paddle, PongBall
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
game_is_on = True

halfway_line = HalfwayLine()

ball = PongBall()
right_paddle = Paddle((480, 0))
left_paddle = Paddle((-490, 0))
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.update()

screen.listen()
screen.onkey(right_paddle.right_up, "Up")
screen.onkey(right_paddle.right_down, "Down")
screen.onkey(left_paddle.left_up, "w")
screen.onkey(left_paddle.left_down, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

# Detect collision with paddles.
    if ball.distance(right_paddle) < 40 and ball.xcor() > 450 or ball.distance(left_paddle) < 40 and ball.xcor() < -450:
        ball.bounce_x()
        if ball.move_speed > 0.01:
            ball.move_speed -= 0.005

# Detect if ball goes past paddle.
    if ball.xcor() > 490:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        ball.move_speed = 0.05

    if ball.xcor() < -490:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        ball.move_speed = 0.05

screen.exitonclick()
