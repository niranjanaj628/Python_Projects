#Rock, paper and scissors game : Day - 4

import random
print("Welcome to the Rock , paper and scissors game!")
choice=int(input("What do you choose?\nType 0 for ROCK, 1 for PAPER and 2 for SCISSORS :"))

sys_choice_list=[0,1,2]
print('Computer chose:')
sys_choice=random.choice(sys_choice_list)
if sys_choice ==0:
    print('''
           _______
        ---'   ____)
                (_____)
                (_____)
                (____)
        ---.__(___)
          ''')
elif sys_choice ==1:
    print ('''
        _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
           ''')
elif sys_choice==2:
    print('''
        _______
    ---'   ____)____
               ______)
            __________)
          (____)
    ---.__(___)
    ''')
    
    
if choice==0:
    if sys_choice==0:
        print('It\'s a tie!')
    elif sys_choice==1:
        print('You lose!')
    elif sys_choice==2:
        print('You win!')
        
elif choice==1:
    if sys_choice==0:
        print('You win!')
    elif sys_choice==1:
        print('it\'s a tie!')
    elif sys_choice==2:
        print('You lose!')
        
if choice==2:
    if sys_choice==0:
        print('You lose')
    elif sys_choice==1:
        print('You win!')
    elif sys_choice==2:
        print('it\'s a tie!')
    