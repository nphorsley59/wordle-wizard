"""
Docstring
"""


from app.classes import Guess, Letter
from app.utils import clean_response, update_letter_state, print_word


def welcome_prompt():
    print("\n** == Welcome to the Wordle Wizard! == **\n")


def recommendation_prompt(guess_count: int):
    match guess_count:
        case 1:
            print("Here are some initial recommendations: ")
            print("1. LEARN\n2. STOIC\n3. THUMP")
        case 2:
            print("\nOkay, here are some recommendations for your 2nd guess: ")
            print("1. LEARN\n2. STOIC\n3. THUMP")
        case 3:
            print("\nOkay, here are some recommendations for your 3rd guess: ")
            print("1. LEARN\n2. STOIC\n3. THUMP")
        case 4:
            print("\nHmmm... here are some recommendations for your 4th guess: ")
            print("1. LEARN\n2. STOIC\n3. THUMP")
        case 5:
            print("\nHmmm... here are some recommendations for your 5th guess: ")
            print("1. LEARN\n2. STOIC\n3. THUMP")
        case 6:
            print("\nThis is your final guess, maybe it's one of these? ")
            print("1. LEARN\n2. STOIC\n3. THUMP")
        case 7:
            print("You have failed... unfortunate! Better luck next time.")
            exit()


def guess_prompt():
    guess = input("\nEnter your guess: ")
    if guess == 'WORDLE':
        print('\n** == Congratulations! == **')
        exit()
    return Guess(guess)


def response_prompt(letters: list[Letter]) -> list[Letter]:
    close = clean_response(input("\nWhich letters are highlighted yellow? "))
    hit = clean_response(input("Which letters are highlighted green? "))
    update_letter_state(letters, close, hit)
    print_word(letters)
    return letters
