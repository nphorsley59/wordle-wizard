"""
Docstring
"""


import re


from termcolor import colored


def get_words(path: str) -> list:
    """Read words from a .txt file."""
    words = []
    with open(path, 'r') as f:
        for line in f:
            words.append(line.rstrip())
    return words


def put_words(words: list, path: str):
    """Write words to a .txt file."""
    with open(path, 'w') as f:
        for word in words:
            f.write('%s\n' % word)


def print_word(letters: list):
    """Docstring"""
    for letter in letters:
        match letter.state:
            case 'pending':
                print(colored(letter.letter, 'white', 'on_grey'), end='', flush=True)
            case 'miss':
                print(colored(letter.letter, 'white', 'on_grey'), end='', flush=True)
            case 'close':
                print(colored(letter.letter, 'grey', 'on_yellow'), end='', flush=True)
            case 'hit':
                print(colored(letter.letter, 'grey', 'on_green'), end='', flush=True)
    print('')


def clean_response(response: str):
    """Docstring"""
    return list(re.sub('[^a-zA-Z]+', '', response).upper())


if __name__ == '__main__':
    print(clean_response('a, B, C'))
