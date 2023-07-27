from datetime import datetime as dt
from pathlib import Path
from random import randrange, choice, randint, sample, choices
import re
import string


female: Path = Path('женские_имена.txt')
male_patronymic: Path = Path('мужские_имена_отчества.txt')
surnames: Path = Path('фамилии.txt')

names: dict[str, list[str]] = {}


def load_data() -> None:
    """
    Читает из файлов данные и упорядочивает их.
    :return: None
    """
    with open(female, 'r', encoding='utf-8') as file:
        names['female_names'] = [name.strip() for name in file]
    with open(male_patronymic, "r", encoding='utf-8') as f:
        file = f.read()
        regex = r'(.*)\((.*), (.*)\)'
        data: list = re.findall(regex, file)
        names['male_names'] = [name[0] for name in data]
        names['male_patronymics'] = [patron[1] for patron in data]
        names['female_patronymics'] = [patron[2] for patron in data]
    with open(surnames, 'r', encoding='utf-8') as file:
        surnames_data = [line.strip().split(', ') for line in file]
        names['male_surnames'] = [surname[0] for surname in surnames_data]
        names['female_surnames'] = [surname[1] if len(surname) > 1 else surname[0] for surname in surnames_data]


def generate_date() -> str:
    """
    Генерирует случайную дату рождения.
    :return: Дата рождения
    """
    current_year: int = dt.now().year
    start_year: int = current_year - 100

    random_year: int = randint(start_year, current_year)
    random_month: int = randint(1, 11)
    days_in_month: int = (dt(random_year, random_month + 1, 1) - dt(random_year, random_month, 1)).days
    random_day: int = randint(1, days_in_month)

    return dt(random_year, random_month, random_day).strftime('%Y-%m-%d')


def generate_email() -> str:
    """
    Генерирует случайную электронную почту.
    :return: email
    """
    domain: list[str] = ['gmail.com', 'yandex.ru', 'mail.ru', 'rambler.ru', 'hotmail.com', 'msn.com']
    username_length: int = randint(5, 10)
    username: str = ''.join(choices(string.ascii_lowercase, k=username_length))
    domain_name: str = choice(domain)
    email: str = f"{username}@{domain_name}"
    return email


def generate_person() -> dict[str: str]:
    """
    Генерирует анкету человека со случайными данными.
    :return: анкета человека
    """
    random_date: str = generate_date()
    mail: str = generate_email()
    number: str = ''.join(sample('0123456789', k=9))
    person: dict = {
        'имя': choice(names['female_names']),
        'отчество': choice(names['female_patronymics']),
        'фамилия': choice(names['female_surnames']),
        'пол': 'женский',
        'дата рождения': random_date,
        'электронная почта': mail,
        'мобильный': f'+79{number}'
    }
    if randrange(2):
        person['имя'] = choice(names['male_names'])
        person['отчество'] = choice(names['male_patronymics'])
        person['фамилия'] = choice(names['male_surnames'])
        person['пол'] = 'мужской'
    return person

# >>> from pprint import pprint
# >>>
# >>> load_data()
# >>>
# >>> pprint(generate_person(), sort_dicts=False)
# {'имя': 'Лукреция',
#  'отчество': 'Харламповна',
#  'фамилия': 'Думчева',
#  'пол': 'женский',
#  'дата рождения': '1953-07-06',
#  'электронная почта': 'aburbucx@msn.com',
#  'мобильный': '+79719208456'}
# >>>
# >>> pprint(generate_person(), sort_dicts=False)
# {'имя': 'Меркул ',
#  'отчество': 'Софониевич',
#  'фамилия': 'Ядрышников',
#  'пол': 'мужской',
#  'дата рождения': '1970-10-04',
#  'электронная почта': 'uzvuo@gmail.com',
#  'мобильный': '+79497058316'}
