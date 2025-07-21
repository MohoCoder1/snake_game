from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.sety(230)
        self.refresh()

    def add_score(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score is {self.score} | High Score : {self.high_score}", align="center")

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game over" , align="center")


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.refresh()

