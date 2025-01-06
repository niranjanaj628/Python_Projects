#importing necessary classes
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#object creation
menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()

#loop to carry out the operations  
while True:
    #customer choice
    choice=input(f'Which coffee would you like to have? {menu.get_items()}: ')
    
    #turning the machine off 
    if choice=='off':
        break
    
    #printing out the report
    elif choice=='report':
        coffee_maker.report()
        money_machine.report()
    
    # acccepting money and making the coffee
    else:
        item=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)
            
        

    