
from .Natural import *

__all__ = ["Integer"]

POSITIVE = 2
NEGATIVE = 1
ZERO = 0

class Integer():

    def __init__(self, n: str = None):
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

    def __eq__(self, num):
        if self._sign != num._sign:
            return False
        else:
            return self._number == num._number

    def sign(self):
        # Определение положительности числа
        # Трибунский Алексей
        return self._sign

    def natural_to_integer(self, numb: Natural):
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
            a = Integer(str(self))
            a._sign = POSITIVE
            b = Natural(str(a))
            return b
        else:
            b = Natural(str(self))
            return b
    
    def to_natural(self):
        '''Модуль TRANZ_Z_N, оформил Проскуряк Влад'''
        if (self._sign != NEGATIVE):
            res = Natural(str(self))
            return res
        else:
            return Natural()

    def __mul__(self, num):
        res = self._number * num._number
        res = Integer(str(res))
        if (self._sign == POSITIVE and num._sign == NEGATIVE) or (num._sign == POSITIVE and self._sign == NEGATIVE):
            res.change_sign()
        return res

    def __add__(self, num):
        '''Модуль ADD_ZZ_Z, оформил Трибунский Алексей'''
        res = Integer("0")
        sign1 = self.sign()
        sign2 = num.sign()
        if (sign1 == 0):
            res = num
        elif (sign2 == 0):
            res = self
        elif (sign1 == 2 and sign2 == 2):
            res = Integer(str(abs(self) + abs(num)))
        elif (sign1 == 1 and sign2 == 1):
            res = Integer(str(abs(self) + abs(num))).change_sign()
        else:
            if (abs(self) > abs(num)):
                large = self
                less = num
            else:
                large = num
                less = self
            res = Integer(str(abs(large) - abs(less)))
            if (large.sign() == 1):
                res = res.change_sign()
        return res

    def __sub__(self, num):
        ''' Функция вычитания целых чисел '''
    # Показацкая Арина
        res = Integer("0")
        sign1 = self.sign()
        sign2 = num.sign()
        if (sign1 == 0):
            res = num
        elif (sign2 == 0):
            res = self
        elif (sign1 == 2 and sign2 == 2):
            if (abs(self) > abs(num)):
                res = Integer(str(abs(self) - abs(num)))
            elif (abs(self) == abs(num)):
                res = Integer(str(abs(self) - abs(num)))
            else:
                res = Integer(str(abs(num) - abs(self))).change_sign()
        elif (sign1 == 1 and sign2 == 1):
            if (abs(self) > abs(num)):
                res = Integer(str(abs(self) - abs(num))).change_sign()
            elif (abs(self) == abs(num)):
                res = Integer(str(abs(self) - abs(num))).change_sign()
            else:
                res = Integer(str(abs(num) - abs(self)))
        else:
            if (sign1 == 1):
                res = Integer(str(abs(self) + abs(num))).change_sign()
            else:
                res = Integer(str(abs(self) + abs(num)))
        return res
