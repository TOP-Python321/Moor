from abc import ABC, abstractmethod
from random import randrange as rr, sample
from string import ascii_lowercase as letters


class TestCase:
    """
    Адресат.
    """

    def __init__(self):
        self.messages = [
            ''.join(sample(letters, k=rr(3, 7)))
            for _ in range(1000)
        ]
        self.numbers = [
            (rr(10, 100) for _ in range(rr(4, 6)))
            for _ in range(1000)
        ]

    def print_msg(self):
        msg = self.messages.pop()
        print(msg)

    def print_nums(self):
        nums = self.numbers.pop()
        print(*nums)


class Command(ABC):
    """Абстрактный класс команды."""
    @abstractmethod
    def execute(self):
        raise NotImplementedError()

    @abstractmethod
    def undo(self):
        raise NotImplementedError()

    @abstractmethod
    def redo(self):
        raise NotImplementedError()


class PrintMessageCommand(Command):
    """Команда для печати сообщения."""

    def __init__(self, test_case):
        self.test_case: TestCase = test_case
        self.message = None

    def execute(self):
        """
        Выполнение команды
        """
        self.message = self.test_case.messages.pop()
        print(self.message)

    def undo(self):
        """
        Отмена команды
        """
        self.test_case.messages.append(self.message)

    def redo(self):
        """
        Повторное выполнение последней команды
        """
        self.execute()


class PrintNumbersCommand(Command):
    """Команда для печати чисел."""

    def __init__(self, test_case):
        self.test_case: TestCase = test_case
        self.numbers = None

    def execute(self):
        """
        Выполнение команды
        """
        self.numbers = self.test_case.numbers.pop()
        print(*self.numbers)

    def undo(self):
        """
        Отмена команды
        """
        self.test_case.numbers.append(self.numbers)

    def redo(self):
        """
        Повторное выполнение последней команды
        """
        self.execute()


class CommandManager:
    """Класс управления командами."""

    def __init__(self):
        self.commands: list[Command] = []
        self.undo_stack: list[Command] = []
        self.redo_stack: list[Command] = []

    def execute_command(self, command: Command):
        """
        Выполнение команды
        """
        command.execute()
        self.commands.append(command)
        self.redo_stack.clear()

    def undo_last_command(self):
        """
        Отмена последней команды
        """
        if self.commands:
            command = self.commands.pop()
            command.undo()
            self.undo_stack.append(command)

    def redo_last_command(self):
        """
        Повторное выполнение последней отмененной команды
        """
        if self.undo_stack:
            command = self.undo_stack.pop()
            command.redo()
            self.redo_stack.append(command)


# >>> test_case = TestCase()
# >>> command_manager = CommandManager()
# >>> print_msg = PrintMessageCommand(test_case)
# >>> print_nums = PrintNumbersCommand(test_case)
# >>> command_manager.execute_command(print_msg)
# rfabhc
# >>>
# >>> command_manager.execute_command(print_nums)
# 45 43 32 91 42
# >>>
# >>> command_manager.commands
# [<__main__.PrintMessageCommand object at 0x00000232D737FB10>, <__main__.PrintNumbersCommand object at 0x00000232D737FD10>]
# >>>
# >>> command_manager.undo_last_command()
# >>> command_manager.commands
# [<__main__.PrintMessageCommand object at 0x00000232D737FB10>]