from datetime import date
from json import dump
from random import choice, sample, randrange as rr, uniform
from pathlib import Path
from re import compile
from string import digits, ascii_uppercase, ascii_lowercase
from sys import path


DATA_DIR = Path(path[0]) / 'data'

pattern1 = compile(r'\W+')

names = {
    'имена': {'мужской': [], 'женский': []},
    'отчества': {'мужской': [], 'женский': []},
    'фамилии': {'мужской': [], 'женский': []},
}
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def load_data() -> None:
    m_names_path = DATA_DIR / 'мужские_имена_отчества.txt'
    f_names_path = DATA_DIR / 'женские_имена.txt'
    lastnames_path = DATA_DIR / 'фамилии.txt'

    names['имена']['женский'] = f_names_path.read_text(encoding='utf-8').split('\n')

    raw_m_names = m_names_path.read_text(encoding='utf-8').split('\n')
    for line in raw_m_names:
        name, pat_m, pat_f, *_ = pattern1.split(line)
        names['имена']['мужской'] += [name]
        names['отчества']['мужской'] += [pat_m]
        names['отчества']['женский'] += [pat_f]

    raw_lastnames = lastnames_path.read_text(encoding='utf-8').split('\n')
    for line in raw_lastnames:
        try:
            lastn_m, lastn_f = line.split(', ')
        except ValueError:
            lastn_m = lastn_f = line
        names['фамилии']['мужской'] += [lastn_m]
        names['фамилии']['женский'] += [lastn_f]


def generate_person(year_start: int = None, year_end: int = None) -> dict:
    sex = choice(('мужской', 'женский'))
    if year_end is None:
        year_end = date.today().year
    if year_start is None:
        year_start = year_end - 100
    rand_year = rr(year_start, year_end)
    rand_month = rr(1, 13)
    leap_febr = rand_month == 2 and is_leap_year(rand_year)
    max_day = days[rand_month]+1 if leap_febr else days[rand_month]
    rand_day = rr(1, max_day+1)
    mob_num = ''.join(sample(digits, k=9))
    return {
        'last_name': choice(names['фамилии'][sex]),
        'first_name': choice(names['имена'][sex]),
        'patr_name': choice(names['отчества'][sex]),
        'sex': sex,
        'birthdate': date(rand_year, rand_month, rand_day).strftime('%d.%m.%Y'),
        'contacts': f'+79{mob_num}',
    }


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def dump_students_list(n: int = 1500):
    students = [
        generate_person(2004, 2007) | {
            'student_id': ''.join(sample(ascii_uppercase + digits, k=12)),
            'grant': choice(('0.0', '2550.00', '2550.00', '2550.00')),
        }
        for _ in range(n)
    ]
    with open(DATA_DIR / f'students.json', 'w', encoding='utf-8') as json_file:
        dump(students, json_file, ensure_ascii=False, indent=2)


def dump_teachers_list(n: int = 1500):
    teachers = [
        generate_person(1958, 2001) | {
            'id_': int(''.join(sample(digits, k=8))),
            'salary': rr(30000, 60000, 690),
            'degree': sample((None, 'кандидат наук', 'доктор наук'), counts=[5, 4, 1], k=1)[0],
            'titles': None,
            'previous_experience': str(round(uniform(0, 45), 1)),
            'courses': [
                ''.join(sample(ascii_lowercase, k=rr(6,10)))
                for _ in range(rr(4))
            ],
        }
        for _ in range(n)
    ]
    with open(DATA_DIR / f'teachers.json', 'w', encoding='utf-8') as json_file:
        dump(teachers, json_file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    load_data()
    dump_students_list(100)
    dump_teachers_list(20)
