import random

def signum(a, b):
    if a - b > 0:
        return 1
    elif a - b < 0:
        return -1
    return 0


def bidding_diamond(diamonds):
    return random.choice(diamonds)

def pl_bid_check(plCards, Bid):
    if Bid in plCards:
        return Bid
    else:
        plCards.remove(random.choice(plCards))
    return 0

def Winnings(plBid, cBid, diamonds):
    plCards.remove(plBid)
    cCards.remove(cBid)
    diamonds.remove(bidding_diamond(diamonds))
    if signum(plBid, cBid) == 1:
        plWinnings.append(bidding_diamond(diamonds))
        return plWinnings
    elif signum(plBid, cBid) == -1:
        cWinnings.append(bidding_diamond(diamonds))
        return cCards

def result(plWinnings, cWinnings):
    return plWinnings >= cWinnings
diamonds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
plCards = diamonds[:]
cCards = diamonds[:]
plWinnings = []
cWinnings = []
cards = 13

print("Hello! Welcome to DIAMONDS\nLet's get started")
for i in range(cards):
    print("\nTurn :",i + 1)
    diamond = bidding_diamond(diamonds)
    print("You are going to bid on diamond", diamond)
    cBid = random.choice(cCards)
    print("Your Available cards are:\n", plCards)
    Bid = int(input("You wanna bid that for _? "))
    plBid = pl_bid_check(plCards, Bid)
    
    if plBid > 0:
        #print(plBid)
        Winnings(plBid, cBid, diamonds)
        if signum(plBid, cBid) == 1:
            print("You got it!!")
        elif signum(plBid, cBid) == -1:
            print("Your bid is too low!!")
        else:
            print("It's a tie...!")
    else:
        print("Enter valid card value!!!\nYou lost the diamond:(  ...as well as a card!!")
    print("Bcoz Opponent's bid is:",cBid)
print("Your have earned",plWinnings,"diamonds","\nYour score:", sum(plWinnings))

if result(plWinnings, cWinnings):
    print("You Won! Congratulations!!!")
else:
    print("Game Over!!\nBetter Luck next time")
