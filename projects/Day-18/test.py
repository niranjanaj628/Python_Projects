import turtle as t
import random

def draw_square():
    tommy.forward(100)
    tommy.left(90)
    tommy.forward(100)
    tommy.left(90)
    tommy.forward(100)
    tommy.left(90)
    tommy.forward(100)
def dotted_line():
    tommy.forward(10)
    tommy.penup()
    tommy.forward(10)
    tommy.pendown()
    
def draw_shapes():
    for i in range(3,11):
        for j in range (i):
            tommy.forward(30)
            angle=360/i
            tommy.left(angle)
            tommy.forward(30)

def random_walk(colors,directions):
    tommy.shape('arrow')
    tommy.pensize(5)
    tommy.speed('fastest')
    t.colormode(255)
    
    for _ in range(100):
        #tommy.color(random.choice(colors))
        tommy.color(random_color())
        tommy.forward(20)
        tommy.setheading(random.choice(directions))
        
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)


def spirograph(size_of_gap):
    tommy.shape('arrow')
    tommy.speed('fastest')
    t.colormode(255)
    
    for _ in range(360//size_of_gap):
        tommy.color(random_color())
        tommy.circle(100)
        current_heading=tommy.heading()
        tommy.setheading(current_heading+5)

tommy=t.Turtle()
# tommy.shape('turtle')
# tommy.color('DarkOrange4')

colors=['coral','AquaMarine1','DarkOrange3','blue4','brown4','CadetBlue3','DarkCyan','DarkGreen','DarkSlateGray','DeepPink4']
directions=[0,90,180,270]

# for i in range(10):
#     dotted_line()
    
# draw_shapes()

# random_walk(colors,directions)

spirograph(5)

screen=t.Screen()
screen.exitonclick()