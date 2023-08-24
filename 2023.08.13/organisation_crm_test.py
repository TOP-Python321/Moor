from datetime import date
from decimal import Decimal as dec
from json import loads
from pathlib import Path
from pprint import pprint
from random import randrange as rr
from re import compile
from sys import path

import organisation_crm as model


data_students = Path(path[0]) / 'data/students.json'
data_teachers = Path(path[0]) / 'data/teachers.json'

data_students = loads(data_students.read_text(encoding='utf-8'))
data_teachers = loads(data_teachers.read_text(encoding='utf-8'))


students, teachers = [], []
for entry in data_students:
    entry['sex'] = model.Person.Sex(entry['sex'])
    entry['contacts'] = model.Contact(mobile=entry['contacts'])
    if rr(10):
        entry['grant'] = dec(entry['grant'])

    try:
        assert isinstance(entry['grant'], dec)
    except AssertionError:
        print()
        pprint(entry, sort_dicts=False)
    else:
        students.append(model.Student(**entry))

for entry in data_teachers:
    entry['sex'] = model.Person.Sex(entry['sex'])
    entry['contacts'] = model.Contact(mobile=entry['contacts'])
    entry['salary'] = dec(f"{entry['salary']}.0")
    if entry['degree'] is not None:
        entry['degree'] = model.Personnel.Degree(entry['degree'])
    entry['previous_experience'] = dec(entry['previous_experience'])
    teachers.append(model.Teacher(**entry))


pat_fio = compile(r'\w+ \w+ \w+')

for i, teacher in enumerate(teachers):
    try:
        assert pat_fio.fullmatch(teacher.fio)
    except AssertionError:
        print(teacher.fio)

    work_age = date.today().year - teacher.birthdate.year - 23
    try:
        assert work_age > teacher.exp
    except AssertionError:
        print(f'\n{i=}, {teacher}\n'
              f'\t{work_age} лет работы, {teacher.exp} лет стажа')
