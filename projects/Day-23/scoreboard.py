from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-250,250)
        self.write(f'Level {self.level}', font=('Courier',17,'normal'))
    def gameover(self):
        self.goto(-80,0)
        self.write("GAME OVER", font=FONT)
        
    def increment(self):
        self.clear()
        self.level += 1
        self.write(f'Level {self.level}', font=('Courier',20,'normal'))

