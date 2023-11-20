from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-150, 250)
        self.write(self.l_score, align="center", font=("Arial", 40, "normal"))
        self.goto(150, 250)
        self.write(self.r_score, align="center", font=("Arial", 40, "normal"))

    def left_point(self):
        self.l_score += 1
        self.update_score()

    def right_point(self):
        self.r_score += 1
        self.update_score()
