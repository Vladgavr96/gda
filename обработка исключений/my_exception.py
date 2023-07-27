class MyException(Exception):
    def __init__(self, text, num):
        self.text =text
        self.num = num

a = int(input('Введите положительное число '))
try:
    if a < 0:
        raise MyException('Число должно было быть положительным, а получено ', a)
except MyException as e:
    print(e)