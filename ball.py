
from turtle import Turtle
import random

class Ball(Turtle):
    #create ball
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.shape("circle")
        self.color("white")
        self.speed("slow")
        self.penup()

    # move the ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.ball_X = new_x
        self.ball_y = new_y
        self.goto(new_x,new_y)

    # bounce in y direction
    def bounce_y(self):
        self.y_move *= -1

    # bounce in x direction
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # start moving ball from centre and in opposite dirextion
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
