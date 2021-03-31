
from .Integer import *

__all__ = ["Polynom"]

class Polynom():

    # _coef - массив коэффициентов начиная с большего и заканчивая меньшим
    # _coef_n - количество коэффициентов
    def __init__(self, l = None):
        if l is None:
            self._coef = []
            self._coef_n = 0
        else:
            self._coef = [Integer(str(i)) for i in list(l)]
            self._coef_n = len(l)

    # TO DO:
    # Пофиксить вывод отрицательных коэффициентов
    def __str__(self):
        s = ""
        for i in range(self._coef_n - 1, -1, -1):
            if i != 0:
                s += str(self._coef[self._coef_n - i - 1]) + f"x^{i} + "
            else:
                s += str(self._coef[self._coef_n - i - 1])
        return s

    def power(self):
        '''Модуль DEG_P_N выполнил и оформил Солодков Никита'''
        return self._coef_n - 1

    def higher_coef(self):
        '''Модуль LED_P_Q выполнил и оформил Шабров Иван'''
        return self._coef[0]

    def mul_xk(self, k):
        '''Модуль MUL_Pxk_P выполнила и оформила Реброва Юлия'''
        b = Polynom(self._coef_n + k)
        b._coef = [0 * (self._coef_n + k)]
        for i in range(self._coef_n):
            b._coef[i] = self._coef[i]
        return b


