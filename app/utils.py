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


def print_word(response: dict):
    """Docstring"""
    print('\nGuess:')
    for letter in response['letters']:
        if letter in response['in_position']:
            print(colored(letter, 'grey', 'on_green') + ' ', end='', flush=True)
        elif letter in response['in_word']:
            print(colored(letter, 'grey', 'on_yellow') + ' ', end='', flush=True)
        else:
            print(colored(letter, 'grey', 'on_red') + ' ', end='', flush=True)
    print('')


def print_letter_pool(letter_pool: dict):
    """Docstring"""
    print('\nLetter Pool:')
    for letter in letter_pool:
        state = letter_pool[letter].state
        if 'in_position' in state:
            print(colored(letter, 'grey', 'on_green') + ' ', end='', flush=True)
        elif 'in_word' in state:
            print(colored(letter, 'grey', 'on_yellow') + ' ', end='', flush=True)
        elif 'not_in_word' in state:
            print(colored(letter, 'grey', 'on_red') + ' ', end='', flush=True)
        else:
            print(colored(letter, 'white', 'on_grey') + ' ', end='', flush=True)
    print('')


def update_letter_pool(letter_pool: dict, response: dict):
    """Docstring"""
    for key in response.keys():
        for letter in response[key]:
            letter_pool[letter].state.append(key)
            letter_pool[letter].position.append(response['letters'].index(letter))
    print_word(response)
    print_letter_pool(letter_pool)


def clean_response(response: str):
    """Docstring"""
    return list(re.sub('[^a-zA-Z]+', '', response).upper())


if __name__ == '__main__':
    print(clean_response('a, B, C'))
