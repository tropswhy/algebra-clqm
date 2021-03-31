
__all__ = ["Natural"]

# TO DO:
# Создать отдельный файл для подобных функций?
def remove_char(s, n):
    return s[:n] + s[n + 1:]

class Natural():

    # _dig_n - количество разрядов в числе
    # _number - натуральное число, представленое в виде перевёрнутого массива цифр
    def __init__(self, n = None):
        self._number = []
        if n is None:
            self._dig_n = 0
        # Число состоит из нулей
        elif n == "0" * len(n):
            self._number = [0]
            self._dig_n = 1
        else:
            while n.find("0") != -1 and n[0] == "0":
                n = remove_char(n,n.index("0"))
            self._number = [int(i) for i in n[::-1]]
            self._dig_n = len(self._number)

    def __reversed__(self):
        return reversed(self._number)

    def __str__(self):
        if self._dig_n != 0:
            # Перевод списка в строку
            return ''.join([str(i) for i in reversed(self._number)])
        else:
            return "0"

    '''Модуль N-6.MUL_ND_N-mul_d #6 выполнил и оформил Цыганков Дмитрий'''
    def mul_d(self,digit:int):
        self_c = Natural(str(self)) 
        if self_c._dig_n != 0: #если числа не пустые
            if self_c._number == [0] or digit == 0: #если одно из чисел нулевое
                return Natural("0")
            else:
                temp = 0 #остаток после умножения разряда на число.
                for j in range(self_c._dig_n):
                    if temp != 0: #если после предыдущего шага есть остаток
                        if self_c._number[j]*digit + temp >= 10: #если умножение очередной цифры числа оказалось больше 10
                            temp_n = self_c._number[j]
                            self_c._number[j] = (self_c._number[j]*digit + temp)%10
                            temp = (temp_n*digit + temp)//10
                        else:
                            self_c._number[j] = self_c._number[j]*digit + temp
                            temp = 0
                    elif self_c._number[j]*digit >= 10:#если умножение очередной цифры числа оказалось больше 10
                        temp_n = self_c._number[j]
                        self_c._number[j] = (self_c._number[j]*digit)%10
                        temp = (temp_n*digit)//10
                    else:
                        self_c._number[j] = self_c._number[j]*digit
                        temp = 0
                if temp != 0: #если на последнем шаге остался остаток, то записываем его в 1 позицию
                    self_c._number.insert(self_c._dig_n, temp)
                return self_c
        else:
            Natural()

    '''Модуль N-7.MUL_Nk_N-mul_k #11 выполнил и оформил Цыганков Дмитрий'''
    def mul_k(self,tenpow:int):
        self_c = Natural(str(self))
        for i in range(tenpow):
            self_c._number.insert(i,0)
        return self_c
        