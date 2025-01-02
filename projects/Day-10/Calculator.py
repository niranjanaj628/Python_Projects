#Calculator : Day-10

print('''
| ________ |
||12345678||
|""""""""""|
|[M|#|C][-]|
|[7|8|9][+]|
|[4|5|6][x]|
|[1|2|3][%]|
|[.|O|:][=]|
"----------" ''')

#addition function
def operations(x,y,op):
    if op=='+':
        res= x + y
    elif op=='-':
        res= x - y
    elif op=='x':
        res= x * y
    elif op=='/':
        if y!=0:
            res= x / y
        else:
            res= 'Error: Division by zero'

    return res
    

new= True

while True:
    if new==True:
        x=float(input('Enter the first number: '))
    op=input('Pick an operation:\n+\n-\nx\n/\n')
    y=float(input('Enter the second number: '))
    
    total= operations(x, y , op)
    print(f'{x} {op} {y} = {total}')
            
    repeat=input(f"Enter 'y' to continue calculating with {total}, enter 'n' to start a new calculation, or enter 'exit' to stop the calculator: ")
    if repeat.lower()=='exit':
        break
    elif repeat.lower()=='y':
        x=total
        new=False
    elif repeat.lower()=='n':
        new=True
        continue
        
