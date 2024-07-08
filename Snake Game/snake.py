import turtle as t
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake():

    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = t.Turtle("square")
        new_segment.penup()
        new_segment.color("LimeGreen")
        new_segment.goto(position)
        self.all_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.all_segments[-1].position())

    def move(self):
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            self.new_x = self.all_segments[seg_num - 1].xcor()
            self.new_y = self.all_segments[seg_num - 1].ycor()
            self.all_segments[seg_num].goto(self.new_x, self.new_y)
            self.all_segments[0].speed(0)
        self.all_segments[0].forward(20)


    def reset(self):
        for segments in self.all_segments:
            segments.goto(1007, 100)
        self.all_segments.clear()
        self.create_snake()
        self.head = self.all_segments[0]
    def up(self):
        if self.head.heading() != DOWN:
         self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def down(self):
        if self.head.heading() != UP:
          self.head.setheading(DOWN)