import datetime
import numbers
from decimal import Decimal


class PowerMeter:
    """
    Описывает двух тарифный счётчик потреблённой электрической мощности.
    """
    def __init__(self,
                 tariff1: numbers.Number = 6,
                 tariff2: numbers.Number = 4,
                 tariff2_starts: datetime.time = datetime.time(22),
                 tariff2_ends: datetime.time = datetime.time(6)):
        self.tariff1: Decimal = Decimal(str(tariff1))
        self.tariff2: Decimal = Decimal(str(tariff2))
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        self.power: Decimal = Decimal('0').quantize(Decimal('1.00'))
        self.month: datetime = datetime.date.today().strftime("%B-%Y")
        self.charges: dict[datetime: Decimal] = {self.month: self.power}

    def __repr__(self):
        return f'<PowerMeter: {float(self.power)} кВт/ч>'

    def __str__(self):
        return f'({datetime.date.today().strftime("%B")}) {self.charges[self.month]}'

    def meter(self, power: numbers.Number) -> Decimal:
        """
        Вычисляет и возвращает стоимость согласно тарифному плану, действующему в текущий момент.

        :arg power: значение потреблённой мощности.
        :return: стоимость согласно тарифному плану.
        """
        power: Decimal = Decimal(str(power))
        current_time = datetime.datetime.now().time()
        self.power += power
        if self.tariff2_ends < current_time < self.tariff2_starts:
            power *= self.tariff1
        else:
            power *= self.tariff2
        self.charges[self.month] += power
        return Decimal(str(power)).quantize(Decimal('1.00'))


# >>> pm = PowerMeter()
# >>> pm.meter(5)
# >>> Decimal('30.00')
# >>> pm.meter(9)
# >>> Decimal('54.00')
# >>> pm
# >>> <PowerMeter: 14.0 кВт/ч>
# >>> print(pm)
# >>> (July) 84.00
