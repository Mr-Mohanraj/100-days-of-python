import os


def find_highest_bidders(dictionary):
    highest_bid = 0
    winner = ""
    for bidder in dictionary:
        bid_amout = dictionary[bidder]
        if bid_amout > highest_bid:
            highest_bid = bid_amout
            winner = bidder
    print(" ")
    print(f"The winner is {winner} with a bid of ${highest_bid}")


name_and_bid = {}

bidding_finished = False
while not bidding_finished:
    name = input("What is your name:: ")
    bid = int(input("What is your bid?: $"))

    name_and_bid[name] = bid
    should_continue = input("Are there any other bidders? Trpe 'yes' or 'no'").lower()
    
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidders(name_and_bid)
    elif should_continue == 'yes':
        os.system('cls')
