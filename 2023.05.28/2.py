from utils import important_message


def main() -> None:
    """
    Функция выводит текст сообщения запрошенное от пользователя.
    """
    message = input('Текст сообщения: ')
    print(important_message(message))


# >>> main()
# Текст сообщения: Python’s with statement supports the concept of a runtime context defined by a context manager. This is implemented using a pair of methods that allow user-defined classes to define a runtime context that is entered before the statement body is executed and exited when the statement ends:
#=====================================================================================================================#
#                                                                                                                     #
#       Python’s with statement supports the concept of a runtime context defined by a context manager. This is       #
#   implemented using a pair of methods that allow user-defined classes to define a runtime context that is entered   #
#                      before the statement body is executed and exited when the statement ends:                      #
#                                                                                                                     #
#=====================================================================================================================#
# >>>
# >>> text = 'Достал нож - режь. Достал хлеб - ешь.'
# >>> msg = important_message(text)
#=====================================================================================================================#
#                                                                                                                     #
#                                        Достал нож - режь. Достал хлеб - ешь.                                        #
#                                                                                                                     #
#=====================================================================================================================#