from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level=1
        self.color("black")
        self.penup()
        self.goto(-280,250)
        self.pendown()
        self.score_writer()

    def score_writer(self):
        self.clear()
        self.write(f"LEVEL:{self.level}",False,"left",FONT)

    def update_score(self):
        self.level += 1
        self.score_writer()

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER ", False, "center", FONT)