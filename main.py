"""
Docstring
"""


from prompts import welcome_prompt, guess_response


class WordleWizard:
    """Docstring"""

    def __init__(self):
        """Docstring"""
        pass

    @staticmethod
    def run():
        welcome_prompt()
        guess_response()


def wordle_wizard_factory():
    """Docstring"""
    wizard = WordleWizard()
    return wizard


if __name__ == '__main__':
    test = wordle_wizard_factory()
    test.run()
