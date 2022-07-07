import random # for random choose
from words import main_words_list# main_words_list-for words

states = [
'''
  +---+
  |   |
  o   |
 /|\  |
 / \  |
      |
========
''',
'''
  +---+
  |   |
  o   |
 /|\  |
 /    |
      |
========
''',
'''
  +---+
  |   |
  o   |
 /|\  |
      |
      |
========
''',
'''
  +---+
  |   |
  o   |
 /|   |
      |
      |
========
''',
'''
  +---+
  |   |
  o   |
  |   |
      |
      |
========
''',
'''
  +---+
  |   |
  o   |
      |
      |
      |
========
'''
] # for lives picture to print if wrong

random_word = random.choice(main_words_list)# for choice random word from the list

display = list()
for n in range(len(random_word)):# for add '_' into the display list
    display.append('_')

lives = 6 # for lives to play or choice wrong word

end_game = False
while not end_game:
    print(display)
    user_input = input('Enter your guess::').lower()# for get user input to guess the word and lower() convert big to small 'abc'
    
    for position in range(len(random_word)):# for add the correct guess word in the display list
        char = random_word[position]
        if char == user_input:
            display[position] = char
    
    if user_input not in random_word:# for check user guess is in random_word or not
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose")
            print(f"The Word is {random_word }")
    
    if '_' not in display:# for check all letters are correct or not
        end_game = True
        print('YOu win!')
        print(display)
    
    
    print(states[lives])# for print the picture of lives
