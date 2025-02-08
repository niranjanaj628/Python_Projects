# #TODO: Create a letter using starting_letter.txt 
# #for each name in invited_names.txt
# #Replace the [name] placeholder with the actual name.
# #Save the letters in the folder "ReadyToSend".
    
# #Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
starting_letter=open('./Input/Letters/starting_letter.txt','r')
word_list=starting_letter.readlines()
letter_list=list(word_list[0].split(' '))


invited_names=open('./Input/Names/invited_names.txt','r')
name_list=invited_names.readlines()

new_name_list=[]
for name in name_list:
    letters=list(name)
    letters[-1]=''
    name=''.join(letters)
    new_name_list.append(name)
    
    
sentance=word_list[0]  
file_name_list=['letter','for']
    
for i in range(len(new_name_list)):
    new_sentance=sentance.replace('[name]',new_name_list[i])
    word_list[0] = new_sentance
    
    file_name_list.append(new_name_list[i])
    filename='_'.join(file_name_list)
    letter=' '.join(word_list)
    file_name_list.pop()
    
    with open(f'./Output/ReadyToSend/{filename}.txt','w') as new_letter:
        new_letter.write(letter)
        
    print(f'Letter for {filename} created successfully!')
    
starting_letter.close()
invited_names.close()