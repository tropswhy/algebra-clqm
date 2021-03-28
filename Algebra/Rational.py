
from .Integer import *
from .Natural import *

__all__ = ["Rational"]

class Rational():

    def __init__(self, n = None, m = None):
        # Если в __init__ не был передан ни один аргумент
        # то создаём "пустое" число
        if n is None and m is None:
            self._numerator = Integer()
            self._denumerator = Natural()
        # Если m не было введено
        # то оно считается равным единице
        else:
            self._numerator = Integer(n)
            self._denumerator = Integer("1" if m is None else m)


    def __str__(self):
        return str(self._numerator) + " / " + str(self._denumerator)

    def integer_to_rational(self, n):
        # Преобразование целого числа в дробное
        # Трибунский Алексей
        self._numerator = n
        self._denumerator = "1"

    def to_integer(self):
        ''' Функция преобразования дробного числа в целое '''
    # Показацкая Арина
        if str(self._denumerator) == "1":
            return self._numerator
        else:
            return Integer()