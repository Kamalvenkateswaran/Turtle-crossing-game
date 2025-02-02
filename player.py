STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
facing=90
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.next_round()
        self.setheading(90)


    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def next_round(self):
        self.goto(STARTING_POSITION)




