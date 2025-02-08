from turtle import Screen
import time 
from snake import Snake
from food import Food
from scoreboard import Scoreboard 

screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor('blue')
screen.title('Snake Game')
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')


game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detect collision with the food
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.grow()
        scoreboard.increment()
        
    #detect collision with wall
    if snake.head.xcor()>295 or snake.head.xcor()<-295 or snake.head.ycor()>295 or snake.head.ycor()<-295:
        # scoreboard.gameover()
        scoreboard.update_highscore()
        snake.reset()
    #detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            # scoreboard.gameover()
            scoreboard.update_highscore()
            snake.reset()
screen.exitonclick()

import os
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))