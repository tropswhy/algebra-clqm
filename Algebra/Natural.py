
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
            # Убираем все нули
            while n.find("0") != -1:
                n = remove_char(n, n.index("0"))
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


    def __gt__(self, num):
        '''Модуль переполнения ">". Оформил Шабров Иван'''
        # Принимает уже реверсированные массивы!
        if len(self.n) > len(num.n):
            return True
        elif len(self.n) < len(num.n):
            return False
        elif (self[0] != 0) or (num[0] != 0):
            for i in range(len(self.n)):
                if self.n[i] > num.n[i]:
                    return True
                elif self.n[i] < num.n[i]:
                    return False
        else:
            return False


    def __lt__(self, num):
        '''Модуль переполнения "<". Оформил Шабров Иван'''
        # Принимает уже реверсированные массивы!
        if len(self.n) < len(num.n):
            return True
        elif len(self.n) > len(num.n):
            return False
        elif (self[0] != 0) or (num[0] != 0):
            for i in range(len(self.n)):
                if self.n[i] < num.n[i]:
                    return True
                elif self.n[i] > num.n[i]:
                    return False
        else:
            return False


    def compare(self, num):
        '''Модуль COM_NN_D. Оформил Шабров Иван'''
        if self > num:
            return 2
        elif self < num:
            return 1
        else:
            return 0