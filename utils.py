"""
Docstring
"""


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
    for position in response.items():
        match position[1]['color']:
            case 'Grey':
                print(colored(position[1]['letter'], 'white', 'on_grey'), end='', flush=True)
            case 'Yellow':
                print(colored(position[1]['letter'], 'grey', 'on_yellow'), end='', flush=True)
            case 'Green':
                print(colored(position[1]['letter'], 'grey', 'on_green'), end='', flush=True)
    print('')
