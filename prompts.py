"""
Docstring
"""


from classes import Word


def welcome_prompt():
    print("\n** == Welcome to the Wordle Wizard! == **\n")


def recommendation():
    print("Here are some recommendations: ")
    print("1. LEARN\n2. STOIC\n3. THUMP")


def guess_dialogue():
    guess_1 = input("\nEnter your guess: ")
    Word(guess_1)
