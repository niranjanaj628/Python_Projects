# GAME OF PONG

from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor('white')
screen.title('Pong')
screen.tracer(0)

l_paddle=Paddle((-380,0))
r_paddle=Paddle((380,0))

ball= Ball()

score=Scoreboard()

#moving paddle
screen.listen()
screen.onkey(l_paddle.move_up,'Up')
screen.onkey(l_paddle.move_down,'Down')
screen.onkey(r_paddle.move_up,'Left')
screen.onkey(r_paddle.move_down,'Right')

#screen division

divider=Turtle()
divider.penup()
divider.goto(0,295)
divider.setheading(270)
divider.color('red')
for i in range(30):
    divider.pendown()
    divider.forward(10)
    divider.penup()
    divider.forward(10)


game_is_on=True

while game_is_on:
    time.sleep(ball.speed_limit)
    screen.update()
    ball.move()

    #detection with upper and lower walls
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
        
    #detection with paddles
    if ball.distance(r_paddle)<50 and ball.xcor()>340 or ball.distance(l_paddle)<50 and ball.xcor()<-340:
        ball.bounce_x()
        
    #ball misses r_paddle
    if ball.xcor()>398:
        ball.reset()
        score.l_increment()
    
    #ball misses l_paddle   
    if ball.xcor()<-398:
        ball.reset()
        score.r_increment()
        
    
screen.exitonclick()
