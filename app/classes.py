"""
Docstring
"""


from dataclasses import dataclass, field


from app.utils import get_words


class Guess:
    """Class to store information about a guessed word."""

    def __init__(self, word):
        self.word = self.validate_word(word.upper())
        self.letters = self.parse_word()

    @staticmethod
    def is_in_dictionary(word):
        dict_words = get_words('data/five_letter_words.txt')
        return word in dict_words

    def validate_word(self, word) -> str:
        """Validate that word meets Wordle rules."""
        if not self.is_in_dictionary(word):
            raise Exception
        return word

    def parse_word(self) -> list:
        """Parse letters and positions."""
        letters = list(self.word)
        return letters


@dataclass
class Letter:
    """Class to store information about a guessed letter."""

    position: list = field(default_factory=list)
    state: list = field(default_factory=list)
