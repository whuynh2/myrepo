name = input("Type your name: ")
print( "Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to and end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        answer = input("You swam across and find a nice house to be in, would you like to break in or keep moving (break/move)? ")

        if answer == "break":
            print("Someone is inside and shoots you. You lose")
        elif answer == "move":
            answer = input("Now you keep moving and you find a lady. Do you rob her or keep walking (rob/walk). ")

            if answer == "rob":
                print("You are a terrible person and the police get in a shoot out and kill you. You lose")

            elif answer == "walk":
                print("You move on with your life and continue on your way.")

            else:
                print('Not a valid option. You lose.')
        else:
            print('Not a valid option. You lose.')

    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
       print('This is not a valid option. You lose.')
        

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)" )

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose/")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else: 
    print('Not a valid option. You lose.')