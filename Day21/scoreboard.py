from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 22, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.update_scoreborad()

    def update_scoreborad(self):
        self.write(f"Current Score {self.score}", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreborad()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGMENT, font=FONT)

