__all__ = ["Natural"]

# TO DO:
# Создать отдельный файл для подобных функций?

def remove_zeros(s):
    i = 0
    while s[i] == '0':
        i += 1
    return s[i:]

class Natural():

    # _dig_n - количество разрядов в числе
    # _number - натуральное число, представленое в виде перевёрнутого массива цифр
    def __init__(self, n: str = None):
        self._number = []
        if not n:
            self._number = [0]
            self._dig_n = 1
        elif not Natural.isNatural(n):
            raise Exception("Number passed to \"Natural\" class constructor is invailid. "
                            "You must enter only digits from 0 to 9 and no other symbols.")
        # Число состоит из нулей
        elif n == "0" * len(n):
            self._number = [0]
            self._dig_n = 1
        else:
            # Убираем все нули
            n = remove_zeros(n)
            self._number = [int(i) for i in n[::-1]]
            self._dig_n = len(self._number)

    @staticmethod
    def isNatural(s):
        for i in s:
            if not ('0' <= i and i <= '9'):
                return False
        return True

    def __reversed__(self):
        return reversed(self._number)

    def __str__(self):
        if self._dig_n != 0:
            # Перевод списка в строку
            return ''.join([str(i) for i in reversed(self._number)])
        else:
            return "0"

    '''Модуль N-6.MUL_ND_N-mul_d #6 выполнил и оформил Цыганков Дмитрий'''

    def mul_d(self, digit: int):
        # Проверка на цифру
        if digit < 0:
            raise Exception("You must not multiple a natural number by negative number")
        elif digit > 9:
            raise Exception("Entered digit must not be greater than 9.")
        # self_c - результат
        self_c = Natural(str(self))
        if self_c._dig_n != 0:  # если числа не пустые
            if self_c._number == [0] or digit == 0:  # если одно из чисел нулевое
                return Natural("0")
            else:
                temp = 0  # остаток после умножения разряда на число.
                for j in range(self_c._dig_n):
                    if temp != 0:  # если после предыдущего шага есть остаток
                        if self_c._number[j] * digit + temp >= 10:  # если умножение очередной цифры числа оказалось больше 10
                            temp_n = self_c._number[j]
                            self_c._number[j] = (self_c._number[j] * digit + temp) % 10
                            temp = (temp_n * digit + temp) // 10
                        else:
                            self_c._number[j] = self_c._number[j] * digit + temp
                            temp = 0
                    elif self_c._number[j] * digit >= 10:  # если умножение очередной цифры числа оказалось больше 10
                        temp_n = self_c._number[j]
                        self_c._number[j] = (self_c._number[j] * digit) % 10
                        temp = (temp_n * digit) // 10
                    else:
                        self_c._number[j] = self_c._number[j] * digit
                        temp = 0
                if temp != 0:  # если на последнем шаге остался остаток, то записываем его в 1 позицию
                    self_c._number.insert(self_c._dig_n, temp)
                    self_c._dig_n += 1
                return self_c
        else:
            return Natural()

    '''Модуль N-7.MUL_Nk_N-mul_k #11 выполнил и оформил Цыганков Дмитрий'''

    def mul_k(self, tenpow: int):
        # Проверка на неотрицательность
        if tenpow < 0:
            raise Exception("You must not raise a natural number to a negative power.")
        self_c = Natural(str(self))
        # Добавляем 0 tenpow раз
        for i in range(tenpow):
            self_c._number.insert(i, 0)
            self_c._dig_n += 1
        return self_c

    def __gt__(self, num):
        '''Модуль переполнения ">". Оформил Шабров Иван'''
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
        '''Перегрузка оператора "==". Оформила Реброва Юлия'''
        # Если количество разрядов не совпадает
        if self._dig_n != num._dig_n:
            return False
        # Последовательно проверяем каждый разряд
        for i in range(num._dig_n):
            if self._number[i] != num._number[i]:
                return False
        return True

    def __lt__(self, num):
        '''Модуль переполнения "<". Оформил Шабров Иван'''
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

    def compare(self, num):
        '''Модуль COM_NN_D. Оформил Шабров Иван'''
        if self > num:
            return 2
        elif self < num:
            return 1
        else:
            return 0

    def is_zero(self):
        '''Модуль NZER_N_B. Оформила Реброва Юлия'''
        if self == Natural("0"):
            return True
        else:
            return False

    def __add__(self, num):
        '''Модуль ADD_NN_N. Оформил Адиль Жексенгалиев'''
        # Сложение натуральных чисел
        res = Natural()
        if self.compare(num) == 1:
            res._dig_n = num._dig_n
            n = self._dig_n
        else:
            res._dig_n = self._dig_n
            n = num._dig_n
        res._number = [0 for i in range(res._dig_n)]
        i = 0
        while i < n:
            x = res._number[i] + self._number[i] + num._number[i]
            if x == 10:
                res._number[i] = 0
                #  расширение массива чисел
                if (i == res._dig_n - 1):
                    res._number.append(0)
                    res._dig_n += 1
                res._number[i + 1] += 1
                if res._number[i + 1] == 10:
                    res._number[i + 1] = 0
                    res._number[i + 2] += 1

            elif x > 10:
                res._number[i] = x - 10
                if (i == res._dig_n - 1):
                    res._number.append(0)
                    res._dig_n += 1
                res._number[i + 1] += 1
            else:
                res._number[i] += self._number[i] + num._number[i]

            i = i + 1
        # Для случая когда числа имеют разные разряды
        j = 0
        while j < abs(self._dig_n - num._dig_n):
            # cтоит ли заменить метод  на переменную или оставить так для читаемости кода?
            if self.compare(num) == 2:
                res._number[j + i] += self._number[j + i]
            else:
                res._number[j + i] += num._number[j + i]
            if res._number[j + i] == 10:
                res._number[j + i] = 0
                if (j + i == res._dig_n - 1):
                    res._dig_n += 1
                    res._number.append(0)

                res._number[j + i + 1] += 1

            j = j + 1
        return res

    def __mul__(self, x):
        '''Модуль MUL_NN_N. Оформил Трибунский Алексей'''
        res = Natural("0")
        # Проходим по всем цифрам второго множителя
        for i in range(x._dig_n):
            # К res прибавляем первый множитель, умноженный на цифру второго множителя и на 10^i
            res += self.mul_d(x._number[i]).mul_k(i)
        return res

    def __sub__(self, num):
        '''Модуль LCM_NN_N. Оформил Жексенгалиев Адиль'''
        ''' SUB_NN_N'''
        t = self.compare(num)
        if t == 2:
            big = self
            less = num
            n = num._dig_n
            m = self._dig_n
        elif t == 1:
            raise Exception("You must not substitute greater number from less number.")
        else:
            return Natural("0")
        # создание результирующего натур  числа
        res = Natural()
        res._dig_n = big._dig_n
        res._number = [0 for i in range(big._dig_n)]
        # print(res._number)
        i = m - 1
        while i > n - 1:
            res._number[i] = big._number[i]
            i -= 1
        # i  по сути будет равно n
        while i >= 0:
            x = big._number[i] - less._number[i]
            if x < 0:
                # Поиск разряда у которого можно занять
                j = i + 1
                while res._number[j] == 0:
                    j += 1
                res._number[j] -= 1
                n = i
                z = j - 1
                while z > n - 1:
                    if res._number[z] == 0:
                        res._number[z] = 9
                    z -= 1
                res._number[i] = x + 10
            elif x > 0:
                res._number[i] = x
            else:
                res._number[i] = 0
            i -= 1
        # Удаление нулей
        i = m - 1
        while res._number[i] == 0:
            res._dig_n -= 1
            del res._number[i]
            i -= 1
        return res

    def gcf(self, num):
        # Модуль GCF_NN_N. Оформил Шабров Иван
        # Проверка на ноль
        if self.is_zero() and num.is_zero():
            raise Exception("GCF of both zeros is undefined.")

        n1 = Natural(str(self))
        n2 = Natural(str(num))

        # Алгоритм Евклида
        while (not n1.is_zero()) and (not n2.is_zero()):
            if n1.compare(n2) == 2:
                n1 = n1 % n2
            else:
                n2 = n2 % n1

        return n1 + n2

    def increment(self):
        '''Модуль ADD_1N_N, оформил Проскуряк Влад.'''
        res = Natural(str(self))
        if (res._number[0] + 1) < 10:
            res._number[0] = res._number[0] + 1 # Если число единиц не превысит 9 то прибавление 1 и окончание модуля
        else:
            i = 0
            while (i < res._dig_n) and ((res._number[i] + 1) == 10): # Прибавление 1 и в случае необходимости поднятие по разрядам
                res._number[i] = 0
                i = i + 1
            if (i < res._dig_n): # Прибавление к высшему разряду единицу или добавление нового разряда
                res._number[i] = res._number[i] + 1
            else:
                res._dig_n = res._dig_n + 1
                res._number.append(1)
        return res

    def __truediv__(self, num):
        '''Функция нахождения частого'''
        # Показацкая Арина
        # Проверка на ноль
        if self.is_zero():
            return Natural("0")
        elif num.is_zero():
            raise Exception("You must not divide natural number by zero.")

        n1 = Natural(str(self))
        n2 = Natural(str(num))
        res = Natural()

        # Количество разрядов в результирующем числе
        res._dig_n = n1.div_dk(n2)[1] + 1
        res._number = [0 for i in range(res._dig_n)]

        while n1.compare(n2) != 1:
            # Очередная цифра результата и номер позиции этой цифры
            a, b = n1.div_dk(n2)
            res._number[b] = a
            # Делитель, умноженный на 10 в степени b
            c = n2.mul_k(b)
            # Разность делимого и делителя, умноженного на первую цифру
            n1 = n1.sub_dn(a, c)

        return res

    def lcm(self, num):
        # Модуль LCM_NN_N. Оформил Жексенгалиев Адиль
        if self.is_zero():
            if num.is_zero():
                raise Exception("LCM of both zeros is undefined")
            else:
                raise Exception("LCM of a zero and a number is undefined")
        gcf = self.gcf(num)
        return (self * num) / gcf

    def div_dk(self, num):
        '''Модуль DIV_NN_Dk, оформил Щусь Максим.'''
        if self.is_zero():
            return 0, 0
        elif num.is_zero():
            raise Exception("You must not divide natural number by zero.")
        n1 = Natural(str(self))
        n2 = Natural(str(num))
        k = 0
        if n1.compare(n2) == 1:
            n3 = n1
            while n2.compare(n3) == 2:
                k += 1
                n3 = n1.mul_k(k)
            k -= 1
            n3 = n1.mul_k(k)
            n1 = n3
            dig = 1
            while n2.compare(n3) == 2:
                dig += 1
                n3 = n1.mul_d(dig)
            if n2.compare(n3) != 0:
                dig -= 1
            if dig == 10:
                dig = 1
                k += 1
        elif n1.compare(n2) == 2:
            n3 = n2
            while n1.compare(n3) == 2:
                k += 1
                n3 = n2.mul_k(k)
            k -= 1
            n3 = n2.mul_k(k)
            n2 = n3
            dig = 1
            while n1.compare(n3) == 2:
                dig += 1
                n3 = n2.mul_d(dig)
            if n1.compare(n3) != 0:
                dig -= 1
            if dig == 10:
                dig = 1
                k += 1
        else:
            return 1, 0
        return dig, k

    def sub_dn(self, dig, num):
        # Модуль SUB_NDN_N. Оформила Реброва Юлия
        # Проверка на цифру
        if dig < 0:
            raise Exception("You must not multiple a number by a negative digit.")
        elif dig > 9:
            raise Exception("Entered digit must not be greater than 9.")
        # Умножаем число
        c = num.mul_d(dig)
        # Если уменьшаемое не меньше вычитаемого
        if self.compare(c) != 1:
            return self - c
        else:
            raise Exception("You can not substitute bigger number from less number.")

    def __mod__(self, num):
        '''Модуль MOD_NN_N, оформил Проскуряк Влад.'''
        if num.is_zero():
            raise Exception("You must not try to find modulo by zero.")
        res = Natural(str(self))
        if (self.compare(num) != 1):
            i = res / num # Частное от деления 
            res = res - i * num # Вычитаем из делимого произведение частного на делитель и получаем остаток
        return res