import random

print("#------> Welcome to Rock Paper Scissors <------#")

user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper OR 2 for Scissors.--"))

computer_choose = random.randint(0, 2)

if (0 <= user_choose <=2) and (0 <= computer_choose <= 2):
    if user_choose == computer_choose:
        print(f"Match Draw {user_choose} and {computer_choose}")
    elif computer_choose == 0:
        if user_choose == 1:
            print(f"You win! {user_choose} VS {computer_choose}")
        else:
            print(f"You Lose! {user_choose} VS {computer_choose}")
    elif computer_choose == 1:
        if user_choose == 2:
            print(f"You win! {user_choose} VS {computer_choose}")
        else:
            print(f"You lose! {user_choose} VS {computer_choose}")
    elif computer_choose == 2:
        if user_choose == 0:
            print(f"You win! {user_choose} VS {computer_choose}")
    else:
        print(f"You lose! {user_choose} VS {computer_choose}")
else:
    print(f"please change your number in between 0 To 2. Your input ->{user_choose}")
    
print("Thank you for playing")
