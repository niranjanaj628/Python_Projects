# Number guessing game: Day-12
import random

def checking(num, guess):
    '''Function to check whether the guessed number is greater than. less than or equal to the actual number.'''
    if num==guess:
        return 0
    elif guess>num:
        return 1
    elif guess<num:
        return "-1"
    
print('Welcome to number guessing game!')
print('''
 _____                            _    _                                        _                  _  
|  __ \                          | |  | |                                      | |                | | 
| |  \/ _   _   ___  ___  ___    | |_ | |__    ___     _ __   _   _  _ __ ___  | |__    ___  _ __ | | 
| | __ | | | | / _ \/ __|/ __|   | __|| '_ \  / _ \   | '_ \ | | | || '_ ` _ \ | '_ \  / _ \| '__|| | 
| |_\ \| |_| ||  __/\__ \\__ \    | |_ | | | ||  __/   | | | || |_| || | | | | || |_) ||  __/| |   |_| 
 \____/ \__,_| \___||___/|___/    \__||_| |_| \___|   |_| |_| \__,_||_| |_| |_||_.__/  \___||_|   (_) 
                                                                                                      
                                                                                                      
      ''')
level=input("Enter level of difficulty: 'easy' or 'hard': ")
num=random.randint(0,100)

if level.lower()=='easy':
    chances=10
            
elif level.lower()=='hard':
    chances=5
    
for i in range (chances):
        guess=int(input('Make a guess: '))
        ans=checking(num,guess)
        if ans==0:
            print("Congratulations! You guessed the correct number!")
            break
        elif ans=="-1":
            print('Too low')
        elif ans==1:
            print('Too high.')
            
        if i!=chances-1:
            print(f'guess again.\nYou have {chances-(i+1)} chances left.')
        else:
            print(f'Oh no, the correct number was {num}.')