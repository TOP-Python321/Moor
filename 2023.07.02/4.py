from pathlib import Path
import csv


class CountableNouns:
    """
    Предоставляет интерфейс для работы с файловой базой существительных.
    """
    db_path = Path('words.csv')
    words: dict[str, tuple[str, str]] = {}
    with open(db_path, encoding='utf-8') as csvfile:
        db_reader = csv.reader(csvfile)
        for row in db_reader:
            words.update({row[0]: (row[1], row[2])})

    @classmethod
    def pick(cls, number: str, word: str) -> str:
        """
        Проверяет существительное на наличие в базе. При его отсутствии - согласовывает его с единственным числом.

        :param number: Число, с которым нужно согласовать.
        :param word: Существительное для согласования в единственном числе.
        :return: Согласованное с переданным числом существительное.
        """
        if str(number)[-1] == '1' and word not in cls.words:
            cls.words[word] = tuple()
            return word
        elif word in cls.words and cls.words[word]:
            return cls.words[word][0] if str(number)[-1] in ['2', '3', '4'] else cls.words[word][1]
        else:
            print(f'существительное "{word}" отсутствует в базе')
            cls.save_words(word)

    @classmethod
    def save_words(cls, word1: str = None) -> None:
        """
        Добавляет полученные значения в поле класса words и дописывает их в файл с базой существительных.

        :param word1: Существительное для согласования во множественном числе.
        :return: None
        """
        if word1 is None:
            word1 = input("введите слово, согласующееся с числительным 'один': ")
            cls.words[word1] = tuple()
        noun2 = input("введите слово, согласующееся с числительным 'два': ")
        noun5 = input("введите слово, согласующееся с числительным 'пять': ")
        cls.words[word1] = (noun2, noun5)
        with open(cls.db_path, 'w', newline='', encoding='utf-8') as csvfile:
            db_writer = csv.writer(csvfile, lineterminator='\n')
            for key in cls.words.keys():
                db_writer.writerow([key, *cls.words[key]])


# >>> CountableNouns.words
# >>> {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней')}
# >>> CountableNouns.pick(26, 'год')
# >>> 'лет'
# >>> CountableNouns.pick(1948, 'день')
# >>> 'дней'
# >>> CountableNouns.pick(21, 'река')
# >>> 'река'
# >>> CountableNouns.pick(22, 'река')
# >>> существительное "река" отсутствует в базе
# >>> введите слово, согласующееся с числительным 'два': >? реки
# >>> введите слово, согласующееся с числительным 'пять': >? рек
# >>>
# >>> CountableNouns.words
# >>> {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'река': ('реки', 'рек')}
# >>>
# >>> CountableNouns.save_words()
# >>> введите слово, согласующееся с числительным 'один': >? носок
# >>> введите слово, согласующееся с числительным 'два': >? носка
# >>> введите слово, согласующееся с числительным 'пять': >? носков
# >>>
# >>> print(CountableNouns.db_path.read_text(encoding='utf-8'))
# >>> год,года,лет
# >>> месяц,месяца,месяцев
# >>> день,дня,дней
# >>> река,реки,рек
# >>> носок,носка,носков
