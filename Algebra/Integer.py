
from .Natural import *

__all__ = ["Integer"]

POSITIVE = 2
NEGATIVE = 1
ZERO = 0

class Integer():

    def __init__(self, n = None):
        # Если число не было передано в качестве аргумента
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


    def sign(self):
        # Определение положительности числа
        # Трибунский Алексей
        return self._sign

    def natural_to_integer(self, numb):
        '''Модуль TRANS_N_Z выполнил и оформил Солодков Никита'''
        return Integer(numb)

    def change_sign(self):
        ''' Функция умножения целого числа на -1'''
    # Показацкая Арина
        if self._sign == NEGATIVE:
            self._sign = POSITIVE
        elif self._sign == POSITIVE:
            self._sign = NEGATIVE
        return self

    def __abs__(self):
        '''Модуль ABS_Z_N выполнила и оформила Реброва Юлия'''
        if self._sign == NEGATIVE:
            a = Integer(self)
            a._sign = POSITIVE
            b = Natural(str(a))
            return b
        else:
            b = Natural(str(self))
            return b
