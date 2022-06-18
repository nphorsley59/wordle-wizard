"""
Docstring
"""


from classes import Word


def welcome_prompt():
    print("\n** == Welcome to the Wordle Wizard! == **\n")
    guess_1 = input("What was your first guess? ")
    Word(guess_1)


def guess_response():
    print("\n")
