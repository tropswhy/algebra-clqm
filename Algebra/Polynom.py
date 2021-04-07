
from .Natural import *
from .Integer import *
from .Rational import *

__all__ = ["Polynom"]

class Polynom():

    # _coef - массив коэффициентов начиная с большего и заканчивая меньшим
    # _coef_n - количество коэффициентов
    def __init__(self, l: list = None):
        if l is None:
            self._coef = []
            self._coef_n = 0
        else:
            self._coef = [Rational(str(i)) for i in l[::-1]]
            self._coef_n = len(l)

    # TO DO:
    # Пофиксить вывод отрицательных коэффициентов
    def __str__(self):
        s = ""
        for i in range(self._coef_n - 1, -1, -1):
            if i != 0:
                s += str(self._coef[i]) + f"x^{i} + "
            else:
                s += str(self._coef[i])
        return s

    def power(self):
        '''Модуль DEG_P_N выполнил и оформил Солодков Никита'''
        return self._coef_n - 1

    def higher_coef(self):
        '''Модуль LED_P_Q выполнил и оформил Шабров Иван'''
        return self._coef[-1]

    # КОД НЕ РАБОТАЕТ
    '''
    def mul_xk(self, k: int):
        #Модуль MUL_Pxk_P выполнила и оформила Реброва Юлия
        b = Polynom(self._coef_n + k)
        b._coef = [0 * (self._coef_n + k)]
        for i in range(self._coef_n):
            b._coef[i] = self._coef[i]
        return b
    '''

    def mul_q(self, num):
        ''' Выполнил Адиль Жексенгалиев'''
        # Модуль P-3
        res = Polynom()
        res._coef_n = self._coef_n
        res._coef = [Rational("1") for i in range(res._coef_n)]
        for i in range(self._coef_n):
            res._coef[i]._numerator = self._coef[i]._numerator * num._numerator
            res._coef[i]._denumerator = self._coef[i]._denumerator * num._denumerator
        return res


    def derivate(self):
        res = Polynom(self._coef[::-1])
        for i in range(len(self._coef)-1):
            res._coef[i] = self._coef[i+1] * Rational(str(i+1))
        res._coef = res._coef[:len(self._coef)-1]
        self._coef_n -= 1
        res = Polynom(res._coef[::-1])
        return res

#Модуль не работает без ADD_QQ_Q
    #
    # def __add__(self, num):
    #     # Модуль ADD_PP_P выполнил и оформил Щусь Максим
    #     p1 = Polynom(self._coef)
    #     p2 = Polynom(num._coef)
    #     if p2._coef_n > p1._coef_n:
    #         res = Polynom(num._coef)
    #         for i in range(p1._coef_n):
    #             res._coef[i] = res._coef[i] + p1._coef[i]
    #     else:
    #         res = Polynom(self._coef)
    #         for i in range(p2._coef_n):
    #             res._coef[i] = res._coef[i] + p2._coef[i]
    #     return res


    def fac(self):
        # Модуль FAC_P_Q выполнил и оформил Солодков Никита'''
        res = Rational()
        # Присваиваем НОД и НОК значение числителя и знаменателя первых элементов соответственно
        num_gcd = abs(self._coef[0]._numerator)
        num_lcm = self._coef[0]._denumerator
        for i in range (self._coef_n):
            num_gcd = num_gcd.gcd(abs(self._coef[i]._numerator))
            num_lcm = num_lcm.lcm(self._coef[i]._denumerator)
        num_gcd = Integer(str(num_gcd))
        res.numerator = num_gcd
        res.denumerator = num_lcm
        return res

    def __sub__(self, num):
        # Вычитание многочленов
        # Показацкая Арина
        k = max(self.power(), num.power())
        c = min(self.power(), num.power())
        res = Polynom([Rational("0") for i in range(k + 1)])
        if (self._coef_n >= num._coef_n):
            for i in range(k + 1):
                res._coef[i] = Rational(str(self._coef[i]))
            for i in range(c + 1):
                print(res._coef[i] - num._coef[i])
                res._coef[i] = res._coef[i] - num._coef[i]
        else:
            for i in range(k + 1):
                res._coef[i] = Rational(str(num._coef[i]))
            for i in range(c + 1):
                res._coef[i] = self._coef[i] - res._coef[i]
        while (res._coef[res._coef_n - 1] == 0):
            res._coef.pop()
            res._coef_n -= 1
        return res

    def __truediv__(self,pol):
        '''
        Частное от деления многочлена на многочлен при делении с остатком
        P-9.DIV_PP_P-__truediv__
        Выполнил Цыганков Дмитрий
        '''
        divisbl = Polynom(self._coef)
        pol_ = Polynom(pol._coef)
        # степнь искомого полинома
        deg = divisbl.power() - pol_.power()
        result = Polynom([0] * deg)
        i = 0
        while (divisbl.power() >= pol_.power()):
            result._coef[deg-i] = divisbl._coef[-1] / pol_._coef[-1]
            # умножаем делитель на полученный член полинома 
            if not (divisbl._coef[-1]._numerator == Integer("0")):
                temp_mon = Polynom([0] * (deg - i))
                temp_mon._coef[deg-i] = result._coef[deg-i]
                # отнимаем полученный полином от делимого
                divisbl -= pol_ * temp_mon
            i += 1
            # удаление первого коэффициента
            divisbl._coef.pop()
        return result # возврат частного


    '''
    # не пашет без ADD_PP_P и MUL_Pxk_P
    # модуль MUL_PP_P, оформил Трибунский Алексей
    def __mul__(self, p):
        res = Polynom(self._coef[::-1])
        for i in range(p._coef_n):
            res += res.mul_q(p._coef[i]).mul_xk(i)
        return res
    '''

    def gcf(self, num):
        '''Модуль P-11 GCF_PP_P выполнил и оформил Шабров Иван'''
        a = Polynom(self._coef)
        b = Polynom(num._coef)
        while a > 0 and b > 0:
            if a.power() > b.power():
                a = a.__mod__(b)
            else:
                b = b.__mod__(a)
        return a + b

    def nmr(self):
        '''
        Преобразование многочлена — кратные корни в простые
        P-13.NMR_P_P-nmr
        Выполнил Цыганков Дмитрий
        '''
        pol_ = Polynom(self._coef)
        pol_ /= pol_.gcf(pol_.derivate()) # делим полином на НОД от него и его производной
        return pol_ 