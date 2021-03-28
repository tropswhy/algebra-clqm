
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
            i = 0
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
            
    def mul_d(self,digit):
        if self._dig_n != 0 and digit._dig_n != 0:
            if self._number == [0] or digit._number[0] == 0:
                return 0
            else:
                temp = 0
                for j in range(self._dig_n):
                    if temp != 0:
                        if self._number[j]*digit._number[0]+temp >= 10:
                            temp_n = self._number[j]
                            self._number[j] = (self._number[j]*digit._number[0]+temp)%10
                            temp = (temp_n*digit._number[0]+temp)//10
                        else:
                            self._number[j] = self._number[j]*digit._number[0]+temp
                            temp = 0
                    elif self._number[j]*digit._number[0] >= 10:
                        temp_n = self._number[j]
                        self._number[j] = (self._number[j]*digit._number[0])%10
                        temp = (temp_n*digit._number[0])//10
                    else:
                        self._number[j] = self._number[j]*digit._number[0]
                        temp = 0
                if temp != 0:
                    self._number.insert(self._dig_n,temp)
                return self._number
        else:
            return -1
            