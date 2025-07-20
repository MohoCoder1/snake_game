import random
from turtle import Turtle


class Food(Turtle) :
    def __init__(self):
        super().__init__(shape="circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-230 , 230)
        random_y = random.randint(-230 , 230)
        self.goto(random_x,random_y)
