
from turtle import Turtle

class Scoreboard(Turtle):

    # initialise scoreboard
    def __init__(self, l_player, r_player):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        
        # print name on screen
        self.print_score_name(l_player, r_player)      

    # function tp print name and score on screen
    def print_score_name(self, l_player, r_player):
        self.clear()
        self.goto(-50,200)
        self.write(f"{self.l_score}", align="center", font=("Arial", 50, "normal"))
        self.goto(50,200)
        self.write(f"{self.r_score}", align="center", font=("Arial", 50, "normal"))
        self.goto(-150,250)
        self.write(f"{l_player}", align="center", font=("Arial", 25, "normal"))
        self.goto(150,250)
        self.write(f"{r_player}", align="center", font=("Arial", 25, "normal"))

    # print name of winner in end
    def game_over(self, winner):
        self.goto(0,0)
        self.write(f"{winner} won", align="center", font=("Arial", 40, "normal"))

    def left_win(self):
        if self.l_score > self.r_score:
            return True
        else:
            return False


