from dataclasses import dataclass
from os import name as os_name
from typing import Self

if os_name == 'nt':
    PATH_SEP = '\\'
else:
    PATH_SEP = '/'


@dataclass
class File:
    """Файл в файловой системе."""
    name: str
    dir: str

    @property
    def extension(self) -> str:
        return ''.join(self.name.rsplit('.', 1)[1:])

    def ls(self) -> str:
        return self.dir + PATH_SEP + self.name


class Folder(list):
    """Каталог в файловой системе. Может содержать вложенные каталоги и файлы."""
    def __init__(self, name: str, dir: str):
        super().__init__()
        self.name = name
        self.dir = dir

    def add_file(self, file: File | Self):
        self.append(file)

    def remove_file(self, file: File | Self):
        self.remove(file)

    def ls(self) -> str:
        output = self.dir + PATH_SEP + self.name
        for component in self:
            output += '\n' + component.ls()
        return output


def ls(*objects: File | Folder) -> str:
    for obj in objects:
        print(obj.ls())


file1 = File("file1.txt", "dir")
file2 = File("file2.txt", "dir")
folder1 = Folder("folder1", "dir")
folder2 = Folder("folder2", "dir")

# Добавляем файлы в папку folder1
folder1.add_file(file1)
folder1.add_file(file2)

# Добавляем папку folder1 в папку folder2
folder2.add_file(folder1)

# Выводим содержимое файлов и папок с помощью функции ls()
print(ls(folder1))

