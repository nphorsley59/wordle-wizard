"""
Docstring
"""


from dataclasses import dataclass, field


from app.utils import print_word


class Guess:
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


@dataclass
class Letter:
    """Docstring"""

    letter: str
    position: int
    state: str = field(default='pending')
