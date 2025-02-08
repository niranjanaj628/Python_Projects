import turtle as t
import pandas as pd 

df=pd.read_csv('projects/Day-25/US-states/50_states.csv')

screen=t.Screen()
screen.title('India States game')
img="projects/Day-25/US-states/blank_states_img.gif"
screen.addshape(img)

t.shape(img)
all_states=list(df['state'])
states=all_states.copy()
guessed_states=[]
score=0

game_is_on=True

while game_is_on:
    guess=screen.textinput(title=f'{score}/50 States correct',prompt='Guess the state!').title()
    coords=t.Turtle()
    
    if guess in states:
        score+=1
        states.remove(guess)
        x=int(df['x'][df['state']==guess])
        y=int(df['y'][df['state']==guess])
        coords.hideturtle()
        coords.penup()
        coords.color('black')
        coords.goto(x,y)
        coords.write(guess)
        
    if guess=='Exit':
        states_to_learn=pd.DataFrame(states)
        states_to_learn.to_csv('D:/100-days-of-code/Python_Projects/projects/Day-25/US-states/states_to_learn.csv')
        game_is_on=False
        
    if score==50:
        game_is_on=False
       

screen.mainloop()