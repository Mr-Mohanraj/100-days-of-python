import random

computer_guess = random.randint(1, 100)

print("#-------> Welcome to the Number Guessing Game <-------#")
print("I'M thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty.Type 'easy' or 'hard': ").lower()

guess_attempts = 0

if difficulty == "easy":
    guess_attempts = 10
elif difficulty == "hard":
    guess_attempts = 5
else:
    print(f"please Choose esay of hard, Not:{ difficulty }")


should_continue = True
while should_continue and guess_attempts > 0:
    print(f"You have {guess_attempts} attemps remaining to guess the number")
    guess_attempts -= 1
    high = 100
    low = 1
    user_guess = int(input("Make a guess: "))
    
    if  user_guess < 0:
        print(f"Please Enter Positive number, your number --> {user_guess}")

    if user_guess == computer_guess:
        print("You win")
        should_continue = False
    elif user_guess > computer_guess:
        print("Too high")
        low = user_guess
    else:
        print("Too low")
        high = user_guess

    if guess_attempts == 0:
        should_continue = False
    else:
        print("Guess again")
