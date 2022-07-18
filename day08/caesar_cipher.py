LETTERS = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(plain_text, shift_number, user_direction):
    end_text = ""
    if user_direction == "decode":
        shift_number *= -1  # for set shift_number minus value -1 * 1 = -1
    for letter in plain_text:
        if letter in LETTERS:
            position = LETTERS.index(letter)
            new_positon = position + shift_number
            end_text += LETTERS[new_positon]
        else:
            end_text += letter
    print(f"The {user_direction}d text is {end_text}")


def encrypt(plain_text, shift_number):
    cipher_text = ""
    for letter in plain_text:
        if letter in LETTERS:
            position = LETTERS.index(letter)
            new_positon = position + shift_number
            if new_positon > 26:
                new_positon = 0
            letter = LETTERS[new_positon]
            cipher_text += letter
        else:
            cipher_text += letter
    print(f"your encode text is {cipher_text}")


def dencrypt(cipher_text, shift_number):
    plain_text = ""
    for letter in cipher_text:
        if letter in LETTERS:
            position = LETTERS.index(letter)
            new_positon = position - shift_number
            if new_positon > 26:
                new_positon = 0
            letter = LETTERS[new_positon]
            plain_text += letter
        else:
            plain_text += letter
    print(f"Your decode text is {plain_text}")


should_continue = True
while should_continue:
    direction = input("Type  'Encode' to encrypt, type 'decode' to  decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    # if direction == "encode":
    #     encrypt(plain_text=text, shift_number=shift)
    # elif direction == "decode":
    #     dencrypt(cipher_text=text, shift_number=shift)
    # else:
    #     print("Please enter either 'decode' or 'encode'")
    #          OR

    shift = shift % 26  # for get remainde of shift number
    caesar(text, shift, direction)

    result = input("Type 'y' if you want to go again. Otherwise type 'n'::").lower()
    if result == 'n':
        should_continue = False
        print('Goodbye')

