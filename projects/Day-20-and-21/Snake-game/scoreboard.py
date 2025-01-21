from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()        
        self.penup()
        self.score=0
        self.goto(0,280)
        self.write(f'Score:{self.score}', False, align='center',font=('Arial', 10, 'normal'))
        
    def gameover(self):
        self.color('white')
        self.goto(0,0)
        self.write('GAME OVER', False, align='center',font=('Arial', 18, 'bold'))
    def increment(self):
        self.clear()
        self.score+=1
        self.write(f'Score:{self.score}', False, align='center',font=('Arial', 10, 'normal'))
