#Coffee making machine : Day - 15
#TODO: money change
def money_change(total,price):
    change=total-price
    return change 


#TODO : make coffee
def make_coffee(coffee_details,report,price):
    for item in coffee_details:
        if item=='money':
            continue
        else:
            if report[item]<coffee_details[item]:
                print(f"Sorry there is not enough {item}.")
                return False
            else:
                report[item]-=coffee_details[item]
            
    report['money']+=price
    return report

menu={
    'espresso':{
        'ingredients':{
            'water':50,
            'coffee':18
        },
        'price':150
            
    },
    'latte':{
        'ingredients':{
            'water':200,
            'milk':150,
            'coffee':25 
        },
        'price':200
    },
    'cappuccino':{
        'ingredients':{
            'water':250,
            'milk':100,
            'coffee':24
        },
        'price':250
    }}
        
report={'water':300,
    'milk':200,
    'coffee':100,
    'money':0}

no_repeat=False

#TODO: user input
while True:
    if no_repeat==True:
        break
    else:
        '''Users can order 3 types of coffee. 
        additionally there is a report option for monitoring the resources and an off button for maintenance'''
        
        choice=input("Which coffee would you like to have? ('espresso','latte','cappuccino): ")
        
        # turns the machine off for maintenance
        if choice=='off':
            break
        
        # monitors the available resources present in the machine
        elif choice=='report':
            for item in report:
                if item=='milk' or item=='water':
                    print(f'{item}: {report[item]}ml')
                elif item=='coffee':
                    print(f'{item}: {report[item]}mg')
                else:
                    print(f'{item}: {report[item]} rupees')
        
        # makes the coffee         
        else:
            
            # accepting money in the form of currencies of 10, 20, 50, 100, 200 and 500
            print('Please insert the cash.')
            currency_10=int(input('How many 10s? :'))
            currency_20=int(input('How many 20s? :'))
            currency_50=int(input('How many 50s? :'))
            currency_100=int(input('How many 100s? :'))
            currency_200=int(input('How many 200s? :'))
            currency_500=int(input('How many 500s? :'))
            total=(currency_10*10)+(currency_20*20)+(currency_50*50)+(currency_100*100)+(currency_200*200)+(currency_500*500)

            # retreives the price of the coffee ordered by the user
            price=menu[choice]['price']
            
            # checks if the user has enough money to buy the coffee. if yes, it makes the coffee and returns the change and if not, refunds the money
            if total>=price:
                coffee_details=menu[choice]['ingredients']
                ans=make_coffee(coffee_details,report,price)
                if ans==False:
                    print('Here is the refund.')
                else:
                    report=ans
                    print(f"Here's your change of {money_change(total,price)} rupees. Enjoy your {choice}!\n")
                repeat=input('Do you eant another coffee? (y/n):')
                if repeat=='n':
                    no_repeat=True
                    
            else:   
                print("You don't have enough money to place the order. Money refunded.")
                repeat=input('Do you eant another coffee? (y/n):')
                if repeat=='n':
                    no_repeat=True     