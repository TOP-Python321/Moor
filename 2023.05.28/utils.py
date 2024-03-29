from pathlib import Path
import importlib.util
import shutil


# КОММЕНТАРИЙ: много лишних переменных и лишних действий
def important_message(text: str) -> str:
    """
    Функция генерирует строку, в которой переданный текст будет обрамлён рамкой из символов '=' и '#'.
    
    :param text: Строка. Текст сообщения от пользователя.
    :return: Строка.
    """
    terminal_size = shutil.get_terminal_size().columns
    terminal_width = terminal_size - 3
    text_width = terminal_width - 4
    text_rows = []
    row = ''
    lines = '#' + '=' * terminal_width + '#'
    empty_line = f"#{' ' * terminal_width}#"
    words = text.split()
    
    for word in words:
        if len(row) + len(word) > text_width:
            text_rows.append(f'#{row.center(117)}#\n')
            row = ''
        row += word + ' '
    text_rows.append(f'#{row.center(117)}#\n')
    rows = ''.join(text_rows)
            
    header = f"\n\n{lines}\n{empty_line}\n"
    for row in text_rows:
        header += row
    header += f"{empty_line}\n{lines}\n\n"
    
    return header

    
def load_file(path: str):
    """
    Функция проверяет наличие файла по указанному пути. Если файл обнаружен, копирует его в другой каталог.
    
    :param path: Строка. Путь к потерянному файлу.
    :return: Объект модуля, созданного при импортировании файла.
    """
    user_path = Path(path)
    # ИСПРАВИТЬ: с текущим рабочим каталогом надо бы аккуратно — вы не знаете, что это за каталог и как он расположен относительно ваших файлов — а про каталог data вы знаете, что он расположен рядом с текущим файлом
    load_path = Path.cwd()

    shutil.copy2(user_path, load_path)

    # КОММЕНТАРИЙ: функция copy2() возвращает путь к копии файла в новом расположении
    name_modul = user_path.name
    path_modul = load_path.joinpath(name_modul)
    spec = importlib.util.spec_from_file_location(name_modul, path_modul)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    return module


def search_files(user_path: str | Path) -> dict[str, str]:
    """
    Функция осуществляет поиск и чтение всех файлов с расширением .txt по указанному пути.
    
    :param user_path: Строка. Путь к директории.
    :return: Словарь. Ключ - название файла, значение - содержимое файла.
    """
    file_ext = r'*.txt'
    text_files = list(file.name for file in Path(user_path).glob(file_ext))
    files = {}
    index = 0
    for path in Path(user_path).glob(file_ext):
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
            # КОММЕНТАРИЙ: сложно как-то..
            files[text_files[0 + index]] = text
            index += 1
    return files

