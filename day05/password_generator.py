import random

LETTERS = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
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
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

SYMBOLS = [
    "?",
    ">",
    "<",
    "(",
    ")",
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "~",
    "[",
    "]",
    "{",
    "}",
    ".",
    "|",
    ";",
    ":",
    "`",
    '"',
]

NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


print("#-------> Welcome to the PyPassword Generator! <-------#")

nr_letters = int(input("How many letterd would you like in your password?\n"))
nr_symbol = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):  # fro choice letters from the list
    password_list.append(random.choice(LETTERS))

# choice() function for choice randomly somthing from the list

for char in range(1, nr_symbol + 1):  # for choice symbols from the list
    password_list.append(random.choice(SYMBOLS))

for number in range(1, nr_numbers):  # for choice number from the list
    password_list.append(random.choice(NUMBERS))

random.shuffle(password_list)  # for reorder the list

password = ""

for char in password_list:  # for list to string
    password += char

print(f"Your PASSWORD is :{password}")
