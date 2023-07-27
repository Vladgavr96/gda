import os
dir_name, file_name = os.path.split(__file__)
n = int(input('Введите нужное кол-во папок '))
if not os.path.exists(f'{dir_name}/result'):
    os.mkdir('result')
os.chdir('result')
for i in range(1, n+1):
    if not os.path.exists(rf'{dir_name}/result/{i}'):
        os.mkdir(f'{i}')