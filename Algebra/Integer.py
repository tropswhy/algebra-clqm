from .Natural import *

__all__ = ["Integer"]

POSITIVE = 2
NEGATIVE = 1
ZERO = 0

class Integer():

    def __init__(self, n):
        if n is None:
            self._number = Natural()
            self._sign = ZERO
        else:
            # Число отрицательное
            if n[0] == '-':
                self._number = Natural(n[1:])
                self._sign = NEGATIVE
            # Если число не состоит из одних нулей, то оно положительное
            elif str(Natural(n)) != "0" * Natural(n)._dig_n:
                self._number = Natural(n)
                self._sign = POSITIVE
            # Число является нулём
            else:
                self._number = Natural(n)
                self._sign = ZERO

    def __str__(self):
        return "-" * (self._sign == NEGATIVE) + str(self._number)

    def natural_to_integer(self, numb):
        '''Модуль TRANS_N_Z выполнил и оформил Солодков Никита'''
        return Integer(numb)