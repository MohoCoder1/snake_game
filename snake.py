from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments: list[Turtle] = []
        self.create_segments()
        self.head = self.segments[0]


    def create_segments(self):
        for i in range(3):
            self.create_segment((-(i * 20), 0))



    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            self.segments[index].goto(self.segments[index - 1].pos())
        self.head.forward(DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def create_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)


    def add_segment(self):
        self.create_segment(position=self.segments[-1].pos())
