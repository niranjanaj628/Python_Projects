#Treasure Island - Day 3

print("Welcome to Treasure Island. \nYour mission is to find the treasure.\n")
cross_road=input("You're at a cross-road."
                 "Where do you want to go?\n  Left or Right?\n").lower()

if cross_road == 'left':
    river=input("\nGood choice!\nCan you hear the sound of the water flowing?!\n"
                "Yes you're infront of the river!!\n"
                "Type 'swim' for Swimming across the river.\n"
                "Type 'wait' for Waiting!\n").lower()

    if river == 'wait':
        door=input("\nWoohoo!!\nYou made it across the river safely."
                   "Look at the doors! Red, Blue, and Yellow."
                   "Which one do you choose?)").lower()
        if door == 'red':
            print("\nOops Burned by fire. Game Over :(")
        elif door == 'blue':
            print("\nOops Eaten by beasts. Game Over :(")
        elif door == 'yellow':
            print("\nFound the treasure! Congratulations!")
        else:
            print('\nGame Over.')
            
    else:
        print("\nOh no, the trout got you! The treasure hunt ends here :(")
    
else:
    print("\nOops, you fell into the hole! The treasure hunt ends here :(")
    