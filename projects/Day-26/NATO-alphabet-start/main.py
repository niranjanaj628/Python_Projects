import pandas as pd

#TODO 1. Create a dictionary in this format:
nato=pd.read_csv('D:/100-days-of-code/Python_Projects/projects/Day-26/NATO-alphabet-start/nato_phonetic_alphabet.csv')
nato_dict={row.letter:row.code for (index,row) in nato.iterrows()}
print(nato_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word=input('Enter a word: ').upper()
output=[nato_dict[letter] for letter in word]
print(output) 