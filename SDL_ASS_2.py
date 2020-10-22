
# SDL-Python Assignment No-2
# Build the Hangman Game using Python

import random

name = input("Enter  your name? ")

print("Good Luck ! ", name)

words = ['mobile', 'laptop', 'smartwatch', 'colours', 'watch', 'camera',
         'bullet', 'google', 'sunglasses', 'medicine']
word = random.choice(words)

print("Guess the characters")

guesses = ''

turns = 12

while turns > 0:

    failed = 0

    for char in word:
        if char in guesses:
            print(char)

        else:
            print("_")

            failed += 1

    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break

    guess = input("guess a character:")
    guesses += guess

    if guess not in word:
        turns -= 1

        print("Wrong")

        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose , better luck next time")
print("Thank you 😊 !")


# Output
"""
D:\Tutorial_point_code\venv\Scripts\python.exe D:/Tutorial_point_code/SDL_ASSGN/SDL_ASS_2.py
Enter  your name? Rohit
Good Luck !  Rohit
Guess the characters
_
_
_
_
_
guess a character:w
w
_
_
_
_
guess a character:a
w
a
_
_
_
guess a character:t
w
a
t
_
_
guess a character:c
w
a
t
c
_
guess a character:j
Wrong
You have 11 more guesses
w
a
t
c
_
guess a character:h
w
a
t
c
h
You Win
The word is:  watch
Thank you.😊!

Process finished with exit code 0


"""

