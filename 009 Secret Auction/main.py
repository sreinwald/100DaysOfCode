# create a secret auction program using a dictionary
import os


def cls():
    os.system("cls" if os.name == "nt" else "clear")


bids = {}


def bidding():
    cls()
    name = input("What is your name? ")
    bid = int(input("How much do you want to bid? "))
    bids[name] = bid


def keep_going():
    response = input("Would you like to bid again? (y/n) ")
    if response == "y":
        return True
    else:
        return False


still_bidding = True

while still_bidding:
    bidding()
    still_bidding = keep_going()

for i in bids:
    if bids[i] == max(bids.values()):
        print(i, "wins the auction!")
