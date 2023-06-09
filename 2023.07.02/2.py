import datetime
import numbers
from decimal import Decimal


class PowerMeter:
    def __init__(self,
                 tariff1: numbers.Number = 6,
                 tariff2: numbers.Number = 4,
                 tariff2_starts: datetime.time = datetime.time(22),
                 tariff2_ends: datetime.time = datetime.time(6)):
        self.tariff1 = Decimal(str(tariff1))
        self.tariff2 = Decimal(str(tariff2))
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        self.power = Decimal('0').quantize(Decimal('1.00'))
        self.month = datetime.date.today().strftime("%B")
        self.charges = {self.month: self.power}

    def __repr__(self):
        return f'<PowerMeter: {float(self.power)} кВт/ч>'

    def __str__(self):
        return f'({self.month}) {self.charges[self.month]}'

    def meter(self, power: numbers.Number) -> Decimal:
        """
        Вычисляет и возвращает стоимость согласно тарифному плану, действующему в текущий момент.

        :arg power: значение потреблённой мощности.
        """
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
