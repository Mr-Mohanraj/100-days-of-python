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

    if computer_total == customer_total:
        print("Match was draw")
    elif computer_total > customer_total:
        print("You went over.you lose ")
    else:
        print("You win")


def check_rule(customer_total, computer_total):

    if customer_total >= 21 and computer_total >= 21:
        return True
    else:
        return False


def getcard_totalValue(customer_gettotal=True, computer_gettotal=False):
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


def main():
    customerCards()
    computerCards()

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
    else:
        computer_total = getcard_totalValue(
            customer_gettotal=False, computer_gettotal=True
        )
        customer_total = getcard_totalValue()
        rule = check_rule(customer_total, computer_total)

        if rule:
            get_customer = getCard(customer_getcard=True)
            get_computer = getCard(customer_getcard=False, computer_getcard=True)
        else:
            computer_total = getcard_totalValue(
                customer_gettotal=False, computer_gettotal=True
            )
            customer_total = getcard_totalValue()
            print(
                f"Your cards : {customer_cards_list}, Current score: {customer_total}"
            )
            print(
                f"Computer's cards: {computer_cards_list}, Current score: {computer_total}"
            )
            check_winner(customer_total, computer_total)


if __name__ == "__main__":
    main()
