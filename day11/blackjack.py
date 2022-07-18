import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
customer_cards_list = []
computer_cards_list = []


def customerCards():
    total = 0
    for card in range(2):
        customer_cards = random.choice(cards)
        customer_cards_list.append(customer_cards)
    return None


def computerCards():
    total = 0
    for card in range(2):
        computer_cards = random.choice(cards)
        computer_cards_list.append(computer_cards)
    return None


def check_winner(customer_total, computer_total):
    """Ruturn Winner"""    
    if (customer_total > computer_total) and (customer_total <= 21):
        print("You Win")
    elif (customer_total < computer_total) and (computer_total <= 21):
        print("You Lose")
    elif customer_total == computer_total:
        print("Match Drew")
    elif (computer_total > 21) or (customer_total > 21):
        if computer_total > 21 or customer_total > 21 :
            if customer_total < computer_total:
                print("You Win")
            else:
                print("You Lose")
    else:
        print("something is worng!!!,Please try again!")


def getcard_totalValue(customer_gettotal=True, computer_gettotal=False):
    if customer_gettotal == False:
        computer_gettotal = True
    
    if computer_gettotal and customer_gettotal:
        print("You must set either one of the value set to False")
    elif computer_gettotal:
        total = 0
        for i in computer_cards_list:
            total += i
        return total
    else:
        total = 0
        for i in customer_cards_list:
            total += i
        return total


def getCard(customer_getcard=True, computer_getcard=False):
    if customer_getcard == False:
        computer_getcard = True

    if computer_getcard and customer_getcard:
        print("You must set either one of the value set to False")
    elif customer_getcard:
        customer_cards = random.choice(cards)
        customer_cards_list.append(customer_cards)
        return customer_cards_list
    else:
        computer_cards = random.choice(cards)
        computer_cards_list.append(computer_cards)
        return computer_cards_list


def check_rule(customer_total, computer_total):
    """Customer total and computer total """
    
    if customer_total >= 21 and computer_total >= 21:
        return False
    elif customer_total <= 21 and computer_total <= 21:
        if customer_total < 17 or computer_total < 17:
            return getCard(),getCard(customer_getcard=False),getcard_totalValue(),getcard_totalValue(customer_gettotal=False)
    else:
        print("Something is wrong!!!, Please try again! check_rule")

def main():
    computer_total = getcard_totalValue(customer_gettotal=False, computer_gettotal=True)
    customer_total = getcard_totalValue()

    print(f"Your cards : {customer_cards_list}, Current score: {customer_total}")
    print(f"Computer's cards: {computer_cards_list}, Current score: {computer_total}")

    choose = input("Type 'y' to get another card, Type 'n' to pass:: ").lower()

    if choose == "n":
        print(f"Your cards : {customer_cards_list}, Current score: {customer_total}")
        print(
            f"Computer's cards: {computer_cards_list}, Current score: {computer_total}"
        )
        check_winner(customer_total, computer_total)
    elif choose == "y":
        checked = check_rule(customer_total, computer_total)  
        print(f"Your cards : {checked[0]}, Current score: {checked[2]}")
        print(f"Computer's cards: {checked[1]}, Current score: {checked[3]}")
        check_winner(checked[2], checked[3])
    else:
        print("Plase choose either one of the 'y' or 'n'!!!")


if __name__ == "__main__":

    should_run = True
    while should_run:
        play_not = input("Enter if you want play one time,Type 'y' for paly OR type 'n' for quit--->").lower()
        if play_not == "y":
            print("#----- Welcome to our game -----#")
            main()
        elif play_not == "n":
            should_run = False
            print("Wlecome back sir :)")
        else:
            print(f"Please enter either one yes or no.your inpute --->{play_not}")
