
from .Natural import *
from .Integer import *
from .Rational import *

__all__ = ["Polynom"]

class Polynom():

    # _coef - массив коэффициентов начиная с меньшего и заканчивая большим
    # _coef_n - количество коэффициентов
    def __init__(self, l: list = None):
        if l is None:
            self._coef = [Rational("0")]
            self._coef_n = 1
        else:
            try:
                self._coef = [Rational(str(i)) for i in l[::-1]]
                self._coef_n = len(l)
            except:
                raise Exception("Error while converting coefficients into rational numbers")

    # TO DO:
    # Пофиксить вывод отрицательных коэффициентов
    def __str__(self):
        i = self._coef_n
        while self._coef[i - 1]._numerator._number.is_zero() and i > 1:
            i -= 1
        return " ".join(map(str, self._coef[i - 1::-1]))

    def power(self):
        '''Модуль DEG_P_N выполнил и оформил Солодков Никита'''
        # self._coef_n - это количество коэффицентов
        # Степень многочлена на единицу меньше количества коэффициентов
        return self._coef_n - 1

    def higher_coef(self):
        '''Модуль LED_P_Q выполнил и оформил Шабров Иван'''
        return self._coef[-1]

    def mul_xk(self, k: int):
        #Модуль MUL_Pxk_P выполнила и оформила Реброва Юлия
        b = Polynom(["0"] * (self._coef_n + k))
        for i in range(self._coef_n):
            b._coef[i + k] = self._coef[i]
        return b

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
    def __add__(self, num):
        # Модуль ADD_PP_P выполнил и оформил Щусь Максим
        p1 = Polynom(self._coef[::-1])
        p2 = Polynom(num._coef[::-1])
        if p2._coef_n > p1._coef_n:
            res = Polynom(num._coef[::-1])
            for i in range(p1._coef_n):
                res._coef[i] = res._coef[i] + p1._coef[i]
        else:
            res = Polynom(self._coef[::-1])
            for i in range(p2._coef_n):
                res._coef[i] = res._coef[i] + p2._coef[i]
        return res


    def fac(self):
        # Модуль FAC_P_Q выполнил и оформил Солодков Никита'''
        res = Rational()
        # Присваиваем НОД и НОК значение числителя и знаменателя первых элементов соответственно
        num_gcf = abs(self._coef[0]._numerator)
        num_lcm = self._coef[0]._denumerator
        # Циклом проходим по всем коэффициентам многочлена
        for i in range (1, self._coef_n):
            if not (self._coef[i].is_zero() and num_gcf.is_zero()):
                num_gcf = num_gcf.gcf(abs(self._coef[i]._numerator))
            if not (self._coef[i].is_zero() or num_lcm.is_zero()):
                num_lcm = num_lcm.lcm(self._coef[i]._denumerator)
            elif num_lcm.is_zero() and not self._coef[i].is_zero():
                num_lcm = self._coef[i]._denumerator
        res._numerator = Integer(str(num_gcf))
        res._denumerator = num_lcm
        return res

    def __sub__(self, num):
        '''Вычитание многочленов'''
        # Показацкая Арина
        k = max(self.power(), num.power()) # степень большего многочлена
        c = min(self.power(), num.power()) # степень меньшего многочлена
        res = Polynom([Rational("0") for i in range(k + 1)]) # результат
        if (self._coef_n >= num._coef_n):
            # если количество коэффициентов первого больше(или равно) второго
            for i in range(k + 1):
                # записываем в результат первый многочлен и вычитаем из него второй
                res._coef[i] = Rational(str(self._coef[i]))
            for i in range(c + 1):
                res._coef[i] = res._coef[i] - num._coef[i]
        else:
            # если количество коэффициентов второго больше первого
            for i in range(k + 1):
                # записываем в результат второй многочлен и вычитаем из него первый
                res._coef[i] = Rational(str(num._coef[i]))
            for i in range(c + 1):
                res._coef[i] = self._coef[i] - res._coef[i]
            zero = Rational("0")
            for i in range(c + 1, k + 1):
                res._coef[i] = zero - res._coef[i]
        while (res._coef[res._coef_n - 1] == 0):
            # удаляем нулевые коэффициенты вначале, если такие есть
            res._coef.pop()
            res._coef_n -= 1
        return res

    def __truediv__(self, pol):
        '''
        Частное от деления многочлена на многочлен при делении с остатком
        P-9.DIV_PP_P-__truediv__
        Выполнил Цыганков Дмитрий
        '''
        divisbl = Polynom(self._coef[::-1])
        pol_ = Polynom(pol._coef[::-1])
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

    # модуль MUL_PP_P, оформил Трибунский Алексей
    def __mul__(self, p):
        res = Polynom(self._coef[::-1])
        for i in range(p._coef_n):
            res += res.mul_q(p._coef[i]).mul_xk(i)
        return res


    def gcf(self, num):
        '''Модуль P-11 GCF_PP_P выполнил и оформил Шабров Иван'''
        a = Polynom(self._coef[::-1])
        b = Polynom(num._coef[::-1])
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
        pol_ = Polynom(self._coef[::-1])
        pol_ /= pol_.gcf(pol_.derivate()) # делим полином на НОД от него и его производной
        return pol_
        
    def __mod__(self, num):
        '''Модуль MOD_PP_P, оформил Проскуряк Влад'''
        res = Polynom(self._coef[::-1])
        resnum = Polynom(num._coef[::-1])
        # Вычитаем из многочлена произведение второго многочлена на частное от деления многочленов и получаем остаток
        res = res - resnum * (res / resnum)
        return res
