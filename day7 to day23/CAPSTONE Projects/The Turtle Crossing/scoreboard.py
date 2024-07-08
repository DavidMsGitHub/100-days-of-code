FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("red")
        self.penup()
        self.goto(-250,250)
        self.level = 0
        self.write(f"Your Level: {self.level}", False, "left", ("Courier", 26, "bold"))


    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Your Level: {self.level}", False, "left", ("Courier", 26, "bold"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over, You crashed", False, "center", ("Courier", 26, "bold"))


