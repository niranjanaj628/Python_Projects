import turtle as t

tommy=t.Turtle()
screen=t.Screen()

def move_forward():
    tommy.forward(10)
    
def move_backward():
    tommy.backward(10)
    
def turn_left():
    tommy.left(10)
    
def turn_right():
    tommy.right(10)

def clear():
    tommy.clear()
    tommy.penup()
    tommy.home() 
    tommy.pendown() 
    
screen.listen()
screen.onkey(move_forward,'f')
screen.onkey(move_backward,'b')
screen.onkey(turn_left,'l')
screen.onkey(turn_right,'r')
screen.onkey(clear,'c')

screen.exitonclick()