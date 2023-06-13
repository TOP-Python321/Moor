from pathlib import Path
import types

from utils import load_file


def ask_for_file() -> types.ModuleType:
    """
    Функция запрашивает у пользователя путь к потерянному файлу и вызывает импортированный объект модуля.
    
    :return: Объект модуля, созданного при импортировании файла.
    """
    while True:
        file_path = input(r"путь: ")
        if not Path(file_path).is_file():
            print("! по указанному пути отсутствует необходимый файл !")
        else:
            break
    return load_file(file_path)
    
    
# >>> config = ask_for_file()
# путь: D:\ACADEMY\HW\2023.05.28\dat
# ! по указанному пути отсутствует необходимый файл !
# путь: D:\ACADEMY\HW\2023.05.28\data\conf.py
# >>>
# >>> config.defaults
# {'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}

# >>> config = ask_for_file()
# путь: D:\ACADEMY\from_git\Moor\2023.05.28\data\vars.py
# >>>
# >>> config.TIMER
# 20