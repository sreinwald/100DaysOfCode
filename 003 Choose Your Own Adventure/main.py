print("Welcome to Treasure Island. Your mission is to find the treasure")
choice1 = input("left or right? ").lower()
if choice1 == "left": 
    print("Cool, you didn't fall into a hole!")
else:
    print("You fall into a hole. Game Over.")
    quit()
choice2 = input("swim or wait? ").lower()
if choice2 == "wait":
    print("You wait for a while but you get bored and start wandering around. You come across a couple of doors. One red, one yellow, one blue.")
else: 
    print("You got killed by a trout. Game Over.")
    quit()
choice3 = input("Which door do you open? red, yellow, blue? ").lower()
if  choice3 == "red":
    print("The room is full of fire, you burn to a crisp. Game Over.")
    quit()
elif choice3 == "blue":
    print("Mighty beasts were locked up in this room. You get eaten. Game Over.")
    quit()
elif choice3 == "yellow":
    print("A winner is you!")
    quit()
else:
    print("Game Over")
    quit()


