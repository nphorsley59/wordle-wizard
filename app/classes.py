"""
Docstring
"""


from dataclasses import dataclass


from app.utils import print_word


class Word:
    """Class to store information about a guessed word."""

    def __init__(self, word):
        self.word = self.validate_word(word)
        self.letters = self.parse_word()
        print_word(self.letters)

    @staticmethod
    def validate_word(word) -> str:
        """Validate that word meets Wordle rules."""
        if len(word) != 5:
            raise Exception
        return word.upper()

    def parse_word(self) -> list:
        """Store letters as Letter instances."""
        letters = list(self.word)
        letter_instances = []
        for i in range(len(letters)):
            letter_instance = Letter(letters[i], i + 1)
            letter_instances.append(letter_instance)
        return letter_instances

    def modify_state(self, position: int, state: str):
        """Modify the state of a letter based on Wordle feedback."""
        self.letters[position - 1].state = state
        print_word(self.letters)


@dataclass
class Letter:
    """Docstring"""

    letter: str
    position: int
    state: str = 'pending'
