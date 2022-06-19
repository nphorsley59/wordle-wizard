"""
Docstring
"""


from app.prompts import welcome_prompt, recommendation_prompt, guess_prompt, response_prompt
from app.utils import update_letter_pool


class WordleWizard:
    """Docstring"""

    def __init__(self):
        """Docstring"""
        self.letters = None
        self.guess_count = 1

    def run(self):
        welcome_prompt()
        while True:
            recommendation_prompt(self.guess_count)
            guess = guess_prompt()
            letters = response_prompt(guess.letters)
            update_letter_pool(self.letters, letters)
            self.guess_count += 1


def wordle_wizard_factory():
    """Docstring"""
    wizard = WordleWizard()
    return wizard


if __name__ == '__main__':
    test = wordle_wizard_factory()
    test.run()
