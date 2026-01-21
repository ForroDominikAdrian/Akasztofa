import random
import os
import time
import platform

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


HANGMAN = [
    """
     -----
     |   |
         |
         |
         |
         |
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    """
]





def guessing_letter(word, guess):
    used_letters = set()
    wrong_letters = set()
    tries = 0
    MAX_TRIES = 5

    while "".join(guess).lower() != word.lower() and tries < MAX_TRIES:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

        print(HANGMAN[tries])
        print("Szó:", " ".join(guess))
        print("Hibás betűk:", ", ".join(sorted(wrong_letters)))
        print(f"Hátralévő próbálkozások: {MAX_TRIES - tries}")
        
#Milán
        user_guess = input("Tippelj egy betűt: ").lower()

        if user_guess in used_letters:
            print("Erre már tippeltél!")
            time.sleep(1.5)
            continue

        used_letters.add(user_guess)

        if user_guess == word.lower():
            guess[:] = list(word)
            break

        if len(user_guess) != 1:
            print("Csak egy betűt írj be!")
            time.sleep(1.5)
            continue

        if user_guess in word.lower():
            for i, char in enumerate(word):
                if char.lower() == user_guess:
                    guess[i] = char
        else:
            wrong_letters.add(user_guess)
            tries += 1
