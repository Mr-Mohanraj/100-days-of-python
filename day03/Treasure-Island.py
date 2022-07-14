print("Welcome TO Treasure Island :)")
print(' ')
print('Your Mission is to find theTreasure.')
print(' ')
user_input = input("You're at a cross road. Where do you want to go? Type 'left!' or 'right!'--").lower()
if user_input == 'right':
    print('You fell into a hole. Game Over')
elif user_input == 'left':
    user_input = input("You're come to a lake. There is on island in the middle of the lake. Type 'wait to for boat. Type 'swim' to swim across--").lower()
    if user_input == 'swim':
        print()
    elif user_input == 'wait':
        user_input = input("You arrive at the island unharmed. There is a house with 3 doors. One red, One yellow and one blue. Which color do you choose?--")
        if user_input == 'yellow':
            print("You Win The Treasure")
            print("But Treasure is gone!!!")
        elif user_input == 'blue':
            print("You enter a room of beasts. Game Over")
        elif user_input == 'red':
            print("You enter a room of fire. Game Over")
print(' ')
print("HAve a nice day")