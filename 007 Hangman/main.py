from operator import le
import random

print("Would you like to play a game of Hangman?")

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
reveal_word = []

for letter in range(0,len(chosen_word)):
    reveal_word.append("_")

def keep_guessing():
    guess = input("Choose a letter, any letter.\n").lower()
    return guess

def check_letter(guess):
    fail = 1
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            reveal_word[position] = letter
            fail = 0
    return fail

lives = 6
while ''.join(reveal_word) != chosen_word:
    print(f'Lives left: {lives}')
    print(reveal_word)
    guess = keep_guessing()
    # check_letter(guess)
    if check_letter(guess) > 0:
        lives -= 1
    if lives == 0:
        print("Game Over")
        quit()
print("A winner is you!")