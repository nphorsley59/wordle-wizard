"""
Docstring
"""


import itertools


from classes import Letter
from app.prompts import (welcome_prompt, recommendation, guess_prompt,
                         response_prompt)
from app.utils import update_letter_pool


class WordleWizard:
    """Docstring"""

    KEYBOARD = {0: ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                1: ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
                2: ['Z', 'X', 'C', 'V', 'B', 'N', 'M']}
    VOWELS = ['A', 'E', 'I', 'O', 'U', 'Y']

    def __init__(self):
        """Docstring"""
        self.letter_pool = self.create_letter_pool()
        self.guess_count = 1

    def create_letter_pool(self):
        """Docstring"""
        alphabet = list(itertools.chain.from_iterable(
            [self.KEYBOARD[row] for row in self.KEYBOARD.keys()]))
        return {letter: Letter() for letter in alphabet}

    def run(self):
        """Docstring"""
        welcome_prompt()
        while True:
            recommendation(self.guess_count)
            guess = guess_prompt()
            response = response_prompt(guess.letters)
            update_letter_pool(self.letter_pool, response)
            self.guess_count += 1


if __name__ == '__main__':
    WordleWizard().run()
