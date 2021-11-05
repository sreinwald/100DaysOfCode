alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(plain_text, shift_amount):
    shifted_text = ""
    for letter in plain_text:
        if alphabet.index(letter) + shift_amount > len(alphabet):
            new_position = alphabet.index(letter)+shift_amount-len(alphabet)
        else:
            new_position = alphabet.index(letter) + shift_amount
        shifted_text += alphabet[new_position]
    return shifted_text

def decode(shifted_text, shift_amount):
    shift_amount = shift_amount * -1
    return(encode(shifted_text, shift_amount))

def ask():
    text = input("Type your message\n").lower()
    shift = int(input("Type the shift number\n"))
    return  text, shift

def greet():
    print("Hello")
    print("Welcome to this very cool ceasar cipher program.")

def keep_going():
    if input("Keep going? Y/N\n").lower() == "n":
        return False
    else:
        return True

def ceasar():
    still_going = True
    while still_going == True:
        direction = input("Use 'encode' or 'decode'\n").lower()
        if direction == "encode":
            text, shift = ask()
            print(encode(text, shift))
            still_going = keep_going()
        else:
            text, shift = ask()
            print(decode(text, shift))
            still_going = keep_going()    

greet()
ceasar()