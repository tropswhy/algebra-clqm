
from .Natural import *

__all__ = ["Integer", "POSITIVE", "NEGATIVE", "ZERO"]

POSITIVE = 2
NEGATIVE = 1
ZERO = 0

class Integer():

    # _number - "натуральная часть" числа
    # _sign - знак целого числа: 2 - положительное, 1 - отрицательное, 0 - ноль
    def __init__(self, n: str = None):
        if not n:
            self._number = Natural()
            self._sign = ZERO
        elif not Integer.isInteger(n):
            raise Exception("number passed to \"Integer\" class constructor is invailid")
        else:
            # Если число отрицательное
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

    @staticmethod
    def isInteger(s):
        i = 1 if s[0] == '-' else 0
        return Natural.isNatural(s[i:])

    def __str__(self):
        return "-" * (self._sign == NEGATIVE) + str(self._number)

    def __eq__(self, num):
        if self._sign != num._sign:
            return False
        else:
            return self._number == num._number

    def __gt__(self, num):
        # Если знаки одинаковые, то придётся сравнивать числа поразрядно
        if self._sign == num._sign:
            if self._sign == POSITIVE:
                return self._number > num._number
            else:
                return self._number < num._number
        # Иначе, достаточно сравнить знаки
        elif self._sign != ZERO and num._sign != ZERO:
            return self._sign > num._sign
        elif self._sign == ZERO:
            return num._sign == NEGATIVE
        else: #num._sign == ZERO
            return self._sign == POSITIVE

    def __lt__(self, num):
        # Если знаки одинаковые, то придётся сравнивать числа поразрядно
        if self._sign == num._sign:
            if self._sign == POSITIVE:
                return self._number < num._number
            else:
                return self._number > num._number
        # Иначе, достаточно сравнить знаки
        elif self._sign != ZERO and num._sign != ZERO:
            return self._sign < num._sign
        elif self._sign == ZERO:
            return num._sign == POSITIVE
        else:  # num._sign == ZERO
            return self._sign == NEGATIVE

    def is_zero(self):
        return self._number.is_zero()

    '''МОДУЛИ INTEGER'''

    def __abs__(self):
        '''Модуль Z-1 ABS_Z_N. Выполнила и оформила Реброва Юлия'''

        if self._sign == NEGATIVE:
            a = Integer(str(self))
            a._sign = POSITIVE
            res = Natural(str(a))
            return res
        else:
            res = Natural(str(self))
            return res

    def sign(self):
        '''Модуль Z-2 POZ_Z_D. Выполнил и оформил Трибунский Алексей'''

        return self._sign

    def change_sign(self):
        '''Модуль Z-3 MUL_ZM_Z. Выполнила и оформила Показацкая Арина'''

        if self._sign == NEGATIVE:
            self._sign = POSITIVE
        elif self._sign == POSITIVE:
            self._sign = NEGATIVE
        return self

    @staticmethod
    def natural_to_integer(natural):
        '''Модуль Z-4 TRANS_N_Z. Выполнил и оформил Солодков Никита'''

        return Integer(str(natural))

    @staticmethod
    def to_natural(integer):
        '''Модуль Z-5 TRANZ_Z_N. Выполнил и оформил Проскуряк Влад'''

        if (integer._sign != NEGATIVE):
            res = Natural(str(integer))
            return res
        else:
            raise Exception("negative number cannot be converted into natural")

    def __add__(self, num):
        '''Модуль Z-6 ADD_ZZ_Z. Выполнил и оформил Трибунский Алексей'''

        sign1 = self.sign()
        sign2 = num.sign()
        # Если первое число - нуль, то выводим второе число
        if (sign1 == ZERO):
            return Integer(str(num))
        # Если второе число - нуль, то выводим первое число
        elif (sign2 == ZERO):
            return Integer(str(self))
        # Если оба числа положительные, то выводим сумму их модулей
        elif (sign1 == POSITIVE and sign2 == POSITIVE):
            return Integer(str(abs(self) + abs(num)))
        # Если оба числа отрицательные, то выводим сумму их модулей с минусом
        elif (sign1 == NEGATIVE and sign2 == NEGATIVE):
            return Integer(str(abs(self) + abs(num))).change_sign()
        # Если модуль первого числа больше модуля второго числа, то large присваиваем значение первого числа, а less - второго
        if (abs(self) > abs(num)):
            large = self
            less = num
        # Если модуль первого числа меньше модуля второго числа, то large присваиваем значение второго числа, а less - первого
        else:
            large = num
            less = self
        # Из большего числа вычитаем меньшее
        res = Integer(str(abs(large) - abs(less)))
        # Если большее число отрицательное, то меняем знак
        if (large.sign() == 1):
            res = res.change_sign()
        return res

    def __sub__(self, num):
        '''Модуль Z-7 SUB_ZZ_Z. Выполнила и оформила Показацкая Арина'''

        res = Integer("0")
        sign1 = self.sign()
        sign2 = num.sign()

        # Проверка на нули
        if (sign1 == ZERO):
            res = Integer(str(num))
        elif (sign2 == ZERO):
            res = Integer(str(self))

        # Если оба числа положительные
        # то из большего вычитаем меньшее
        elif (sign1 == POSITIVE and sign2 == POSITIVE):
            compare = abs(self).compare(abs(num))
            if compare != 1:
                res = Integer(str(abs(self) - abs(num)))
            else:
                res = Integer(str(abs(num) - abs(self))).change_sign()
        # Если оба числа отрицательные,
        # то из модуля большего числа вычитаем модуль меньшего
        elif (sign1 == NEGATIVE and sign2 == NEGATIVE):
            # если результат отличен от нуля, меняем знак
            compare = abs(self).compare(abs(num))
            if compare != 1:
                res = Integer(str(abs(self) - abs(num))).change_sign()
            else:
                res = Integer(str(abs(num) - abs(self)))
        # Если числа с разными знаками
        else:
            # Если отрицательно первое, складываем модули и меняем знак
            if (sign1 == NEGATIVE):
                res = Integer(str(abs(self) + abs(num))).change_sign()
            # Если отрицательно второе, складываем модули чисел
            else:
                res = Integer(str(abs(self) + abs(num)))

        return res

    def __mul__(self, num):
        '''Модуль Z-8 MUL_ZZ_Z. Выполнил и оформил Жексенгалиев Адиль'''

        # Проверка на ноль
        if self.is_zero() or num.is_zero():
            return Integer("0")

        res = Integer()
        res._number = self._number * num._number
        res._sign = POSITIVE
        # Если знаки self и num отличаются
        if self._sign != num._sign:
            res.change_sign()

        return res

    def __truediv__(self, num):
        '''Модуль Z-9 DIV_ZZ_Z. Выполнил и оформил Солодков Никита'''

        # Проверка на ноль
        if num.is_zero():
            raise Exception("unable to divide by zero")
        elif self.is_zero():
            return Integer("0")

        res = Integer()
        divisible = Integer(str(self))
        divisor = Integer(str(num))
        # Делим число без учета знака
        res._number = divisible._number / divisor._number
        # Определение знака частного
        if divisible._sign == divisor._sign:
            # Если у делимого и делителя одинаковые знаки, то у частного будет положительный знак
            res._sign = POSITIVE
            # Если делимое и делитель - отрицательный числа, то добавляем к частному единицу
            if (divisible._sign == NEGATIVE):
                res += Integer("1")
        elif divisible._sign != ZERO:
            # В ином случае знак будет отрицательный.
            res._sign = NEGATIVE
            # Если остаток больше нуля и делимое меньше нуля, то вычитаем из полученного частного единицу
            if (divisible._number % divisor._number > Natural("0")) and (divisible._sign == NEGATIVE):
                res -= Integer("1")
        # Если частное по модулю равно нулю, то присваиваем знаку числа значение ZERO
        if (res._number == Natural("0")):
            res._sign = ZERO
        return res

    def __mod__(self, num):
        '''Модуль Z-10 MOD_ZZ_Z. Выполнил и оформил Щусь Максим'''

        # Проверка на ноль
        if num._number.is_zero():
            raise Exception("unable to find modulo by zero")

        z1 = Integer(str(self))
        z2 = Integer(str(num))
        div = (z1 / z2)

        return z1 - z2 * div
