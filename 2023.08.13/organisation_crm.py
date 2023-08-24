from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date, datetime as dt, timedelta
from decimal import Decimal as dec
from enum import Enum
from typing import Literal


@dataclass
class Contact:
    mobile: str = None
    office: str = None
    email: str = None


class Person(ABC):
    """
    Абстрактный класс, представляющий человека.
    """
    class Sex(Enum):
        MALE = 'мужской'
        FEMALE = 'женский'

    _default_date_format: str = '%d.%m.%Y'

    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            sex: Sex,
            birthdate: date | str | tuple[str, str],
            contacts: Contact,
    ):
        """
        Инициализирует объект Person.

        :param last_name: Фамилия
        :param first_name: Имя
        :param patr_name: Отчество
        :param sex: Пол (Sex.MALE - мужской, Sex.FEMALE - женский)
        :param birthdate: Дата рождения в формате дд.мм.гггг или кортеж (дата, формат)
        :param contacts: Контактные данные
        """
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name
        self.__fio: str = f'{self.last_name} {self.first_name} {self.patr_name}'
        self.sex = sex
        if isinstance(birthdate, tuple):
            try:
                date_, format_ = birthdate
                assert isinstance(date_, str)
                assert isinstance(format_, str)
            except (ValueError, AssertionError):
                raise  # собственное исключение
            else:
                birthdate = dt.strptime(*birthdate)
        elif isinstance(birthdate, str):
            birthdate = dt.strptime(birthdate, self._default_date_format)
        self.birthdate: date = birthdate
        self.contacts = contacts

    @property
    def fio(self):
        """
        Полное имя человека.

        :return: Полное имя
        """
        return self.__fio

    def change_name(
            self,
            new_name: str,
            name_part: Literal['last', 'first', 'patr']
    ):
        """
        Изменяет одну из частей имени человека.

        :param new_name: Новое значение
        :param name_part: Часть имени, которую нужно заменить
        """
        setattr(self, f'{name_part}_name', new_name)
        self.__fio = f'{self.last_name} {self.first_name} {self.patr_name}'

    @abstractmethod
    def __str__(self):
        pass


class Personnel(Person):
    """
    Класс, представляющий персонал.
    """

    class Degree(Enum):
        CANDIDATE = 'кандидат наук'
        DOCTOR = 'доктор наук'

    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            sex: Person.Sex,
            birthdate: date | str | tuple[str, str],
            contacts: Contact,
            id_: int,
            salary: dec,
            degree: Degree | None = None,
            titles: list[str] = None,
            previous_experience: dec = dec(0),
    ):
        """
        Инициализирует объект Pesonel.

        :param last_name: Фамилия
        :param first_name: Имя
        :param patr_name: Отчество
        :param sex: Пол (Sex.MALE - мужской, Sex.FEMALE - женский)
        :param birthdate: Дата рождения в формате дд.мм.гггг или кортеж (дата, формат)
        :param contacts: Контактные данные
        :param id_: Идентификатор
        :param salary: Заработная плата
        :param degree: Ученая степень
        :param titles: Звание
        :param previous_experience: Предыдущий опыт работы (в годах)
        """
        super().__init__(
            last_name,
            first_name,
            patr_name,
            sex,
            birthdate,
            contacts
        )
        self.id = id_
        self.salary = salary
        self.degree = degree
        if titles is None:
            titles = []
        self.titles = titles
        self.job_start: date = date.today()
        self._exp = previous_experience

    @property
    def exp(self) -> dec:
        """
        Вычисляет полный стаж работы.

        :return: Стаж работы
        """
        return self._exp + dec((date.today() - self.job_start).days / 365.25)


class Administrator(Personnel):
    """
    Класс, представляющий администратора.
    """
    def __str__(self):
        return f'<Administrator: {self.fio}>'


class Teacher(Personnel):
    """
    Класс, представляющий учителя.
    """
    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            sex: Person.Sex,
            birthdate: date | str | tuple[str, str],
            contacts: Contact,
            id_: int,
            salary: dec,
            courses: list[str],
            degree: Personnel.Degree | None = None,
            titles: list[str] = None,
            previous_experience: dec = dec(0)
    ):
        """
        Инициализирует объект Teacher.

        :param last_name: Фамилия
        :param first_name: Имя
        :param patr_name: Отчество
        :param sex: Пол (Sex.MALE - мужской, Sex.FEMALE - женский)
        :param birthdate: Дата рождения в формате дд.мм.гггг или кортеж (дата, формат)
        :param contacts: Контактные данные
        :param id_: Идентификатор
        :param salary: Заработная плата
        :param courses: Курсы, которые ведет учитель
        :param degree: Ученая степень
        :param titles: Звание
        :param previous_experience: Предыдущий опыт работы (в годах)
        """
        super().__init__(
            last_name,
            first_name,
            patr_name,
            sex,
            birthdate,
            contacts,
            id_,
            salary,
            degree,
            titles,
            previous_experience
        )
        self.courses = courses

    def __str__(self):
        return f'<Teacher: {self.fio}>'


class Student(Person):
    """
    Класс, представляющий студента.
    """
    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            sex: Person.Sex,
            birthdate: date | str | tuple[str, str],
            contacts: Contact,
            student_id: str,
            grant: dec = dec(0),
    ):
        """
        Инициализирует объект Student.

        :param last_name: Фамилия
        :param first_name: Имя
        :param patr_name: Отчество
        :param sex: Пол (Sex.MALE - мужской, Sex.FEMALE - женский)
        :param birthdate: Дата рождения в формате дд.мм.гггг или кортеж (дата, формат)
        :param contacts: Контактные данные
        :param student_id: Идентификатор
        :param grant: Степендия
        """
        super().__init__(
            last_name,
            first_name,
            patr_name,
            sex,
            birthdate,
            contacts
        )
        self.student_id = student_id
        self.grant = grant

    def __str__(self):
        return f'<Student: {self.fio}>'


class Group(list):
    """
    Класс, представляющий группу студентов.
    """
    def __init__(self, semester: int, curator: Teacher, head: Student):
        """
        Инициализирует объект Group

        :param semester: Семестр
        :param curator: Куратор из числа учителей
        :param head: Староста из числа студентов
        """
        super().__init__()
        self.semester = semester
        self.curator = curator
        self.head = head

    def promote(self):
        """
        Переводит студентов на следующий семестр, если средняя оценка соответствует.
        """
        super().__init__([elem for elem in self if elem.grade > sum([2, 3, 4, 5]) / 4])
        self.semester += 1


class Organization(list):
    """
    Класс, представляющий организацию.
    """
    def __init__(self, title: str, head: Administrator, contacts: Contact):
        """
        Инициализирует объект Organization.

        :param title: Название
        :param head: Администратор
        :param contacts: Контактные данные
        """
        super().__init__()
        self.title = title
        self.head = head
        self.contacts = contacts

    def hire(self, personnel: Personnel) -> None:
        """
        Нанимает сотрудника.

        :param personnel: Объект класса Personnel
        """
        self.append(personnel)

    def fire(self, personnel: Personnel) -> None:
        """
        Увольняет сотрудника.

        :param personnel: Объект класса Personnel
        """
        if personnel in self:
            self.remove(personnel)


class Laboratory(Organization):
    """
    Класс, представляющий лабораторию.
    """
    def __init__(
            self,
            title: str,
            head: Administrator,
            contacts: Contact,
            equipment: list[str],
            schedule: list[dict[dt, timedelta]]
    ):
        """
        Инициализирует объект Laboratory.

        :param title: Название
        :param head: Администратор
        :param contacts: Контактные данные
        :param equipment: Список оборудования
        :param schedule: Расписание, представленное списком словарей (дата и время начала занятия и продолжительность)
        """
        super().__init__(title, head, contacts)
        self.equipment = equipment
        self.schedule = schedule


class Department(Organization):
    """
    Класс, представляющий кафедру.
    """
    def __init__(
            self,
            title: str,
            head: Administrator,
            contacts: Contact,
            groups: list[Group]
    ):
        """
        Инициализирует объект Department.

        :param title: Название кафедры
        :param head: Администратор
        :param contacts: Контактные данные
        :param groups: Список групп, принадлежащих кафедре
        """
        super().__init__(title, head, contacts)
        self.groups = groups


class Institute(Organization):
    """
    Класс, представляющий институт.
    """
    def __init__(
            self,
            title: str,
            head: Administrator,
            contacts: Contact,
            department: list[Department],
            labs: list[Laboratory]
    ):
        """
        Инициализирует объект Institute.

        :param title: Название
        :param head: Администратор
        :param contacts: Контактные данные
        :param department: Список кафедр
        :param labs: Список лабораторий
        """
        super().__init__(title, head, contacts)
        self.department = department
        self.labs = labs


class University(Organization):
    """
    Класс, представляющий университет.
    """
    def __init__(
            self,
            title: str,
            head: Administrator,
            contacts: Contact,
            institutes: list[Institute]
    ):
        """
        Инициализирует объект University.

        :param title: Название
        :param head: Администратор
        :param contacts: Контактные данные
        :param institutes: Список институтов
        """
        super().__init__(title, head, contacts)
        self.institutes = institutes


s1 = Student('Moor', 'Alexander', 'Nikolaevich', Person.Sex.MALE, '27.06.1990', Contact('9370777130'), '12345678')
t1 = Teacher('Ivanov', 'Ivan', 'Ivanovich', Person.Sex.MALE, '01.01.1967', Contact('9370777140'), 92883,
             dec('32000.00'), ['math', 'info'])
