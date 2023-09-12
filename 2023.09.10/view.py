""" CLI представление. """

class CLI:
    @staticmethod
    def input_email() -> str:
        return input('Введите email: ')

    @staticmethod
    def show_incorrect_message() -> None:
        print('Введен некорректный email!')

    @staticmethod
    def show_save_message() -> None:
        print('Email успешно сохранен.')
