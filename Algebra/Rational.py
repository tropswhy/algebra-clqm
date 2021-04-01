
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
                self._denumerator = Natural("1")
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

    def to_integer(self):
        ''' Функция преобразования дробного числа в целое '''
        # Показацкая Арина
        if str(self._denumerator) == "1":
            return self._numerator
        else:
            return Integer()