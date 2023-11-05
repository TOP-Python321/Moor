from utils_ref import important_message


def main() -> None:
    text = input('текст сообщения: ')
    text = important_message(text)
    print(f"\n{text}\n")


# >>> main()
# текст сообщения: На шишкосушильную фабрику требуется шишкосушильщик для работы на шишкосушильном аппарате. Шишкосушильщик должен иметь опыт шишкосушения на шишкосушильном аппарате с использованием шишкосушильной технологии качественного шишкосушения. Он также должен отличать аппарат шишкосушения от нешишкосушения, ремонтировать шишкосушильный аппарат, отличать шишки, пригодные для шишкосушения, от негодных для шишкосушения, отличать шишки недошишкосушенные от перешишкосушенных, за каждую недошишкосушенную или перешишкосушенную шишку шишкосушильщик получит шишкосушилкой по голове.
# 
# #=============================================================================#
# #                                                                             #
# #       На шишкосушильную фабрику требуется шишкосушильщик для работы на      #
# #  шишкосушильном аппарате. Шишкосушильщик должен иметь опыт шишкосушения на  #
# #      шишкосушильном аппарате с использованием шишкосушильной технологии     #
# #  качественного шишкосушения. Он также должен отличать аппарат шишкосушения  #
# #   от нешишкосушения, ремонтировать шишкосушильный аппарат, отличать шишки,  #
# #   пригодные для шишкосушения, от негодных для шишкосушения, отличать шишки  #
# #   недошишкосушенные от перешишкосушенных, за каждую недошишкосушенную или   #
# #   перешишкосушенную шишку шишкосушильщик получит шишкосушилкой по голове.   #
# #                                                                             #
# #=============================================================================#
# 
# >>> text = 'ЗАГОЛОВОК ПРОГРАММЫ'
# >>> print(important_message(text))
# #=============================================================================#
# #                                                                             #
# #                             ЗАГОЛОВОК ПРОГРАММЫ                             #
# #                                                                             #
# #=============================================================================#