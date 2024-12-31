#Hangman word guessing game : Day-7

#importing random module
import random

#defining the list of words
list_of_words =['packet','library','detective', 'whole', 'mouth', 'progressive', 'flexible', 'burn', 'diabetes', 'extension', 'potttery', 'conclusion', 'correspond', 'flour', 'summary', 'concrete', 'morning', 'ritual', 'powder', 'soap']

#choosing a random word from the list
word=random.choice(list_of_words)

def hangman(word, hangmanpics):
    
    #number of lives initially=6
    lives=6

    #initializing the guess word with underscores
    guess='_'*len(word)

    #playing the game until all lives are lost or the word is guessed correctly
    while lives>0 :
        guess=list(guess)
        word=list(word)
        
        #checking if the word is guessed correctly
        if word==guess:
            print('Congratulations, You Win!')
            break
        
        #if the word is yet to be guessed correctly
        else:   
            print(f"\nword to guess:{''.join(guess)}")
            letter=input('Guess a Letter:').lower()
            
            #checking if the guessed letter is in the word
            if letter in word:
                for i in range(len(word)):
                    if letter==word[i]:
                        guess[i]=letter
                print(''.join(guess))
                
            #if the guessed letter is not in the word, decrement the lives by 1 and print the hangman picture
            else:
                lives-=1
                if lives==0:
                    print(f"The word was {''.join(word)}, you LOSE.")
                else:
                    
                    print(f"You guessed {letter}, but it's NOT in the word.\nYou've {lives} lives left.\n")
                    print(hangmanpics[0])
                    hangmanpics.pop(0)
        
    return lives

#list of hangman pics
hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print('Welcome to the game of Hangman! Tru guessing the word letter by letter.')

#number of lives initially=6
lives=6

#starting the game loop until all lives are lost or the word is guessed correctly
while lives>0:
    hangman(word, hangmanpics)
    