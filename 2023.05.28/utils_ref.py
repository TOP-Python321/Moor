from pathlib import Path
from shutil import get_terminal_size as gts, copy2
from sys import path
from types import ModuleType

import data.vars as data


ROOT_DIR = Path(path[0])
DATA_DIR = ROOT_DIR / 'data'


# для задачи 1
def important_message(text) -> str:
    width, padding = gts()[0] - 1, 2
    just = width - padding*2 - 2

    edge = '=' * (width-2)
    empty = ' ' * (width-2)
    
    words, lines, i = text.split(), [], 0
    while i < len(words):
        line = ''
        while i < len(words):
            if len(line + words[i]) > just:
                break
            line += words[i] + ' '
            i += 1
        lines += [line[:-1]]

    text = '\n'.join(
        f'#  {line.center(just)}  #'
        for line in lines
    )
    return (
        f'#{edge}#\n'
        f'#{empty}#\n'
        f'{text}\n'
        f'#{empty}#\n'
        f'#{edge}#'
    )


# для задачи 3
def load_file(file_path) -> ModuleType:
    copy2(file_path, ROOT_DIR)
    import conf
    return conf

