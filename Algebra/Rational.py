
from .Natural import *
from .Integer import *

__all__ = ["Rational"]

class Rational():

    def __init__(self, n: str = None):
        if not n:
            self._numerator = Integer("0")
            self._denumerator = Natural("0")
        elif not Rational.isRational(n):
            raise Exception("number passed to \"Rational\" class constructor is invailid")
        else:
            k = n.find("/")
            if k == -1:
                self._numerator = Integer(n)
                self._denumerator = Natural("1" if self._numerator != Integer("0") else "0")
            else:
                num = n[:k]
                denum = n[k + 1:]
                self._numerator = Integer(num)
                self._denumerator = Natural(denum)
                if self._numerator == Integer("0"):
                    self._numerator = Integer("0")
                    self._denumerator = Natural("0")

    def is_zero(self):
        return self._numerator.is_zero()

    @staticmethod
    def isRational(s):
        k = s.find("/")
        if k == -1:
            return Integer.isInteger(s)
        else:
            integerPart, naturalPart = s[:k], s[k + 1:]
            integer, natural = Integer(integerPart), Natural(naturalPart)
            if natural.is_zero() and not integer._number.is_zero():
                return False
            return Integer.isInteger(integerPart) and Natural.isNatural(naturalPart)

    def __str__(self):
        return str(self._numerator) + "/" + str(self._denumerator)

    @staticmethod
    def integer_to_rational(integer):
        '''Модуль TRANS_Z_Q, оформил Трибунский Алексей'''
        # Числитель равен введенному числу, знаменатель равен единице
        res = Rational()
        res._numerator = Integer(str(integer))
        res._denumerator = Natural("1")
        return res

    @staticmethod
    def to_integer(rational):
        ''' Функция преобразования дробного числа в целое '''
        # Показацкая Арина
        # Если знаменатель равен "1", число преобразуется в целое
        if rational._denumerator == Natural("1"):
            return Integer(str(rational._numerator))
        else:
            raise Exception("unable to convert rational number into integer (denumerator is not equal to 1)")

    def __mul__(self, num):
        # Жексенгалиев
        # Провекра на ноль
        if self.is_zero() or num.is_zero():
            return Rational("0")

        res = Rational()
        res._numerator = self._numerator * num._numerator
        res._denumerator = self._denumerator * num._denumerator

        return res

    def __sub__(self, num):
        '''
        Алгоритм вычитание дробей
        Q-6.SUB_QQ_Q-__sub__
        Выполнил Цыганков Дмитрий
        Необходимые модули:
            - Z-7 Вычитание целых чисел __sub__
            - Z-8 Умножение целых чисел __mul__
            - N-14 НОК натуральных чисел lcm
        '''
        # Проверка на ноль
        if self.is_zero():
            res = Rational(str(num))
            res._numerator.change_sign()
            return res
        elif num.is_zero():
            return Rational(str(self))

        res = Rational()
        # Общий знаминатель
        denum = self._denumerator.lcm(num._denumerator)
        res._denumerator = denum
        # Вычесление числителя
        res._numerator = self._numerator * Integer(str(denum / self._denumerator)) - num._numerator * Integer(str(denum / num._denumerator))
        return res

    def __truediv__(self, num):
        '''Модуль DIV_QQ_Q, оформила Реброва Юлия.'''
        # Проверка на ноль
        if num.is_zero():
            raise Exception("unable to divide by zero")
        elif self.is_zero():
            return Rational("0/0")

        res = Rational()
        # "Переворачиваем" дробь
        n = Integer.natural_to_integer(num._denumerator)
        m = abs(num._numerator)
        res._numerator = self._numerator * n
        res._denumerator = self._denumerator * m

        return res

    def reduce(self):
        #Модуль Q-1 RED_Q_Q оформил Шабров Иван
        if self.is_zero():
            return Rational("0/0")

        r = Rational()
        # Вычисляем НОД числителя и знаменателя
        gcf = abs(self._numerator).gcf(self._denumerator)
        # Переводим k из Natural в Integer
        gcf_int = Integer.natural_to_integer(gcf)

        r._denumerator = self._denumerator / gcf
        r._numerator = self._numerator / gcf_int

        return r


    def is_int(self):
        # Щусь
        num = self.reduce()
        return num._denumerator == Natural("1") or num.is_zero()

    def __add__(self, num):
        '''Модуль ADD_QQ_Q, оформил Проскуряк Влад.'''
        if self.is_zero():
            return Rational(str(num))
        elif num.is_zero():
            return Rational(str(self))

        res = Rational(str(self))
        lcm = self._denumerator.lcm(num._denumerator) # Получаем НОК

        common_div1 = Integer(str(lcm / res._denumerator))
        num1 = res._numerator * common_div1 # Получаем числитель первой дроби

        common_div2 = Integer(str(lcm / num._denumerator))
        num2 = num._numerator * common_div2 # Получаем числитель второй дроби

        res._numerator = num1 + num2 # Вычисляем общий числитель
        res._denumerator = lcm # Приравниваем знаменатель к НОК

        return res