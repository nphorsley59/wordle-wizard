"""
Docstring
"""


from app.prompts import welcome_prompt, recommendation, guess_dialogue


class WordleWizard:
    """Docstring"""

    def __init__(self):
        """Docstring"""
        pass

    @staticmethod
    def run():
        welcome_prompt()
        recommendation()
        guess_dialogue()


def wordle_wizard_factory():
    """Docstring"""
    wizard = WordleWizard()
    return wizard


if __name__ == '__main__':
    test = wordle_wizard_factory()
    test.run()
