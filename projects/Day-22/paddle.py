from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape('square')
        self.shapesize(5,1)
        self.penup()
        self.color('red')
        self.goto(pos)
        
    def move_up(self):
        x=self.xcor()
        y=self.ycor()+20
        self.goto(x,y)
        
    def move_down(self):
        x=self.xcor()
        y=self.ycor()-20
        self.goto(x,y)
        
        