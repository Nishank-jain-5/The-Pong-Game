from turtle import Screen
from moving_paddle import Moving_paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

# take input from user
mode = screen.textinput(title="Mode", prompt="Timed / Endless").lower()
l_user = screen.textinput(title="Player 1", prompt="Enter the name of left player: ")
r_user = screen.textinput(title="player 2", prompt="Enter the name of Right player: ")

# setup screen
screen.setup(800,600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

# initialise object
r_paddle = Moving_paddle((350,0))
l_paddle = Moving_paddle((-350,0)) 
ball = Ball()
scoreboard = Scoreboard(l_user, r_user)

# key press function
screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.fun_up)
screen.onkeypress(key="Down", fun=r_paddle.fun_down)
screen.onkeypress(key="w", fun=l_paddle.fun_up)
screen.onkeypress(key="s", fun=l_paddle.fun_down)


# game starts
game_is_on = True

while game_is_on:

    # update screen from animation
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # colliode with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with  right paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320):
        ball.bounce_x()
        scoreboard.r_score += 1
        scoreboard.print_score_name(l_user, r_user)

    # collision with left paddle
    if (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        scoreboard.l_score += 1
        scoreboard.print_score_name(l_user, r_user)
    
    # miss ball from right side
    if ball.xcor() > 350:
        if mode == "endless":
            ball.reset_position()

        scoreboard.l_score += 1
        scoreboard.print_score_name(l_user, r_user)

        if mode != "endless":
            game_is_on = False
            if scoreboard.left_win():
                scoreboard.game_over(l_user)
    
    # miss ball from left side
    if ball.xcor() < -350:
        if mode == "endless":
            ball.reset_position()
            
        scoreboard.r_score += 1
        scoreboard.print_score_name(l_user, r_user)

        if mode != "endless":
            game_is_on = False
            if not scoreboard.left_win():
                scoreboard.game_over(r_user)



screen.exitonclick()