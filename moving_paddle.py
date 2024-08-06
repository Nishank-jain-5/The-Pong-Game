from turtle import Turtle, Screen

screen = Screen()

class Moving_paddle(Turtle):

    # create paddle
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)
        
    # move right paddle upward
    def fun_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)
    
    # move right paddle downward
    def fun_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

