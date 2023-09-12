""" Управляющий модуль. """

from model import Email, FileIO
from view import CLI


class Application:
    """ Описывает взаимодействие с моделью и представлением. """

    def __init__(self):
        self.model_email: str

    def save_email(self, email: str) -> None:
        """Сохраняет переданный email адрес."""
        try:
            self.model_email = Email(email)
            FileIO.add_email(email)
            CLI.show_save_message()
        except ValueError as ex:
            CLI.show_incorrect_message()

    def run_app(self) -> None:
        """Запускает условно-бесконечный цикл получения адресов от пользователя."""
        while True:
            email = CLI.input_email()
            if email == "":
                break
            self.save_email(email)
