from pathlib import Path
from types import ModuleType

import utils_ref


lost_file_name = 'conf.py'


def get_path_from_user() -> Path:
    while True:
        file_path = Path(input('путь: '))
        if file_path.is_file() and file_path.name == lost_file_name:
            return file_path
        print('! по указанному пути отсутствует необходимый файл !')


def ask_for_file() -> ModuleType:
    return utils_ref.load_file(get_path_from_user())


# >>> config_module = ask_for_file()
# путь: d:\G-Doc\TOP Academy\Python web\! Задачи\7. Импорт модулей, работа с путями, файловый ввод-вывод\data\conf.py
# >>>
# >>> config_module.defaults
# {'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}

