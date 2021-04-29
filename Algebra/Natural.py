__all__ = ["Natural"]

def remove_zeros(s):
    while s[0] == '0':
        s.pop(0)
    return s

class Natural():

    # _dig_n - количество разрядов в числе
    # _number - натуральное число, представленое в виде перевёрнутого массива цифр (начиная с младших разрядов)
    def __init__(self, n: str = None):
        if not n:
            self._number = [0]
            self._dig_n = 1
        elif not Natural.isNatural(n):
            raise Exception("number passed to \"Natural\" class constructor is invalid")
        # Число состоит из нулей
        elif n == "0" * len(n):
            self._number = [0]
            self._dig_n = 1
        else:
            # Убираем все нули
            n = remove_zeros(n)
            self._number = [int(i) for i in n[::-1]]
            self._dig_n = len(self._number)

    def __str__(self):
        if self._dig_n != 0:
            # Перевод списка в строку
            return ''.join([str(i) for i in reversed(self._number)])
        else:
            return "0"

    @staticmethod
    def isNatural(s):
        for i in s:
            if not ('0' <= i and i <= '9'):
                return False
        return True

    def __gt__(self, num):
        '''Перегрузка оператора ">". Выполнил и оформил Шабров Иван'''

        # Если количетсво разрядов self больше num
        if self._dig_n > num._dig_n:
            return True
        # Если количество разрядов self меньше num
        elif self._dig_n < num._dig_n:
            return False
        # Если количество разрядов одинаковое
        else:
            # Поочередно сравниваем разряды каждого числа
            for i in range(-1, -(self._dig_n + 1), -1):
                if self._number[i] > num._number[i]:
                    return True
                elif self._number[i] < num._number[i]:
                    return False
        return False

    def __eq__(self, num):
        '''Перегрузка оператора "==". Выполнила и оформила Реброва Юлия'''

        # Если количество разрядов не совпадает
        if self._dig_n != num._dig_n:
            return False
        # Последовательно проверяем каждый разряд
        for i in range(num._dig_n):
            if self._number[i] != num._number[i]:
                return False
        return True

    def __lt__(self, num):
        '''Перегрузка оператора "<". Оформил Шабров Иван'''

        # Если количетсво разрядов self меньше num
        if self._dig_n < num._dig_n:
            return True
        # Если количетсво разрядов self больше num
        elif self._dig_n > num._dig_n:
            return False
        else:
            # Поочередно сравниваем разряды каждого числа
            for i in range(-1, -(self._dig_n + 1), -1):
                if self._number[i] < num._number[i]:
                    return True
                elif self._number[i] > num._number[i]:
                    return False
        return False

    '''МОДУЛИ NATURAL'''

    def compare(self, num):
        '''Модуль N-1 COM_NN_D. Выполнил и оформил Шабров Иван'''

        if self > num:
            return 2
        elif self < num:
            return 1
        else:
            return 0

    def is_zero(self):
        '''Модуль N-2 NZER_N_B. Выполнила и оформила Реброва Юлия'''

        if self == Natural("0"):
            return True
        else:
            return False

    def increment(self):
        '''Модуль N-3 ADD_1N_N. Выполнил и оформил Проскуряк Влад'''

        res = Natural(str(self))
        # Если число единиц не превысит 9, то прибавление 1 и окончание модуля
        if (res._number[0] + 1) < 10:
            res._number[0] = res._number[0] + 1
        else:
            i = 0
            # Прибавление 1 и в случае необходимости поднятие по разрядам
            while (i < res._dig_n) and ((res._number[i] + 1) == 10):
                res._number[i] = 0
                i = i + 1
            # Прибавление к высшему разряду единицу или добавление нового разряда
            if (i < res._dig_n):
                res._number[i] = res._number[i] + 1
            else:
                res._dig_n = res._dig_n + 1
                res._number.append(1)
        return res

    def __add__(self, num):
        '''Модуль ADD_NN_N. Выполнил и оформил Жексенгалиев Адиль'''

        res = Natural()
        # Находим наименьшее количество разрядов среди self и num
        if self.compare(num) == 1:
            res._dig_n = num._dig_n
            n = self._dig_n
        else:
            res._dig_n = self._dig_n
            n = num._dig_n
        # Добавляем нули в искомое число
        res._number = [0 for i in range(res._dig_n)]

        # Складываем числа до n - наименьшего количества разрядов
        i = 0
        while i < n:
            # Получаем цифру i-того разряда
            x = res._number[i] + self._number[i] + num._number[i]
            # Если после сложения получилось число, а не цифра
            if x >= 10:
                res._number[i] = x - 10
                # Если x - последний разряд, то расширяем массив чисел
                if (i == res._dig_n - 1):
                    res._number.append(0)
                    res._dig_n += 1
                # Прибавляем единицу к следующему разряду
                res._number[i + 1] += 1
            # Если х - цифра
            else:
                res._number[i] += self._number[i] + num._number[i]
            i += 1
        # Для случая когда числа имеют разные разряды
        j = 0
        # m - количество разрядов, не добавленных в искомое число
        m = abs(self._dig_n - num._dig_n)
        compare = self.compare(num)
        while j < m:
            # Если self больше num
            if compare == 2:
                res._number[j + i] += self._number[j + i]
            # Если num больше self
            else:
                res._number[j + i] += num._number[j + i]
            # Если цифра равна 10, то приравниваем её к нулю
            if res._number[j + i] == 10:
                res._number[j + i] = 0
                # Если складывается последний разряд
                if (j + i == res._dig_n - 1):
                    res._dig_n += 1
                    res._number.append(0)
                # Следующая цифра увелчиивается на 1
                res._number[j + i + 1] += 1
            j = j + 1

        return res

    def __sub__(self, num):
        '''Модуль N-5 SUB_NN_N. Выполнил и оформил Солодков Никита'''
        t = self.compare(num)
        # Если self больше num
        if t == 2:
            big = self
            less = num
            n = num._dig_n
            m = self._dig_n
        # Если self меньше num, то вычитание нельзя произвести
        elif t == 1:
            raise Exception("unable to substitute greater natural number from less natural number")
        # Если числа равны
        else:
            return Natural("0")

        res = Natural()
        res._dig_n = big._dig_n
        res._number = [0 for i in range(big._dig_n)]

        # Вычитаем, начиная со старшего разряда
        i = m - 1
        while i > n - 1:
            res._number[i] = big._number[i]
            i -= 1
        # Вычитаем ненулевые разряды
        while i >= 0:
            x = big._number[i] - less._number[i]
            # Если цифра меньше 0
            if x < 0:
                # Поиск разряда у которого можно "занять" единицу
                j = i + 1
                while res._number[j] == 0:
                    j += 1
                # "Занимаем" единицу
                res._number[j] -= 1
                n = i
                # Вычитаем единицу из нулевых разрядов
                z = j - 1
                while z > n - 1:
                    if res._number[z] == 0:
                        res._number[z] = 9
                    z -= 1
                res._number[i] = x + 10
            else:
                res._number[i] = x
            i -= 1

        # Удаляем незначащие нули
        i = m - 1
        while res._number[i] == 0:
            res._dig_n -= 1
            del res._number[i]
            i -= 1

        return res

    def mul_d(self, digit: int):
        '''Модуль N-6 MUL_ND_N. Выполнил и оформил Цыганков Дмитрий'''
        # Проверка цифры
        if digit < 0:
            raise Exception("unable to multiple a natural number by a negative digit")
        elif digit > 9:
            raise Exception("digit cannot be greater than 9")
        # Проверка на ноль
        if self.is_zero() or digit == 0:
            return Natural("0")

        # self_c - искомое число
        # temp - остаток после умножения разряда на число.
        self_c = Natural(str(self))
        temp = 0

        for j in range(self_c._dig_n):
            # Если после предыдущего шага есть остаток
            if temp != 0:
                # Если умножение очередной цифры числа оказалось больше 10
                if self_c._number[j] * digit + temp >= 10:
                    temp_n = self_c._number[j]
                    self_c._number[j] = (self_c._number[j] * digit + temp) % 10
                    temp = (temp_n * digit + temp) // 10
                else:
                    self_c._number[j] = self_c._number[j] * digit + temp
                    temp = 0
            # Если умножение очередной цифры числа оказалось больше 10
            elif self_c._number[j] * digit >= 10:
                temp_n = self_c._number[j]
                self_c._number[j] = (self_c._number[j] * digit) % 10
                temp = (temp_n * digit) // 10
            else:
                self_c._number[j] = self_c._number[j] * digit
                temp = 0

        # Если на последнем шаге остался остаток, то записываем его в 1 позицию
        if temp != 0:
            self_c._number.insert(self_c._dig_n, temp)
            self_c._dig_n += 1

        return self_c

    def mul_k(self, tenpow: int):
        '''Модуль N-7 MUL_Nk_N. Выполнил и оформил Цыганков Дмитрий'''
        # Проверка на неотрицательность
        if tenpow < 0:
            raise Exception("unable to raise a natural number to a negative power")
        # Проверка на ноль
        if self.is_zero():
            return Natural("0")

        self_c = Natural(str(self))
        # Добавляем ноль tenpow раз
        for i in range(tenpow):
            self_c._number.insert(i, 0)
            self_c._dig_n += 1

        return self_c

    def __mul__(self, x):
        '''Модуль N-8 MUL_NN_N. Выполнил и оформил Трибунский Алексей'''
        res = Natural("0")
        # Проходим по всем цифрам второго множителя
        for i in range(x._dig_n):
            # К res прибавляем первый множитель, умноженный на цифру второго множителя и на 10^i
            res += self.mul_d(x._number[i]).mul_k(i)
        return res

    def sub_dn(self, dig, num):
        '''Модуль N-9 SUB_NDN_N. Выполнила и оформила Реброва Юлия'''
        # Проверка цифры
        if dig < 0:
            raise Exception("unable to multiple a natural number by a negative digit")
        elif dig > 9:
            raise Exception("digit cannot be greater than 9")

        c = num.mul_d(dig)
        if self.compare(c) != 1:
            return self - c
        else:
            raise Exception("unable to substitute greater natural number from less natural number")

    def div_dk(self, num):
        '''Модуль N-10 DIV_NN_Dk. Выполнил и оформил Щусь Максим'''
        # Проверка на ноль
        if self.is_zero():
            return 0, 0
        elif num.is_zero():
            raise Exception("unable to divide natural number by zero")
        if self.compare(num) == 0:
            return 1, 0

        n1 = Natural(str(self))
        n2 = Natural(str(num))
        # k - первая цифра деления
        k = 0

        if n1.compare(n2) == 1:
            less = n1
            greater = n2
        else:
            less = n2
            greater = n1

        # Номер позиции первой цифры от деления greater на less
        n3 = less
        while greater.compare(n3) == 2:
            k += 1
            n3 = less.mul_k(k)
        k -= 1

        n3 = less.mul_k(k)
        less = n3

        # Находим цифру деления greater на less
        dig = 1
        while greater.compare(n3) == 2:
            dig += 1
            n3 = less.mul_d(dig)

        # Если n3 стало больше greater, то уменьшаем цифру деления на 1
        if greater.compare(n3) != 0:
            dig -= 1
        # Если оказалось, что цифра равна 10
        if dig == 10:
            # Увеличиваем номер позиции цифра на 1, dig присваиваем 1
            dig = 1
            k += 1

        return dig, k

    def __truediv__(self, num):
        '''Модуль N-11 DIV_NN_N. Выполнила и оформила Показацкая Арина'''
        # Проверка на ноль
        if self.is_zero():
            return Natural("0")
        elif num.is_zero():
            raise Exception("unable to divide natural number by zero")

        n1 = Natural(str(self))
        n2 = Natural(str(num))
        res = Natural()

        res._number = [0 for i in range(res._dig_n)]
        # Количество разрядов в результирующем числе
        res._dig_n = n1.div_dk(n2)[1] + 1

        while n1.compare(n2) != 1:
            # Очередная цифра результата и номер позиции этой цифры
            a, b = n1.div_dk(n2)
            res._number[b] = a
            # Делитель, умноженный на 10 в степени b
            c = n2.mul_k(b)
            n1 = n1.sub_dn(a, c)

        return res

    def __mod__(self, num):
        '''Модуль N-12 MOD_NN_N. Выполнил и оформил Проскуряк Влад'''
        # Проверка на ноль
        if num.is_zero():
            raise Exception("unable to find modulo by zero")

        res = Natural(str(self))
        if self.compare(num) != 1:
            i = res / num # Частное от деления
            res = res - i * num # Вычитаем из делимого произведение частного на делитель и получаем остаток
        return res

    def gcf(self, num):
        '''Модуль N-13 GCF_NN_N. Выполнил и оформил Шабров Иван'''
        # Проверка на ноль
        if self.is_zero() and num.is_zero():
            raise Exception("gcf of both zeros is undefined")

        n1 = Natural(str(self))
        n2 = Natural(str(num))

        # Алгоритм Евклида
        while (not n1.is_zero()) and (not n2.is_zero()):
            if n1.compare(n2) == 2:
                n1 = n1 % n2
            else:
                n2 = n2 % n1

        return n1 + n2

    def lcm(self, num):
        '''Модуль N-14 LCM_NN_N. Выполнил и оформил Жексенгалиев Адиль'''
        # Проверка на ноль
        if self.is_zero():
            if num.is_zero():
                raise Exception("lcm of both zeros is undefined")
            else:
                raise Exception("lcm of a zero and a number is undefined")

        gcf = self.gcf(num)
        return (self * num) / gcf