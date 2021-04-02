
from .Integer import *
from .Natural import *

__all__ = ["Rational"]

class Rational():

    def __init__(self, n: str = None):
        if n is None:
            self._numerator = Integer()
            self._denumerator = Natural()
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
                if self._numerator == Integer("0") or self._denumerator == Natural("0"):
                    self._numerator = Integer()
                    self._denumerator = Natural()


    def __str__(self):
        return str(self._numerator) + "/" + str(self._denumerator)

    def integer_to_rational(self, n: Integer):
        # Преобразование целого числа в дробное
        # Трибунский Алексей
        self._numerator = n
        self._denumerator = Natural("1")
        return self

    def to_integer(self):
        ''' Функция преобразования дробного числа в целое '''
        # Показацкая Арина
        if self._denumerator == Natural("1"):
            return self._numerator
        else:
            return Integer()

    def reduce(self):
        ''' Модуль Q-1 RED_Q_Q оформил Шабров Иван '''
        r = Rational(str(self))
        k = abs(r._numerator).gcf(r._denumerator)
        # Переводим k из Natural в Integer
        k_int = Integer()
        k_int = k_int.natural_to_integer(k)
        # ---------------------------------
        r._denumerator = r._denumerator / k
        r._numerator = r._numerator / k_int
        return r
