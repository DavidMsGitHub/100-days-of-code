from turtle import Turtle

Paddles = []

class Paddle(Turtle):
    def __init__(self, position_tuple):
        super().__init__()
        self.y_position = 0
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(5,1)
        self.goto(position_tuple)
        Paddles.append(self)

    def move_up(self):
        self.y_position = self.ycor() + 20
        self.goto(self.xcor(), self.y_position)
        print("up")

    def move_down(self):
        self.y_position = self.ycor() - 20
        self.goto(self.xcor(), self.y_position)
        print("down")
