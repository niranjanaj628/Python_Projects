from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("./data.txt") as file:
            self.highscore=int(file.read())
        self.color('white')
        self.hideturtle()        
        self.penup()
        self.goto(-20,260)
        self.write(f'Score:{self.score}    High Score:{self.highscore}', False, align='center',font=('Arial', 15, 'bold'))
    
    def display_scoreboard(self):
        self.clear()
        self.write(f'Score:{self.score}    High Score:{self.highscore}', False, align='center',font=('Arial', 15, 'bold'))
    
    # def gameover(self):
    #     self.color('white')
    #     self.goto(0,0)
    #     self.write('GAME OVER', False, align='center',font=('Arial', 18, 'bold'))
        
    
    def increment(self):
        self.clear()
        self.score+=1
        self.display_scoreboard()
    
    def update_highscore(self):
        if self.score>self.highscore:
            self.highscore=self.score
            
        with open('./data.txt','w') as file:
            file.write(str(self.highscore))
            
        self.score=0 
        self.display_scoreboard()  
            