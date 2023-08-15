# https://docs.google.com/forms/d/e/1FAIpQLSc8O2WF4M4ziAPnWG6dDPqvZ79e0Z23FrGfTCqwKWbhs5SSBA/viewform?usp=sf_link

'''1) Напишите класс с описанием параллелепипеда
-принимает в себя ширину и длинну основания, а так же высоту
-реализуйте методы для расчета его объема, площади основания и площади боковой стороны
-добавьте статический метод info, который бы выводил перечень методов
'''


class Parallelepiped:
    def __init__(self, w, l, h):
        self.w = int(w)
        self.l = int(l)
        self.h = int(h)

    def volume(self):
        return self.w * self.l * self.h

    def s_osn(self):
        return self.w * self.l

    def s_storony(self):
        return self.l * self.h

    @staticmethod
    def info():
        return dir(Parallelepiped)


p1 = Parallelepiped('3', '3', '4')
'''print(p1.volume())
print(p1.s_osn())
print(p1.s_storony())
print(p1.info())'''

"""2)Напишите класс ListWorker
-принимает в себя неограниченное количество неименованных аргументов и работает с ними как со списком
-Реализуйте методы, которые возвращают
    -только числа
    -только строки
    -все кроме чисел и строк"""


'''class ListWorker:
    def __init__(self, *args):
        self.args = args

    def number(self):
        list1 = []
        for i in self.args:
            if type(i) == int:
                list1.append(i)
        return list1

    def string(self):
        list2 = []
        for i in self.args:
            if isinstance(i, str):
                list2.append(i)
        return list2

    def other(self):
        list3 = []
        for i in self.args:
            if not type(i) == int and not type(i) == str:
                list3.append(i)
        return list3'''
class ListWorker:
    def __init__(self, *args):
        self.args = args

    def numbers(self):
        return list(filter(lambda x: type(x) is int, self.args))

    def string(self):
        return list(filter(lambda x: type(x) is str, self.args))

    def other(self):
        return list(filter(lambda x: type(x) is not int and not str, self.args))

l1 = ListWorker(3, 3, 4, 'aaa', 'bbb', 'ccc', 5, 7.5, None, True, False)
print(l1.numbers())
print(l1.string())
print(l1.other())

"""Есть папка которая содержит 100 файлов со случайными цифрами, но в одной из них есть пароль password
Проверьте все файлы, и найдите пароль. В итоге покажите в консоли номер файла с паролем и содержимое этого файла"""

import os

os.chdir('data')
for i in os.listdir():
    with open(i) as f:
        data = f.read()
        if 'password' in data:
            print(i)
            print(data)
            break

"""Напишите программу которая бы открывала файл и выводила его содержимое. Если попытаться открыть несуществующий файл
то вместо этого она его создаст и запишет туда слово 'Пусто'"""

file = 'фффф.txt'
try:
    with open(file) as f:
        print(f.read())
except FileNotFoundError:
    with open(file, 'w') as f:
        f.write('Пусто')
