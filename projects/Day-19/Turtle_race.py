#Turtle race: day-19

from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
user_choice=screen.textinput(title='Make your bet!', prompt='Which turtle will win the race? Choose a color:')
colors=['violet','indigo','blue','green','yellow','orange','red']
y_pos=[165,115,65,15,-35,-85,-135]
turtles=[]

race_is_on=False
for i in range(7):
    tt=Turtle(shape='turtle')
    tt.penup()
    tt.goto(x=-230,y=y_pos[i])
    tt.color(colors[i])
    turtles.append(tt)

if user_choice:
    race_is_on=True

while race_is_on:
    for t in turtles:
        if t.xcor()>230:
            race_is_on=False
            winning_color=t.pencolor()
            if winning_color==user_choice:
                print(f'You won! The {winning_color} turtle won the race.')
            else:
                print(f'You lost! The {winning_color} turtle won the race.')
            break
        distance=random.randint(0,10)
        t.forward(distance)
        
screen.exitonclick()