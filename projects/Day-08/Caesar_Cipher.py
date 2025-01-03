# Caesar Cipher : Day-8

#Encoding function
def encoding(message,shift_number,letters):
    encoded_message=[]
    for i in message:
        if i in letters:
            pos=letters.index(i)
            encoded_message.append(letters[(pos+shift_number)%26])
        else:
            encoded_message.append(i)
            
    return ''.join(encoded_message)

#Decoding function
def decoding(message,shift_number,letters):
    decoded_message=[]
    for i in message:
        if i in letters:
            pos=letters.index(i)
            decoded_message.append(letters[(pos-shift_number)%26])
        else:
            decoded_message.append(i)
        
    return ''.join(decoded_message)

#list of letters
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# taking the message, shift number and encryption/decryption choice from the user as input
while True:
    choice=input("Type 'encode' to encrypt, type 'decode' to decrypt:").lower()
    message=input("Enter the message: ").lower()
    shift_number=int(input('Enter the shift number: '))
    if choice=='encode': 
        print(f"Here's the encoded result: {encoding(message,shift_number,letters)}")
    elif choice=='decode':
        print(f"Here's the decoded result: {decoding(message,shift_number,letters)}")
    repeat=input("Enter 'yes' to continue, enter 'no' to stop: ")
    if repeat=='no':
        break
    

