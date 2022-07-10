"""
Docstring
"""


from app.prompts import (welcome_prompt, recommendation, guess_prompt,
                         response_prompt)
from app.utils import update_letter_pool


class WordleWizard:
    """Docstring"""

    def __init__(self):
        """Docstring"""
        self.letter_pool = {}
        self.guess_count = 1

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
