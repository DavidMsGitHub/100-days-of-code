from turtle import Turtle
FONT = ("Arial",25,"bold")
class Scoreboard(Turtle):

    def __init__(self,position):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(position)
        self.hideturtle()
        self.write("0", align="center", font=("Arial", 60, "bold"))

    def add_score(self, score):
        self.clear()
        self.write(score, align="center", font=("Arial", 60, "bold"))

