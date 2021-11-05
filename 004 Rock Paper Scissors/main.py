import random
options = {0: "rock", 1: "paper", 2: "scissors"}

print("Hello, would you like to play a game?")
for i in options:
    print(i, options[i])

userChoice = int(input())
computerChoice = random.randint(0,2)

print(f'You Picked {options[userChoice]}, Computer picked {options[computerChoice]}')
if userChoice == computerChoice:
    print("Draw.")
elif (userChoice == 0 and computerChoice == 2) or (userChoice == 1 and computerChoice == 0):
    print("You Win!")
else:
    print("You lose.")
print("Thanks for playing with me.")