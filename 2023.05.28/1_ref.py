from pathlib import Path


def list_files(dir_path: str) -> tuple[str, ...] | None:
    dir_path = Path(dir_path)
    if not dir_path.is_dir():
        return None
    
    return tuple(
        file.name
        for file in dir_path.iterdir()
        if file.is_file()
    )


# >>> data_path = r'd:\G-Doc\TOP Academy\Python web\! Задачи\7. Импорт модулей, работа с путями, файловый ввод-вывод\data'
# >>> 
# >>> list_files(data_path)
# ('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')

