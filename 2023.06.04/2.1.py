from datetime import datetime, timedelta, date


def check_vacation(current_date: datetime.date) -> list[bool]:
    """
    Проверяет, содержится ли дата в списке исключаемого периода.
    :param current_date: текущая дата
    :return: bool
    """
    global vacations
    dates = []
    if 'vacations' in globals():
        for vacation in vacations:
            if vacation[0] <= current_date <= vacation[0] + vacation[1]:
                dates.append(True)
            else:
                dates.append(False)
    return dates


def check_days(current_date: datetime.date, days: list) -> bool:
    """
    Проверяет, соответствует ли текущая дата указанным дням недели.
    :param current_date: текущая дата
    :param days: день недели
    :return: bool
    """
    return current_date.isoweekday() in days


def schedule(start: datetime.date,
             *days: int | tuple[int, int, ...],
             total_days: int,
             date_format: str = '%d/%m/%Y') -> list[datetime.date, ...]:
    """
    Генерирует график проведения мероприятий.
    :param start: дата первого мероприятия
    :param days: дни недели
    :param total_days: количество занятий
    :param date_format: формат строкового представления генерируемых дат
    :return: список строковых представлений дат
    """
    result: list = []
    current_date = start

    while total_days != 0:
        if current_date.isoweekday() in days and not any(check_vacation(current_date)):
            result.append(current_date.strftime(date_format))
            total_days -= 1
        current_date += timedelta(days=1)

    return result


# >>> vacations = [
# ...     (date(2023, 5, 1), timedelta(weeks=1)),
# ...     (date(2023, 7, 17), timedelta(weeks=1)),
# ... ]
#  >>>
# >>> py321 = schedule(date(2023, 4, 1), 6, 7, total_days=77)
# >>> len(py321)
# >>> 77
# >>> py321[21:28]
# >>> ['18/06/2023', '24/06/2023', '25/06/2023', '01/07/2023', '02/07/2023', '08/07/2023', '09/07/2023']
