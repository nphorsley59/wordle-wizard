"""
Docstring
"""


from dataclasses import dataclass


from utils import print_word


class Word:
    """Class to store information about a guessed word."""

    def __init__(self, word):
        self.word = self.validate_word(word)
        self.response = self.parse_word()
        print_word(self.response)

    @staticmethod
    def validate_word(word):
        """Validate word meets Wordle rules."""
        if len(word) != 5:
            raise Exception
        return word.upper()

    def parse_word(self) -> dict:
        """Break word into a dictionary of letters to store response."""
        letters = list(self.word)
        response = {}
        for i in range(len(letters)):
            response[i + 1] = {'letter': letters[i], 'color': 'Grey'}
        return response

    def store_response(self, position: str, color: str):
        """Store information about the position of an accepted letter."""
        self.response[position]['color'] = color
        print_word(self.response)


@dataclass
class Letter:
    """Docstring"""

    letter: str
    position: int
    state: str
