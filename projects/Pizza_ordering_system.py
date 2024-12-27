def billing(size,pepp,extra_cheese):
    #initial bill amount is 0 
    total=0
    
    #adding the base cost for the size of the pizza
    if size=='S':
        total+=15
        # adding the base cost for the pepperoni choice
        if pepp=='Y':
            total+=2
            # adding the base cost for the extra cheese choice
            if extra_cheese=='Y':
                total+=1
                return total
            else:
                return total
        if pepp=='N':
            if extra_cheese=='Y':
                total+=1
                return total
            else:
                return total
        
    elif size=='M':
        total+=20
        if pepp=='Y':
            total+=3
            if extra_cheese=='Y':
                total+=1
                return total
            else:
                return total
        if pepp=='N':
            if cheese=='Y':
                total+=1
                return total
            else:
                return total
        
    elif size=='L':
        total+=25
        if pepp=='Y':
            total+=3
            if extra_cheese=='Y':
                total+=1
                return total
            else:
                return total
        if pepp=='N':
            if extra_cheese=='Y':
                total+=1
                return total
            else:
                return total
    else:
        return 'Invalid size. Please choose S, M or L.'
    
    
print('Welcome to Pizza Castello!\nWhat size Pizza do you want? S, M or L:\n')
#input for size
size=input()
print('Do you want Pepperoni on your pizza? Y or N:')
#input for pepperoni
pepp=input()
print('Do you want extra cheese? Y or N:')
#input for extra cheese
extra_cheese=input()
print(f'Your final bill is: ${billing(size,pepp,extra_cheese)}')