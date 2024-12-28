#Password-Generator: Day-5
import random

def password_generator():
    password=[]

    # Add letters
    for i in range(0,let_num):
        password.append(random.choice(letters))

    # Add symbols
    for j in range(0,sym_num):
        password.append(random.choice(symbols))
        
    # Add numbers
    for k in range(0,num_num):
        password.append(random.choice(numbers))
        
    # Shuffle the list
    random.shuffle(password)
    
    # Convert list to string and print it out
    password=''.join(password)
    return password
        
    
print('Welcome to the password generator!')
tot_char=int(input('How many total characters would you like in your password? '))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

let_num=int(input('How many letters would you like in your password? '))
sym_num=int(input('How many symbols would you like in your password? '))
num_num=int(input('How many numbers would you like in your password? '))

if (let_num+num_num+sym_num)==tot_char:
    print(f'Your password is:{password_generator()}')
else:
    print('Invalid input! Please ensure that you entered correct number of total characters, letters, numbers, and symbols.')


