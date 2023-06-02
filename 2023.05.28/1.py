from pathlib import Path


def list_files(user_path: str) -> tuple | None:
    """
    Функция получает список имен файлов по указанному пути.
    
    :param user_path: Строка. Абсолютный путь к каталогу.
    :return: Кортеж с именами фалов, если они существуют по указанному пути, иначе None
    """
    path = Path(user_path)
    files = tuple((file.name for file in path.glob('*') if file.is_file()))
    
    return files if len(files) > 0 else None   
    
    
    
# >>> list_files(r'D:\Web Development\Blog with users')
# ('.idea.zip', 'blog.db', 'forms.py', 'main.py', 'poetry.lock', 'Procfile', 'pyproject.toml', 'requirements.txt')
# >>>
# >>> list_files(r'D:\Web Development\Blog with users\templates')
# ('about.html', 'contact.html', 'footer.html', 'header.html', 'index.html', 'login.html', 'make-post.html', 'post.html', 'register.html')