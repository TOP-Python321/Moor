class SIUnit:
    """Представление значений в удобочитаемом виде с корректировкой приставок СИ."""
    __prefixes = {0: '', 3: 'k', 6: 'M', 9: 'G', 12: 'T', 15: 'P', 18: 'E', 21: 'Z', 24: 'Y',
                  -3: 'm', -6: 'μ', -9: 'n', -12: 'p', -15: 'f', -18: 'a', -21: 'z', -24: 'y'}
    __exponents = {v: k for k, v in __prefixes.items()}
    
    def __init__(self, number, unit='', *, start_exp=0, digits=None):
        self.number = number
        self.__unit = unit
        self.__start_exp = start_exp
        for k in range(-24, 25, 3):
            r_number = number / 10**k
            if 0 < r_number < 1000:
                self.readable = r_number if digits is None else round(r_number, digits)
                self.readable_unit = f"{self.__class__.__prefixes[k+start_exp]}{unit}"
                break
    
    def __str__(self):
        if self.__unit:
            return f"{self.readable} {self.readable_unit}"
        else:
            exp = self.__class__.__exponents[self.readable_unit]
            return f"{self.readable:.1f}\u00b710^{exp}"
    
    def target(self, target_exp):
        t_number = self.number * 10**(target_exp+self.__start_exp)
        t_unit = f"{self.__class__.__prefixes[target_exp]}{self.__unit}"
        return f"{t_number} {t_unit}"


if __name__ == '__main__':

    v1 = SIUnit(123734345)
    print(v1)

    v2 = SIUnit(2364, 'eV', start_exp=3, digits=1)
    print(v2)

    v3 = SIUnit(0.00003215)
    print(v3)

    v4 = SIUnit(0.000000000358, 's')
    print(v4)


