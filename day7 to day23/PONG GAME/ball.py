from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.game_speed = 0.075

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_from_paddle(self):
        self.x_move *= -1
        self.game_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.game_speed = 0.075
        self.bounce_from_paddle()



