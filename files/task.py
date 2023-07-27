import os
import shutil

n = int(input('Введите нужное кол-во папок '))
os.mkdir('result')
os.chdir('result')
for i in range(1, n+1):
    os.mkdir(f'{i}')