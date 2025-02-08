from turtle import Turtle
import time 
starting_position =[(0,0),(-20,0),(-40,0)]
move_distance=20
up=90
down=270
left=180
right=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake() 
        self.head=self.segments[0]
    def create_snake(self):
        for pos in starting_position:
            self.add_segment(pos)
        
    def add_segment(self,pos):
        t=Turtle('square')
        t.penup()
        t.color('white')
        t.goto(pos)
        self.segments.append(t) 
        
    def grow(self):
        self.add_segment(self.segments[-1].position())
        
    def move(self):
        segments=self.segments
        for seg in range(len(segments)-1,0,-1):
            x=segments[seg-1].xcor()
            y=segments[seg-1].ycor()
            segments[seg].goto(x,y)
            
        self.head.forward(move_distance)
        
    def up(self):
        if self.head.heading()!=down:
            self.head.setheading(up)
        
    def down(self):
        if self.head.heading()!=up:        
            self.head.setheading(down)
        
    def left(self):
        if self.head.heading()!=right:
            self.head.setheading(left)
        
    def right(self):
        if self.head.heading()!=left:
            self.head.setheading(right)
            
    def reset(self):
        for seg in self.segments:
            seg.goto(800,800)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]
        