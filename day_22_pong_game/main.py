from turtle import Screen
from paddle import  Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

#initialize the paddles, ball, and scoreboard
right_paddle = Paddle(360,0)
left_paddle = Paddle(-360, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.move_upwards, key="Up")
screen.onkey(right_paddle.move_downwards, key="Down")
screen.onkey(left_paddle.move_upwards, key="w")
screen.onkey(left_paddle.move_downwards, key="s")

playing_game = True

while playing_game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #check if ball collides with top or lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    #check if ball collides with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    #reset ball if it goes out of bounds on right side
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.increment_left_score()
        scoreboard.update_scoreboard()

    #reset ball if it goes out of bounds on left side
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.increment_right_score()
        scoreboard.update_scoreboard()


screen.exitonclick()