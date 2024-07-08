from turtle import Turtle
FONT = ("Arial",25,"bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font= ("Arial", 35))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Your Score: {self.score} High Score: {self.high_score}", False, "center", FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
