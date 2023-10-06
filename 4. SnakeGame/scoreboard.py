from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.score = 0
        self.color("white")
        self.update()

    def game_over(self):
        self.clear()
        self.goto(0, 12)
        self.write("GameOver!", True, ALIGNMENT, FONT)
        self.goto(0, -10)
        self.write(f"Your score is: {self.score}", True, ALIGNMENT, FONT)
    def update(self):
        self.clear()
        self.goto(0, 265)
        self.write(f"Score: {self.score}", True, ALIGNMENT, FONT)

    def increase_score(self):
        self.score+=1
        self.update()